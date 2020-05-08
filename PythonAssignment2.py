#!/usr/bin/env python3 

import sys #use interactive with user
import pandas as pd #use pandas dataframe 

def get_dnatext(filename): #run this chunk with the (filename) given by user
    with open(filename, "r") as f: #open the file as entered by the user
      dnatext = f.read() #reading text in the file store it to dnatxt
    return(dnatext) #return the value of this function as "dnatext"

def get_dnalist(dnatext): #run this chunk with (dnatext) from previous function
    """
    Take a string of text and removes unnecessary symbols
      Args:
        dnatext: string
    Returns:
      string
    """
    dnalist = dnatext #set dnalist as dnatext for filtering unnecessary mark that will disturb data processing
    unlisted = [".",",",";",":",'"'," ","'","@","#","*"] #unlisted contains symbols that need to be removed
    for mark in unlisted: #loop through punctuation list
      dnalist = dnalist.replace(mark,"") #replace each punctuation mark in the dnatext and save the new string in dnalist
    return(dnalist) #return the value of this function as "dnalist"

def get_sequence(dnalist,k): #run this chunk with (dnalist) from previous function and (k) as defined by user
    """
    Take a string of text and makes a list of dictionary
    Args:
      dnalist: string
    Returns:
      list of dictionary
    """
    while k < len(list(dnalist)): #k cannot exceed the lenght of dna
      sequences = [] #set the initial list of the collection of sequence to "sequences"
      for h in range(k): #loop in the range of k
          seq_dict = {} #create initial dictionary name seq_dict
          g = h + 1 #since python is 0 base language, I set this because I want to start the loop from 1 to k
          p_seq = len(dnalist) - g + 1 #possible dna sequence at each loop is set by this formula of "p_seq"
          for i in range(p_seq): #create loop inside the loop with the "p_seq" as the range, for each main loop
              seq = dnalist[i:i+g] #defined "seq" as part of dnalist taken from character i to i+g
              if seq not in seq_dict: #if the part in "seq" is not in the "seq_dict" ->
                  seq_dict[seq] = 1 #then add "seq" to the dictionary
              else: #if everything else ->
                  seq_dict[seq] += 1 #then pass it
              sequence = seq_dict #set sequence (without 's' :-D ) as the dictionary of seq_dict in each loop
          sequences.append(sequence) #for each main loop, add "sequence" in "sequences"
      return(sequences) #return the value of this function as the list of "sequences"

def get_observedk(sequences,k): #this function count the observed kmers, with the (sequences) from previous function and (k) as defined by user
    """
    Take a list of dictionary and makes a list of number
    Args:
      sequences: list of dictionary
    Returns:
      list of number
    """
    obs_seq = [] #set "obs_seq" for the list of count of observed sequence
    for i in range(k): #loop in range (k)
        obs_seq.append(len(sequences[i])) #add the value of "ob_seq" by counting the number of observed sequences in "sequences" database
    obs_seq.append(sum(obs_seq)) #add the total counting as the last data
    return(obs_seq) #return the value of this function as the list of obs_seq

def get_possiblek(sequences,k): #this function count the possible kmers, with the (sequences) from previous function and (k) as defined by user
    """
    Take a list of dictionary and makes a list of number
    Args:
      sequences: list of dictionary
    Returns:
      list of number
    """
    pos_seq = [] #set "pos_seq" for the list of number of possible sequences
    for i in range(k): #loop in range (k)
        seq_pos = sum(sequences[i].values()) #set "seq_pos" as the sum of frequency value in the part of dictionary "sequences"
        pos_seq.append(seq_pos) #add the value of "seq_pos" to the list of "pos_seq"
    pos_seq.append(sum(pos_seq))#add the total counting as the last data
    return(pos_seq) #return the value of this function as the list of pos_seq
    
def get_dataframe(k,obs_seq,pos_seq,sequences): #create dataframe using k from user, and (obs_seq,pos_seq,sequences) from previous function    
    """
    Combine several lists and makes a dataframe
    Args:
      list: list of number, list of dictionary
    Returns:
      dataframe
    """
    blank = "END OF SEQUENCES" #I create this to be added in the last data of sequences, so all of my list have the same number of data
    sequences.append(blank) #Add the "blank" to the last data of sequences as identifier of the end list
    dnasequence_df = pd.DataFrame( #create pandas dataframe and name it as "dnasequence_df"
        {'k':range(1,k+2), #k is the number of row to be put in the first column of the data frame (start from one until k+1), I use (1,k+2) because python is 0 based
        'observed kmers':obs_seq, #this column is from the list of obs_seq
        'possible kmers':pos_seq, #this column is from the list of pos_seq
        'list of sequence':sequences #this column show the list of sequences and its frequency
        }
    )
    
    dnasequence_df.loc[k,'k'] = 'Total' #I change the last row of 'k' column to "Total" just to make the table clear 
    return(dnasequence_df) #return the value of this function as dataframe "dnasequence_df"

def get_linguistic_complexity(dnasequence_df,k): #this function use (dnasequence_df) from the previous function and k from user
    """
    Take a dataframe and makes a number
    Args:
      dnasequence dataframe: dataframe
    Returns:
      number
    """
    obs = dnasequence_df.loc[k].at['observed kmers'] #set "obs" as the value of total observed count, taken from the last row of column 'observed kmers'
    pos = dnasequence_df.loc[k].at['possible kmers'] #set "pos" as the value of total observed count, taken from the last row of column 'possible kmers'
    linguistic_complexity = int(obs)/int(pos) #count lingustic complexity as a ratio of obs/pos (after they set to integer data, numeric data could be used as well, but since it's observation it should counts 1,2,3 etc.)
    return(linguistic_complexity) #return the value of this function as "linguistic_complexity"
    
if __name__ == '__main__': #if this script run, run the following
  myfile = sys.argv[1] #load myfile in the command line
  k = int(sys.argv[2]) #load the k (sequence number) in the command line
  
  try:
    dnatext = get_dnatext(myfile) #get list of DNA from user's DNA file input
  except IOError: #if error in reading the file, print the following messages
    print("Could not read file: ",sys.argv[1],", write the correct filename follow by the sequence") 
    print("for example: python3[space]pythonassign.py[space]filename.txt[space]7")
  
  dnalist = get_dnalist(dnatext) #get dnalist from the function "get_dnalist"
  
  try:
    seq = get_sequence(dnalist,k) #get list of DNA sequence and its frequency (dictionary) using get_sequence function
    observed = get_observedk(seq,k) #get list of observed count using get_observedk function
    possible = get_possiblek(seq,k) #get list of possible count using get_possiblek function
    seq_table = get_dataframe(k,observed,possible,seq) #get table using get_dataframe function
    ling_comp = get_linguistic_complexity(seq_table,k) #get linguistic complexity using get_linguistic_complexity function
  except TypeError: #if k value more than the dna length then print the following, asking user to enter value lower than dna length
    print("Sequence number should be smaller than ",len(list(dnalist)))  
  
  #the following is to print the table and linguistic complexity on the screen
  print("")
  print(seq_table[['k','observed kmers','possible kmers']]) #here only the first three column is printed
  print("")
  print("Linguistic Complexity is ",ling_comp)
  print("")

  #the following print the table in file, named kmers_table.txt
  with open('kmers_table.txt', 'w') as f:
      with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None):
          print(seq_table, file=f)
