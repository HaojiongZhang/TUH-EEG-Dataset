# TUH-EEG-Dataset
The dataset is organized into a two level hierarchy design with a top level CSVs that summarizes the metadata of the other corpuses. 
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
