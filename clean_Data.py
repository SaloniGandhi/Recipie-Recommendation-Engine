# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 16:44:26 2020

@author: salon
"""
import os
print(os.getcwd())
cd C:\Users\salon\


import pickle
import pandas as pd

data=pd.read_csv('clean_final_1.csv')
print(data.head(5))
data['Ingredients']
ingr_df=data['Ingredients']
type(ingr_df)

ingr_df_clean1=ingr_df_clean
#drop index

ingr_df
ingr_df = pd.DataFrame(ingr_df).reset_index()
ingr_df.columns = ['Index', 'Ingredients']
ingr_df_clean= ingr_df[ingr_df['Ingredients'].isnull() != True]

ingr_df_clean
'''
import string
def remove_punctuations(text):
    for punctuation in '!()-[]{};:'"\<>./?@#$%^&*_~':
        text = text.replace(punctuation, '')
    return text'''
import re
#re.sub(r'^[^a]*', '')
import string
def preprocess(df):
    df['Ingredients'] = df['Ingredients'].str.replace('\d+', '')
    df['Ingredients'] = df['Ingredients'].str.lower()
    df['Ingredients'] = df['Ingredients'].str.replace('(','')
    df['Ingredients'] = df['Ingredients'].str.replace(')','')
    df['Ingredients'] = df['Ingredients'].str.replace('ounce','')
    df['Ingredients'] = df['Ingredients'].str.replace('.','')
    bad_words=['cups','packages','crust','cans','can','inch','pound','pounds','peeled','gallons','package','cup','package','jar','bottle','loaf','"','loaves','-','fluid','gallon','\'"',':',';']
    for i in range(len(df)):
        ingr=df.iloc[i,0]
        for w in bad_words:
            if ingr.find(w):
                ingr=ingr.replace(w,'')
                ingr=ingr.replace('/', '')
                ingr=ingr.replace(':', '')
                ingr=ingr.replace('"', '')
                ingr=ingr.replace('\'', '')
                ingr=ingr.strip()
                df.iloc[i,0]=ingr
    return df
ingr_df_submit=ingr_df.drop(['Index'],axis=1)
ingr_df_submit
preprocess(ingr_df_submit)

print("its perfect")
#convert to list of lists
#successfully extract each row of the given data frame into a list
# Empty list 
row_list =[] 

# Iterate over each row 
for index, rows in ingr_df_submit.iterrows(): 
    # Create list for the current row 
    my_list =[rows.Ingredients] 

    # append the list to the final list 
    row_list.append(my_list) 

# Print 

import csv
with open('C:\\Users\\salon\\Desktop\\ingr_df_submit.csv', 'w') as outcsv:   
    #configure writer to write standard csv file
    writer = csv.writer(outcsv, delimiter=',')
    writer.writerow(['Ingredients'])
    for item in row_list:
        #Write item to outcsv
        writer.writerow([item])

#ingr_df_submit.to_csv('C:\\Users\\salon\\Desktop\\ingr_df_submit.csv')
file2="C:\\Users\\salon\\Desktop\\DataSci\\proj\\yummly_clean.pkl"
yummly_clean_df=pd.read_pickle(file2)
for col in yummly_clean.columns:
       print(col)
print(type(yummly_clean_df))
yummly_clean_ingr_df=yummly_clean_df['ingredients']
yummly_clean_ingr_df
yummly_clean_ingr_df.to_csv('C:\\Users\\salon\\Desktop\\DataSci\\proj\\yummly_clean_df_ingr.csv')
