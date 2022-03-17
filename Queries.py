from dataclasses import dataclass
from pathlib import Path
import itertools
from attr import field
import pandas as pd
import glob
import csv
import itertools
import os
from collections import defaultdict

class Query:
    def __init__(self):
        self.pathTUSZ = '/scr/shared/TUH_SEIZURE/edf'               #Seizure Corpus
        self.pathTUAR = "/scr/shared/TUH_ARTIFACTS_v2"              #Artifact Corpus
        self.pathTUEP = '/scr/shared/TUH_EPILEPSY/edf'              #Epilepsy Corpus
        self.pathTUAB = '/shared/TUH/tuh_eeg_abnormal/v2.0.0/edf'   #Abonormal Corpus

        self.topEntity = 'topEntity.csv'

        self.trainEval = {'TUAB':{'train':'TUAB_train','eval':'TUAB_eval'}}  #list of corpus with train/eval labels
        self.index = {'TUAB': 'TUAB_Norm', 'TUEP':'TUEP_Epilepsy', 'TUAR': 'TUAR_Artifacts'}
        self.paths = {'TUSZ':self.pathTUSZ, 'TUEP':self.pathTUEP, 'TUAB':self.pathTUAB, 'TUAR':self.pathTUAR}
    
    #takes in a list of corpuses and return the patient/session pair of patients that have the label
    def getIntersect(self,corpuses,labels):
        patient = []
        patientCSV = []
        df = pd.read_csv(self.topEntity)

        tmp = df[self.index[corpuses[0]]].dropna()
        rows = tmp.index.tolist()
        tmp = df.iloc[rows,:]

        
        for subset, label in zip(corpuses, labels):
            tmp = tmp[self.index[subset]].dropna()
            rows = tmp.index.tolist()
            tmp = df.iloc[rows,:]
            tmp = tmp[tmp[self.index[subset]]==label]
        patientID = list(zip(tmp['Patient Id'],tmp['Session']))

        



        return patientID

    def getCleanCorpus(self,corpus,ignore):
        df = pd.read_csv(self.topEntity)


    #given a unique patient/session pair returns all the information about said patient in the top level
    #when full = True return all the info retaining to the patient accross multiple sessions
    def getPatient(self,patient,full=False):
        patientID = patient[0]
        Session = patient[1]
        df = pd.read_csv(self.topEntity)
        if full:
            return df[df['Patient Id']==patientID]
        else:
            return df[(df['Session']==Session) & (df['Patient Id']==patientID)]


    #given a dataframe, specified corpus, preferred eval/train return unique patient/session pairs
    def getData(self,corpus,df,train='train'):
        df = pd.read_csv(self.topEntity)
        tmp = df[df['Eval_Train'] == self.trainEval[corpus][train]]
        patientID = list(zip(tmp['Patient Id'],tmp['Session']))
        return patientID
    
        

    #return the patient/session pair containing the list of artifacts
    def getArtifact(self,artifacts):
        df = pd.read_csv(self.topEntity)
        tmp = df[self.index['TUAR']].dropna()
        rows = tmp.index.tolist()
        tmp = df.iloc[rows,:]
        for arti in artifacts:
            index = tmp[self.index['TUAR']].str.contains(arti)
            tmp = tmp[index]
        
        patientID = list(zip(tmp['Patient Id'],tmp['Session']))
        return patientID
    
    

if __name__ == '__main__':
    q = Query()
    testList = ['TUAB','TUEP']
    testLabels = ['normal','no_epilepsy']
    patientList = q.getIntersect(testList,testLabels)
    #print(patientList)
    df = pd.read_csv('topEntity.csv')
    
    # artifacts = ['eyem','elec']
    # tmp = q.getArtifact(artifacts)
    # train = q.getData('TUAB',df)

    patientInfo = q.getPatient(patientList[0],full=False)
    print(patientInfo)

