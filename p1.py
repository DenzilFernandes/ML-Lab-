import csv
filename='1-dataset.csv'
lines=csv.reader(open(filename))
data=list()

for row in lines:
#FIND-S uses only positive examples
	if(row[-1]=='Yes'):
		data.append(row)

for x in data:
	print(x)

numberOfRows=len(data)
numberOfCols=len(data[0])-1

hypothesis=['%' for _ in range(numberOfCols)]

print("No. of rows:",numberOfRows)
print("No. of cols:",numberOfCols)
print("Initial Hypothesis:",hypothesis)
hypothesis=data[0][:-1]
for i in range(numberOfRows):
	for j in range(numberOfCols):
		
		if(hypothesis[j]!=data[i][j]):
			hypothesis[j]='?'
		else:
			None

print("final Hypothesis:",hypothesis)
print("Input new testcase:")
testcase=input()
testcase=testcase.split(',')
print("testcase:")
print(testcase)



flag=1
for i in range(len(hypothesis)):
	if(hypothesis[i]!='?'):
		if(hypothesis[i]!=testcase[i]):
			flag=0
			break
if (flag==1):
	print("Accepted")
else:
	print("Rejected")



