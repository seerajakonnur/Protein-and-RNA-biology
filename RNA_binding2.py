import pandas as pd
import numpy as np
data=pd.read_csv("2nd.txt")
data2=data.drop_duplicates()

data2.to_csv("2nd.txt", index=False, header=True)
f=open("2nd.txt","r")
file1=f.readlines()
with open('combination1.txt', 'w') as f:
 for i in file1:
  i=i.replace('U', 'A')
  i=i.replace('G', 'U')
  i=i.replace('s', 'U')
  i=i.replace('r', 'C')
  i=i.replace('q', 'G')
  i=i.replace('t', 'G')
  f.write("%s\n" % i)
 


data=pd.read_csv("3rd.txt")
data2=data.drop_duplicates()

data2.to_csv("3rd.txt", index=False, header=True)
f=open("3rd.txt","r")
file1=f.readlines()
with open('combination2.txt', 'w') as f:
 for i in file1:
  i=i.replace('U', 'G')
  i=i.replace('t', 'A')
  i=i.replace('s', 'U')
  i=i.replace('r', 'C')
  i=i.replace('q', 'G')
  i=i.replace('m', 'U')
  f.write("%s\n" % i)

data=pd.read_csv("4th.txt")
data2=data.drop_duplicates()

data2.to_csv("4th.txt", index=False, header=True)
f=open("4th.txt","r")
file1=f.readlines()
with open('combination3.txt', 'w') as f:
 for i in file1:
  i=i.replace('U', 'A')
  i=i.replace('t', 'G')
  i=i.replace('s', 'U')
  i=i.replace('r', 'U')
  i=i.replace('q', 'G')
  i=i.replace('m', 'C')
  f.write("%s\n" % i)
 

data=pd.read_csv("5th.txt")
data2=data.drop_duplicates()

data2.to_csv("5th.txt", index=False, header=True)
f=open("5th.txt","r")
file1=f.readlines()
with open('combination4.txt', 'w') as f:
 for i in file1:
  i=i.replace('U', 'G')
  i=i.replace('t', 'A')
  i=i.replace('s', 'U')
  i=i.replace('r', 'U')
  i=i.replace('q', 'G')
  i=i.replace('m', 'C')
  f.write("%s\n" % i)



