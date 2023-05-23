import random

create_unlabeled_data = True # If set to true, this file will create tsv file for unlabelled data, ie, without any labels after \t (UNK)

disfluent_sentences_path = "./data/data.dis"
disfluen_labels_path = "./data/data.labels" # no need to use if create_unlabeled_data=True


if(create_unlabeled_data==False):
  

  lines = open(disfluent_sentences_path,'r').readlines()
  labels = open(disfluent_sentences_path,'r').readlines()


  temp = list(zip(lines, labels))
  random.shuffle(temp)
  res1, res2 = zip(*temp)
  # res1 and res2 come out as tuples, and so must be converted to lists.
  lines, labels = list(res1), list(res2)


# In[7]:


  split = [0.8,0.1,0.1]
  
  with open('./data/train-labeled.tsv','w') as write_tsv:
      i = 0
      for x,y in zip(lines,labels):
          write_tsv.write(x[:-1]+"\t"+y[:-1].strip())
          write_tsv.write("\n")
          i+=1
          if(i==int(split[0]*len(lines))):
              break
          
  with open('./data/valid-labeled.tsv','w') as write_tsv:
      i = 0
      for x,y in zip(lines,labels):
          if(i<int(split[0]*len(lines))):
              i+=1
              continue
          write_tsv.write(x[:-1]+"\t"+y[:-1].strip())
          write_tsv.write("\n")
          i+=1
          if(i==int(sum(split[:2])*len(lines))):
              break
              
          
  with open('./data/test-labeled.tsv','w') as write_tsv:
      i = 0
      for x,y in zip(lines,labels):
          if(i<int(sum(split[:2])*len(lines))):
              i+=1
              continue
          write_tsv.write(x[:-1]+"\t"+y[:-1].strip())
          write_tsv.write("\n")
          i+=1
          
else(create_unlabeled_data==True):

  lines = open(disfluent_sentences_path,'r').readlines()
  
  random.shuffle(lines)
  
  with open('./data/train-unlabeled.tsv','w') as write_tsv:

      for i,x in enumerate(lines):
          write_tsv.write(x[:-1]+"\t"+"UNK".strip())
          write_tsv.write("\n")
          

          
  
  
  
  
        
        





