# TUH-EEG-Dataset
This project seeks to acquire and reformat the 30,000 EEG patient files provided by the Temple Univeristy Hospital into a database that's easy for acquiring clean epochs for training machine learning models and to gain a global view about the connections between each individual corpuses.
The dataset is organized into a two level hierarchy design with a top level CSV that summarizes the metadata of the other corpuses. 
Each row is uniquely deteremined by a patient Id and session number combination, which combined with certain labels/artifacts can be used to
acquire specific information from the lower level CSVs.

**Summary of Files**

Extract.py:

Example code for extracting and parsing data from the TUSZ corpus

Label.py:

Code for extracting data from .lbl and .tse files from the TUH corpuses

Queries.py:

Code for querying the database

database folder:
outline of the two level csv design consisting of:
- top entity
- TUAB corpus
- TUAR corpus
- TUEP corpus
