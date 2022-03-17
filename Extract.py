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


pathTUSZ = '/scr/shared/TUH_SEIZURE/edf'      #Seizure Corpus
pathTUAR = "/scr/shared/TUH_ARTIFACTS_v2"     #Artifact Corpus
pathTUEP = '/scr/shared/TUH_EPILEPSY/edf'     #Epilepsy Corpus
pathTUAB = '/shared/TUH/tuh_eeg_abnormal/v2.0.0/edf' #Abonormal Corpus
pathTUSL = '/scr/shared/TUH_SLOWING/edf'    #slowing corpus
pathTUE = '/scr/shared/TUH_EVENTS/edf' #events corpus


def getUniqueArtifact(file_path):
    header_list = ['id','channel','start time','end time', 'artifact', 'count']
    sec_Rec = pd.read_csv(file_path,skiprows=6,names=header_list)
    artifacts = set(sec_Rec['artifact'].tolist())
    return artifacts

def cleanCSV(file_path,id_pair):
    header_list = ['id','channel','start time','end time', 'artifact', 'count']
    sec_Rec = pd.read_csv(file_path,skiprows=6,names=header_list)
    
    sec_Rec['Patient ID'] = id_pair[0]
    sec_Rec['Session'] = id_pair[1]
    sec_Rec['File Path'] = file_path
    return sec_Rec



TUSZ_Data = []
fields = ['Patient Id','Session','Epilepsy','Channel Type','Date','File Path']
for parth in Path(pathTUSL).rglob('*.txt'):
    #print(parth)
    patid = []
    labels = str(parth).split('/')
    print(labels)
    print(labels)
    train = labels[5]
    channel_type = labels[6]
    tmp = tuple(labels[-1].split('_'))
    patid.append(tmp[0])
    patid.append(tmp[1].split('.')[0])
    patid.append(channel_type)
    patid.append(Ep_notEp)
    t = labels[-2].split('_')
    date = t[1]+'_'+t[2]+'_'+t[3]
    patid.append(date)
    patid.append(str(parth))
    TUSZ_Data.append(tmp)
print(len(TUSZ_Data))
t = list(set(TUSZ_Data))
print(len(t))
tuep_df = pd.DataFrame(TUEP_Data,columns=fields)
tuep_df.to_csv('TUEP_CSV.csv',index=False)

df = pd.read_csv('TUEP.csv')
top_entity = pd.read_csv('TopEntity.csv')
count = (top_entity['TUEP_Epilepsy'] != '').sum()
print(count)
print((top_entity['TUEP_Epilepsy'].dropna()))
error = 0
for index,ps in df.iterrows():
    
     patientID = ps['Patient Id']
     sessionID = ps['Session']
     Eplipsy = ps['Epilepsy']
     Channel = ps['Channel Type']
     Date = ps['Date']
     print(patientID,sessionID,Eplipsy,Channel,Date)
     try:
        top_entity.loc[(top_entity['Session']==sessionID) & (top_entity['Patient Id']==patientID),'Date'] = Date
        top_entity.loc[(top_entity['Session']==sessionID) & (top_entity['Patient Id']==patientID),'TUEP_Epilepsy'] = Eplipsy
        top_entity.loc[(top_entity['Session']==sessionID) & (top_entity['Patient Id']==patientID),'Channel Configuration'] = Channel
     except KeyError:
        error +=1
print(error)


print(top_entity)
top_entity.to_csv('temp.csv',index=False)
