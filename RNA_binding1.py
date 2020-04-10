# To find possible binding partners for a given RNA sequence. In RNA sequence U can bind to 'A' and 'G'. 'U.G' is wobble base pairing. 'G' binds to 'C' and 'U'. 'A' binds to 'U' , and 'C' binds to 'G'. Therefore theoretically there can be many possible sequences which will be able to bind the given RNA sequence.
 
import pandas as pd
import numpy as np

# Read the fasta file that contains the RNA sequence (NOTE: The sequence must be without any new line characters)

f=open("Fe1.fasta","r")
file1=f.readlines()

# Setting the counter to zero for counting 'C' and 'G'

uc=0
ug=0

for i in file1[0]:
 if i=='U':
  uc=uc + 1


for i in file1[0]:
 if i=='G':
  ug=ug + 1


if uc==ug:
 largest=uc
elif uc>ug:
 largest=uc
else:
 largest=ug
a=np.arange(1,(largest+1),1)

# Replacing with temp characters

file1[0]= file1[0].replace('C', 'q') 
file1[0]= file1[0].replace('A', 's')

# U to G and G to C

with open('2nd.txt', 'w') as f:
 for i,j in zip(file1[0],a):
  str1=file1[0].replace('U', 't', j)
  for i,j in zip(file1[0],a):
    str2=str1.replace('G', 'r', j)
    print(str2)
    f.write("%s\n" % str2)

# U to A and G to C

file1[0]= file1[0].replace('G', 'm')
with open('3rd.txt', 'w') as f:
 for i,j in zip(file1[0],a):
  str2=file1[0].replace('U', 't', j)
  for i,j in zip(file1[0],a):
    str3=str2.replace('m', 'r', j)
    print(str3)
    f.write("%s\n" % str3)

# U to G and G to U

file1[0]= file1[0].replace('G', 'm')
with open('4th.txt', 'w') as f:
 for i,j in zip(file1[0],a):
  str1=file1[0].replace('U', 't', j)
  for i,j in zip(file1[0],a):
    str2=str1.replace('m', 'r', j)
    print(str2)
    f.write("%s\n" % str2)

# U to A and G to U

file1[0]= file1[0].replace('G', 'm')
with open('5th.txt', 'w') as f:
 for i,j in zip(file1[0],a):
  str1=file1[0].replace('U', 't', j)
  for i,j in zip(file1[0],a):
    str2=str1.replace('m', 'r', j)
    print(str2)
    f.write("%s\n" % str2)





