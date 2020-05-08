# PythonAssignment

This repository contains my Python Assignment for BIO 539

There will be four main files in this repository

1. PythonAssignment1.py
2. PythonAssignment2.py
3. test_PythonAssignment1.py
4. test_PythonAssignment2.py

PythonAssignment1.py and PythonAssignment2.py is the python program to find
linguistic complexity and display the table of observed and possible kmers.
Both file will create a file named kmers_table.txt.

The different between these two is that PythonAssignment2.py also print the
dictionary of sequences in the file it produced.

In PythonAssignment1.py there are 4 functions besides the main function,
in PythonAssignment2.py there are 7 functions besides the main function.

to used the program, you can run in command line with this line:

> python3 PythonAssignment1.py [name of file to be analyzed] [sequence number] 

for example :

> python3 PythonAssignment1.py sampledna.txt 4

[name of file to be analyzed] have to be txt file in correct location
[sequence number] have to be integer

Besides the program, I attach also the testing program :
1. test_PythonAssignment1.py for testing the function in PythonAssignment1.py
2. test_PythonAssignment2.py for testing the function in PythonAssignment2.py

The test will show error about ambiguity of dataframe, because I create
the dataframe with mix data type, so the table will look nice.
And it still work as it supposed to when I run it to a sample file.

To try the program, I also add the sampledna.txt file in this repo.

Crucial improvement needed in the function that remove unnecessary mark,
because sometimes in DNA file it's not only punctuation marks involved,
and the file should only contain the letter A, C, G, and T.

Thank you.
