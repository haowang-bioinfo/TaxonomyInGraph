#!/usr/bin/env python
# coding: utf-8

# In[7]:


import PySimpleGUI as sg
import time
from neo4j import GraphDatabase
import pandas as pd
import csv
#DB info
uri             = "bolt://localhost:7687"
userName        = "neo4j"
password        = "1234"
header_list=[]
data=[]
result_dict={}
result=[]
result=''
node1_rank=''
node2_rank=''
background_image=r'C:\Users\GURU\Desktop\26-06-21 Thesis\Screenshots 20-07\bg.png'
top_banner = [[sg.Text('Chalmers University of Technology', font='Any 20', background_color='black')]]
top  = [[sg.Text("Taxonomy Information Toolbox", size=(50,1),font='Any 20',background_color='black')]]
distance_block = [[sg.Text('Distance Estimation', font='Any 20',background_color='black')],
            [ sg.Text('"Source Tax_ID"',background_color='black'),sg.Input()],
            [ sg.Text('"Destination Tax_ID"',background_color='black'),sg.Input()],
            [sg.Button('Find Distance'), sg.Button('Exit')]  ]
layout = [[sg.Column(top_banner, size=(455, 60), pad=(0,0), background_color='black')],
          [sg.Column(top, size=(455, 60),background_color='black')],
          [sg.Column(distance_block, size=(455,150),background_color='black')],[sg.Image(background_image)]]
                     
def make_window2(distance,data,header_list):
    layout = [[sg.Text('Path is ordered from the source to destination',background_color='black')],
              [[sg.Text('Distance:',background_color='black')],[sg.Text(distance,background_color='black')]],
              [sg.Table(values=data,
                  headings=header_list,
                  display_row_numbers=False,
                  auto_size_columns=True,
                  num_rows=min(25, len(data)),background_color='black')]]

    return sg.Window('Path Information', layout, finalize=True,background_color='black')

def val_extract(item,loc):
    extracted_val=str(item).split(',')[loc]
    final_val=str(extracted_val).split(':')[1]
    return final_val

def dict_tocsv(path_dict):
    my_dict = path_dict
    with open(r'C:\Users\GURU\Desktop\tax_data 26-3\path-finding.csv', 'w') as f:
        for key in my_dict.keys():
            f.write("%s\n"%(my_dict[key]))
    csv_file = pd.read_csv(r'C:\Users\GURU\Desktop\tax_data 26-3\path-finding.csv', 
                  sep=',',names=["Tax_id","Rank","Scientific_name"])
 
    csv_file.to_csv(r'C:\Users\GURU\Desktop\tax_data 26-3\path-finding.csv', encoding='utf-8', index=False)
       
    return csv_file


def db_connection(event,cql_distance,cql_table):
     # Execute the CQL query
    graphDB_Driver  = GraphDatabase.driver(uri, auth=(userName, password))
    with graphDB_Driver.session() as graphDB_Session:       
        
        if event=='Find Distance':
            nodes = graphDB_Session.run(cql_distance)
            for node in nodes:
                distance=node[0]
            time.sleep(0.5)
            node_table = graphDB_Session.run(cql_table)
            for node in node_table:
                result=node[0]
            count=0
            path_dict={}
            for index,item in enumerate(result):
                rank=val_extract(item,0)
                sc_name=val_extract(item,1)
                tax_id=val_extract(item,2)
                path_dict[count]=tax_id+','+rank+','+sc_name
                count+=1
            table=dict_tocsv(path_dict)
            
            return distance,table


window = sg.Window('Neo4j-GUI', layout, margins=(0,0), background_color='black', no_titlebar=False, grab_anywhere=True)

while True:            
    event, values = window.read()
    window_2= None
    if event=='Find Distance':
        print(event)
        cql_distance='match path = shortestpath((p:node {id: '+values[0]+'})-[:HAS_CHILD*1..]-(c:node {id: '+values[1]+'})) return length(path),p.rank,c.rank,p.scientific_name,c.scientific_name'
        cql_table= 'match path = shortestpath((:node {id: '+values[0]+'})-[:HAS_CHILD*1..]-(:node {id: '+values[1]+'})) return nodes(path)'
        distance,table_output=db_connection(event,cql_distance,cql_table)    
        header_list = list(table_output.columns)
        data = table_output[0:].values.tolist()
        window2 = make_window2(distance,data,header_list)
        window2.refresh()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()


# In[ ]:




