# Adversarial Training for Low-Resource Disfluency Correction

This repository contains the code and data used in the above short paper co-authored by Vineet Bhat, Preethi Jyothi and Pushpak Bhattacharyya, accepted at ACL 2023 Findings.

Abstract: Disfluencies commonly occur in conversational speech. Speech with disfluencies can result in noisy Automatic Speech Recognition (ASR) transcripts, which affects downstream tasks like machine translation. In this paper, we propose an adversarially-trained sequence-tagging model for Disfluency Correction (DC) that utilizes a small amount of labeled real disfluent data in conjunction with a large amount of unlabeled data. We show the benefit of our proposed technique, which crucially depends on synthetically generated disfluent data, by evaluating it for DC in three Indian languages- Bengali, Hindi, and Marathi (all from the Indo-Aryan family). Our technique also performs well in removing stuttering disfluencies in ASR transcripts introduced by speech impairments. We achieve an average 6.15 points improvement in F1-score over competitive baselines across all three languages mentioned. To the best of our knowledge, we are the first to utilize adversarial training for DC and use it to correct stuttering disfluencies in English, establishing a new benchmark for this task. 

#### Steps to run the code - 

1) Create a new conda environment and install the necessary packages using the requirements file
   conda create --name <env> --file requirements.txt
2) You will have to convert your dataset into the right format for using the training notebook. Functions in ./utils/ folder can be used for this purpose
  a) Make sure your data is in a csv format with column names - "Disfluent Sentence" and "Fluent Sentence" containing the parallel DC data
  b) Add the path to the above csv file and run python3 ./utils/LabelsFromPairs.py to clean the data, remove punctuations and create corresponding .dis and .labels        files
  c) Add path of ".dis" and ".labels" files create in step 2 b) and run python3 ./utils/PrepareDataset.py to create tsv files for both labeled and unlabeled data. 
3) Run trainer.ipynb notebook to train the model with adversarial training. Appropriate comments and instructions have been mentioned in the notebook.
  
For best training settings and data usage, refer to the paper here: <Link will be added soon>
  
## Citation 
```
@misc{<Will be added soon>,
  doi = {<Will be added soon>},
  
  url = {<Will be added soon>},
  
  author = {Vineet Bhat, Preethi Jyothi, Pushpak Bhattacharyya},
  
  title = {Adversarial training for low-resource disfluency correction},
  
  publisher = {ACL Findings},
  
  year = {2023},
  
  copyright = {MIT}
}


