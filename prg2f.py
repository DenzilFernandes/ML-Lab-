from csv import reader
def classify(hyp,row):
	for a,b in zip(hyp,row):
		if not (a=='?' or a==b):
			return 'No'
	return 'Yes'
with open('Dataset1.csv') as file:
	data=[row for row in reader(file)]

posData=[row[:-1] for row in data if row[-1]=='Y']
negData=[row[:-1] for row in data if row[-1]=='N']
hypLen=len(data[0])-1
spcHyp=posData[0]
genHyp=[['?']*hypLen]
for row in posData[1:]:
	spcHyp=['?' if comp[0]!=comp[1] else comp[0] for comp in zip(spcHyp,row)]
for row in negData:
	newHyp=[]
	for hyp in genHyp:
		if classify(hyp,row)=='Yes':
			cand=[hyp[:] for i in range(hypLen)]
			for i in range(hypLen):
				if cand[i][i]=='?':
					cand[i][i]=spcHyp[i]
			newHyp+=cand
	genHyp+=newHyp
	genHyp=[hyp for hyp in genHyp if classify(hyp,row)=='No']
	#genHyp = list(dict.fromkeys(genHyp))
print("Specific Hypothesis: ",spcHyp)
print("General Hypotheses: ", genHyp)