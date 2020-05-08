#!/usr/bin/env python3 

from PythonAssignment2 import *
import pytest

def test_tidyup():
  ex_tidy = "ACGTTGA;:,."
  dna_list = get_dnalist(ex_tidy)
  assert dna_list == "ACGTTGA"

def test_create_list_dict():
  ex_dna = "AGGTGTA"
  seq_list = get_sequence(ex_dna,2)
  assert seq_list == [{'A':2,'G':3,'T':2},{'AG':1,'GG':1,'GT':2,'TG':1,'TA':1}]

def test_observed_kmers():
  ex_list_seqo = [{'A':2,'G':3,'T':2},{'AG':1,'GG':1,'GT':2,'TG':1,'TA':1}]
  obs_list = get_observedk(ex_list_seqo,2)
  assert obs_list == [3,5,8]
  
def test_possible_kmers():
  ex_list_seqp = [{'A':2,'G':3,'T':2},{'AG':1,'GG':1,'GT':2,'TG':1,'TA':1}]
  pos_list = get_possiblek(ex_list_seqp,2)
  assert pos_list == [7,6,13]
  
def test_table():
  import pandas as pd
  ob_list = [3,5,8]
  po_list = [7,6,13]
  list_seq = [{'A':2,'G':3,'T':2},{'AG':1,'GG':1,'GT':2,'TG':1,'TA':1}]
  table = get_dataframe(2,ob_list,po_list,list_seq)
  tab = {'k':[1,2,'Total'],
         'observed kmers':[3,5,8],
         'possible kmers':[7,6,13],
         'list of sequence':[{'A':2,'G':3,'T':2},{'AG':1,'GG':1,'GT':2,'TG':1,'TA':1},'END OF SEQUENCES']}
  assert table == pd.DataFrame(tab)

def test_linguistic():
  import pandas as pd
  tab_ling = {'k':[1,2,'Total'],
              'observed kmers':[3,5,8],
              'possible kmers':[7,6,13],
              'list of sequence':[{'A':2,'G':3,'T':2},{'AG':1,'GG':1,'GT':2,'TG':1,'TA':1},'END OF SEQUENCES']}
  tbl = pd.DataFrame(tab_ling)
  ling_comp = get_linguistic_complexity(tbl,2)
  assert ling_comp == 8/13
