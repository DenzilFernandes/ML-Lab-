import numpy as np
import csv
data = np.array([i for i in csv.reader(open('in2.csv'))])
print(data)
s=['$']*6
g=[]
for i in range(6):
	g.append(['?']*6)
print("Specic Set:")
print(s)
print("General Set:")
print("[")
for x in g:
	print(x)
print("]")
for row in data:
	if row[6]=='+':
		for j in range(len(row)-1):
			if s[j]=='$':
				s[j]=row[j]
			elif row[j]!=s[j]:
				s[j]='?'
			if s[j]!=g[j][j] and g[j][j]!='?':
				g[j][j]='?'
	else:
		for j in range(len(row)-1):
			if row[j]!=s[j]:
				g[j][j]=s[j]
	print ("\nspecific Set : ")
	print (s)
	print ("\nGeneral Set : ")
	print("[")
	for x in g:
		print(x)
	print("]")
