#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import csv
import re


# In[4]:


df1 = pd.read_csv(r'C:\Users\GURU\.Neo4jDesktop\relate-data\dbmss\dbms-54585cc4-525c-4aa1-92ed-aaaae67c1505\import\sksp_0909.csv')
df1.head(5)


# In[32]:


counter=0
index_list=[]
directed_path=""
result_dict={}
start_val=0
for total in range(0,len(df1)-1):
    directed_path=""
    for index,val in enumerate(df1.iloc[total]):
        splitted=str(val).split(':')
        #rint(splitted)
        for i,v in enumerate(splitted):
            if(re.findall('\\brank\\b', str(v))):
                directed_path+=str(splitted[i+1]).split(',')[0]+'->'
                result_dict[total]=directed_path


# In[33]:



my_dict = result_dict
with open(r'C:\Users\GURU\Desktop\tax_data 26-3\rank_SKtoSP.csv', 'w') as f:
    for key in my_dict.keys():
        f.write("%s\n"%(my_dict[key]))


# In[7]:


linnean_list=['superkingdom','kingdom','phylum','class','order','family','genus','species']


# In[9]:


#Direct read from original file(superkingdom to species)
csv_file = pd.read_csv(r'C:\Users\GURU\.Neo4jDesktop\relate-data\dbmss\dbms-54585cc4-525c-4aa1-92ed-aaaae67c1505\import\sktosp.csv',names=["path"])

for i in range(linnean_list.index(((csv_file.iloc[1][0].split("rank")[1]).split(",")[0])[3:-1])+1,linnean_list.index(((csv_file.iloc[1][0].split("rank")[-1]).split(",")[0])[3:-1])):
    csv_file=csv_file[~csv_file.path.str.contains('\\b'+linnean_list[i]+'\\b')]
    print(len(csv_file))


# In[14]:


#Direct read from original file(king to species)
csv_file = pd.read_csv(r'C:\Users\GURU\.Neo4jDesktop\relate-data\dbmss\dbms-54585cc4-525c-4aa1-92ed-aaaae67c1505\import\ktosp.csv',names=["path"])

for i in range(linnean_list.index(((csv_file.iloc[1][0].split("rank")[1]).split(",")[0])[3:-1])+1,linnean_list.index(((csv_file.iloc[1][0].split("rank")[-1]).split(",")[0])[3:-1])):
    csv_file=csv_file[~csv_file.path.str.contains('\\b'+linnean_list[i]+'\\b')]
    print(len(csv_file))


# In[32]:


#Direct read from original file(phylum to species)
csv_file = pd.read_csv(r'C:\Users\GURU\.Neo4jDesktop\relate-data\dbmss\dbms-54585cc4-525c-4aa1-92ed-aaaae67c1505\import\phtosp.csv',names=["path"])

for i in range(linnean_list.index(((csv_file.iloc[1][0].split("rank")[1]).split(",")[0])[3:-1])+1,linnean_list.index(((csv_file.iloc[1][0].split("rank")[-1]).split(",")[0])[3:-1])):
    csv_file=csv_file[~csv_file.path.str.contains('\\b'+linnean_list[i]+'\\b')]
    print(len(csv_file))


# In[13]:


#Direct read from original file(class to species)
csv_file = pd.read_csv(r'C:\Users\GURU\.Neo4jDesktop\relate-data\dbmss\dbms-54585cc4-525c-4aa1-92ed-aaaae67c1505\import\clstosp.csv',names=["path"])

for i in range(linnean_list.index(((csv_file.iloc[1][0].split("rank")[1]).split(",")[0])[3:-1])+1,linnean_list.index(((csv_file.iloc[1][0].split("rank")[-1]).split(",")[0])[3:-1])):
    csv_file=csv_file[~csv_file.path.str.contains('\\b'+linnean_list[i]+'\\b')]
    print(len(csv_file))


# In[34]:


#Direct read from original file(order to species)
csv_file = pd.read_csv(r'C:\Users\GURU\.Neo4jDesktop\relate-data\dbmss\dbms-54585cc4-525c-4aa1-92ed-aaaae67c1505\import\ordtosp.csv',names=["path"])

for i in range(linnean_list.index(((csv_file.iloc[1][0].split("rank")[1]).split(",")[0])[3:-1])+1,linnean_list.index(((csv_file.iloc[1][0].split("rank")[-1]).split(",")[0])[3:-1])):
    csv_file=csv_file[~csv_file.path.str.contains('\\b'+linnean_list[i]+'\\b')]
    print(len(csv_file))


# In[10]:


#Direct read from original file(family to species)
csv_file = pd.read_csv(r'C:\Users\GURU\.Neo4jDesktop\relate-data\dbmss\dbms-54585cc4-525c-4aa1-92ed-aaaae67c1505\import\famtosp.csv',names=["path"])

for i in range(linnean_list.index(((csv_file.iloc[1][0].split("rank")[1]).split(",")[0])[3:-1])+1,linnean_list.index(((csv_file.iloc[1][0].split("rank")[-1]).split(",")[0])[3:-1])):
    csv_file=csv_file[~csv_file.path.str.contains('\\b'+linnean_list[i]+'\\b')]
    print(len(csv_file))


# In[8]:


#Direct read from original file(superkingdom to phylum)
csv_file = pd.read_csv(r'C:\Users\GURU\.Neo4jDesktop\relate-data\dbmss\dbms-54585cc4-525c-4aa1-92ed-aaaae67c1505\import\sktophy.csv',names=["path"])

for i in range(linnean_list.index(((csv_file.iloc[1][0].split("rank")[1]).split(",")[0])[3:-1])+1,linnean_list.index(((csv_file.iloc[1][0].split("rank")[-1]).split(",")[0])[3:-1])):
    csv_file=csv_file[~csv_file.path.str.contains('\\b'+linnean_list[i]+'\\b')]
    print(len(csv_file))

