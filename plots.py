import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


all_paths = [
    '/home/aga/Desktop/EEG/Nagrania/Nagrania/ssvep_count/Agnieszka_03_06/unity_log.csv',
    '/home/aga/Desktop/EEG/Nagrania/Nagrania/ssvep_count/Rysiek_03_06/unity_log.csv',
    '/home/aga/Desktop/EEG/Nagrania/Nagrania/ssvep/ssvep/Ania_14_06_16/unity_log.csv',
    '/home/aga/Desktop/EEG/Nagrania/Nagrania/ssvep/ssvep/Blazej 13.06.16/unity_log.csv',
    '/home/aga/Desktop/EEG/Nagrania/Nagrania/ssvep/ssvep/Karen_14_06_16/unity_log.csv',
    '/home/aga/Desktop/EEG/Nagrania/Nagrania/ssvep/ssvep/Kuba_14_06_16/unity_log.csv'
    ]

   
   
def Get_Accuracy(path):
     #Calculates ssvep counting accuracy for a single subject     
    log = pd.read_csv(filepath_or_buffer = path, sep = ',', header = 0, names = ['time', 'trial', 'code', 'received', 'expected'], skiprows = 1)
    bool_array = log['code'] == 'responded'
    log.loc[bool_array]
    subset_of_log = log.loc[bool_array]
    accuracy = subset_of_log['received'] / subset_of_log['expected']
    return np.array(accuracy)
           
def Plot_Accuracies():
    plt.style.use('ggplot')
    all_accuracies = []
    fig, axes = plt.subplots(1)
    for single_path in all_paths:
        subject_accuracy = Get_Accuracy(single_path)
        all_accuracies.append(Zscore(subject_accuracy))
       # axes.hist(subject_accuracy, bins = 10, range = [0.3, 1.3], alpha = 0.5)
    flattenedArray = np.array(all_accuracies).flatten()               
    axes.hist(flattenedArray, bins = 10, range = [-2, 2], alpha = 0.5)
    flattenedAmp = np.array(ZscoreAmp(ZscoreAmp(saving)).flatten())
    axes.hist(flattenedAmp, bins = 10, range = [-2, 2], alpha = 0.5)
   
    all_accuracies
    fig2, axes2 = plt.subplots(1)
    axes2.boxplot( all_accuracies)
    axes2.set_title("celnosc")
    axes2.set_xticklabels(['Aga', 'Rysiek', 'Ania', 'Blazej', 'Karen', 'Kuba'])
    #plt.setp(axes, xticks=[y+1 for y in range(len(all_accuracies))], xticklabels=['Aga', 'Rysiek', 'Ania', 'Blazej', 'Karen', 'Kuba'])
   
def Zscore(subject_scores):    
    zscore = ((subject_scores - subject_scores.mean())/subject_scores.std())
    return np.array(zscore)

def ZscoreAmp(saving):
    #normalization of 'saving' (signal peaks)
    svalues =  np.array([(k,)+v for k,v in saving.items()], dtype=[('date', '|O4'), ('high', '<f8'), ('low', '<f8')])
    for subject_name, ssvep_values in saving.items():
        return ssvep_values
    zscoreAmp = ((svalues - svalues.mean())/svalues.std())   
    return np.array(zscoreAmp)
      
#korelacja wyników z sygnałem
