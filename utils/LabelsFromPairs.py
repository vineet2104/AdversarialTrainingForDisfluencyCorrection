
import os
import argparse
from os import path
import pandas as pd

disfluent_fluent_parallel_data = "./data/data.csv"
# CSV file should have the following columns - "Disfluent Sentence" and "Fluent Sentence"


def isSubSequence(str1, str2):
    m = len(str1)
    n = len(str2)
 
    j = 0   
    i = 0    
 
    while j < m and i < n:
        if str1[j] == str2[i]:
            j = j+1

        i = i + 1
 
    return j == m
    
def clean_text(test_str):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 
    # Removing punctuations in string
    # Using loop + punctuation string
    for ele in test_str:
        if ele in punc:
            test_str = test_str.replace(ele, "")
    
    new_sent = ""
    for w in test_str.lower().strip().split(" "):
        if(w==''):
            continue
        else:
            new_sent = new_sent + w + " "
        
    # printing result
    return new_sent.strip().replace("।","")




df = pd.read_csv(disfluent_fluent_parallel_data)
disfluent = df['Disfluent Sentence']
fluent = df['Fluent Sentence']

with open('./data/data_clean.dis','w') as write_file:
    for d in disfluent:
        write_file.write(clean_text(d))
        write_file.write("\n")

with open('./data/data_clean.flu','w') as write_file:
    for d in fluent:
        write_file.write(clean_text(d))
        write_file.write("\n")
    


disfluent_path = "./data/data_clean.dis"
fluent_path = "./data/data_clean.flu"



with open(disfluent_path, 'r') as dis, open(fluent_path, 'r') as flu, open("./data/data.dis", 'w') as dis_out, open("./data/data.labels", 'w') as label_out:
    dis = dis.readlines()
    flu = flu.readlines()
    subsequence = 0

    for dis_line, flu_line in zip(dis, flu):
        
        dis_line = dis_line.strip()
        flu_line = flu_line.strip()

        if flu_line == "None":
            flu_line = ""

        # Find those sentence pairs where fluent sentence is a subsequence of disfluent sentence
        if isSubSequence(flu_line, dis_line): 
            
            subsequence += 1
            dis_words = dis_line.split()
            flu_words = flu_line.split()

            i = len(dis_words) - 1
            j = len(flu_words) - 1
            
            labels = [1] * len(dis_words) # 0 means this word is part of disfluency

            while i >= 0:
                if j >= 0 and dis_words[i] == flu_words[j]:
                    labels[i] = 0 # Means dis_words[i] is not disfluent
                    j -= 1
            
                i -= 1
            
            dis_out.write(dis_line + "\n")
            label_out.write(' '.join(map(str, labels)) + "\n")
        else:
            print("The following pair cannot be used for sequence tagging")
            print("Fluent:", flu_line)
            print("Disfluent:", dis_line)
            print()

    print("{} fluent sentences are subsequence of corresponding disfluent sentence out of {} sentences".format(subsequence, len(dis)))








