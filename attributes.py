import array
import pandas as pd
import numpy as np
from pandas import read_csv
import csv
import statistics
import modlamp
from modlamp.descriptors import PeptideDescriptor, GlobalDescriptor
# Reading the csv file and saving in data
data=pd.read_csv("motifs.csv")
# Saving it into multidimesional array
arr_motifs=data.values
# Defining arrays
arr_len=[]
motif=[]
ch=[]
ch_den=[]
ip=[]
ii=[]
bi=[]
hr=[]
ar=[]
al=[]
for i in arr_motifs:
 print(i[0])
 motif.append(i[0])
 arr_len.append(len(i[0]))


# charge
for i,j in zip(arr_motifs, arr_len):
 desc = GlobalDescriptor(i[0])
 desc.calculate_charge(ph=7.4, amide=True)
 ch.append(desc.descriptor/j)


#hydrophobic ratio
for i,j in zip(arr_motifs, arr_len):
 desc = GlobalDescriptor(i[0])
 desc.hydrophobic_ratio()
 hr.append(desc.descriptor/j)

# aromaticity
for i,j in zip(arr_motifs, arr_len):
 desc = GlobalDescriptor(i[0])
 desc.aromaticity()
 ar.append(desc.descriptor/j)

# aliphatic index
for i,j in zip(arr_motifs, arr_len):
 desc = GlobalDescriptor(i[0])
 desc.aliphatic_index()
 al.append(desc.descriptor/j)
# ii

data2=pd.read_csv("ii_nef_pred.csv")
arr_ii=data2.values
arr_ii2=arr_ii[:,0]
print(arr_ii2)

for i,j in zip(arr_ii2, arr_len):
 ii.append(i/j)

data2=pd.read_csv("ip_nef_pred.csv")
arr_ip=data2.values
arr_ip2=arr_ip[:,0]
print(arr_ip2)

for i,j in zip(arr_ip2, arr_len):
 ip.append(i/j)

df = pd.DataFrame({"motif" : motif, "charge" : ch, "hr" : hr,  "aromaticity" : ar, "aliphatic_index" : al, "ii" : ii, "ip" : ip })
df.to_csv("attributes_nef_pred.csv", index=False)




 



