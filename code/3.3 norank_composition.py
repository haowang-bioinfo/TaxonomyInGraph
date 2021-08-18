# import the neo4j driver for Python
#code for compositional distribution of "norank"
from neo4j import GraphDatabase
import csv
import pandas as pd
# Database Credentials
uri             = "bolt://localhost:7687"
userName        = "neo4j"
password        = "1234"
graphDB_Driver  = GraphDatabase.driver(uri, auth=(userName, password))
result_dict={}
rank_name_list=['superkingdom','kingdom','phylum','class','order','family','genus','species']
itercount=0
for index,item in enumerate(rank_name_list):
        cql='MATCH (n {rank:"'+item+'"})-[r:HAS_CHILD]->(p {rank:"norank"}) Return count(r)'
        with graphDB_Driver.session() as graphDB_Session:
            nodes = graphDB_Session.run(cql)
            for node in nodes:
                print(item,node[0])
                result_dict[itercount]=item+','+str(node[0])
                itercount+=1

#CSV file generation
my_dict = result_dict
with open(r'C:\Users\GURU\Desktop\tax_data 26-3\norank_composition.csv', 'w') as f:
    for key in my_dict.keys():
        f.write("%s\n"%(my_dict[key]))

csv_file = pd.read_csv(r'C:\Users\GURU\Desktop\tax_data 26-3\norank_composition.csv', 
                  sep=',', 
                  names=["parent_rank","norank_count"])


csv_file.to_csv(r'C:\Users\GURU\Desktop\tax_data 26-3\norank_composition.csv', encoding='utf-8', index=False)
    
