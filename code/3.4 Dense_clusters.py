#import the neo4j driver for Python
#Code for identifying dense clusters
import pandas as pd
from collections import Counter
df=pd.read_csv(r'C:\Users\GURU\Desktop\tax_data 14-08\Final.csv')

#Counter to find count of each ranks
dense_dict=Counter(df['parent tax_id'])

#Sorting the values in descending order based on count
result_list=sorted(dense_dict.items(), key=lambda pair: pair[1], reverse=True)       
result_dict={}
count=0
for index,data in enumerate(result_list):
    result_dict[result_list[index][0]]=result_list[index][1]

result_df=pd.DataFrame.from_dict(result_dict, orient='index',columns=['Count of child nodes'])    
result_df = result_df.reset_index()
result_df.rename(columns = {'index':'tax_id'}, inplace = True)          
#result_df      
final_df= pd.merge(result_df, df,how='left',left_on='tax_id',right_on='tax_id')

#Using first 100 dense clusters called as norank_df(contains "norank")
norank_df=final_df.head(100)

#Saving 100 rows to csv named Dense_with_norank
norank_df.to_csv(r'C:\Users\GURU\Desktop\tax_data 26-3\Dense_with_No-rank.csv',encoding='utf-8', index=False)

#Remove no-ranks from the dataframe and saving csv
norank_df.drop(norank_df[norank_df['rank'] == 'norank'].index, inplace = True)
norank_df.to_csv(r'C:\Users\GURU\Desktop\tax_data 26-3\Dense_without_No-rank.csv',encoding='utf-8', index=False)
