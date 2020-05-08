#!/usr/bin/env python3 

from PythonAssignment1 import *
import pytest

def test_tidyup():
  ex_tidy = "ACGTTGA;:,."
  dna_list = get_dnalist(ex_tidy)
  assert dna_list == "ACGTTGA"

def test_create_table():
  import pandas as pd
  ex_dna = "AGGTGTA"
  table_seq = get_sequence(ex_dna,2)
  table = {'k':[1,2,'Total'],
         'observed kmers':[3,5,8],
         'possible kmers':[7,6,13]}
  assert table_seq == pd.DataFrame(table)

def test_linguistic():
  import pandas as pd
  tab_ling = {'k':[1,2,'Total'],
              'observed kmers':[3,5,8],
              'possible kmers':[7,6,13]}
  tbl = pd.DataFrame(tab_ling)
  ling_comp = get_linguistic_complexity(tbl,2)
  assert ling_comp == 8/13
