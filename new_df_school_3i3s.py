#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 10:53:39 2018

@author: buckz
"""

# chemin pour les différents fichiers

filev2 = 'New_file_school_313s.xls'
filev3 = 'frame_school_aerospace.xls'

# Ouverture des fichiers en tant que DF

df = pd.read_excel(filev2)
newdf = pd.read_excel(filev3, header=None) #Suppression des mauvaises colonnes
newdf = pd.read_excel(filev3, header=3) #Ajout des colonnes via 3e lignes
    
#fonction pour extraire les valeurs de chaques colonnes

#def extract_values(colname):
#    a = []
#    for i in df[colname] :
#        a.append(i)
#    return a

#Stockage des valeurs
    
#nom = extract_values('Nom')
#interlocuteur = extract_values('Interlocuteur')
#adresse = extract_values('Adresse')
#ville = extract_values('Ville')
#code = extract_values('Code')
#pays = extract_values('Pays')
#tel = extract_values('Telephone')
#mail = extract_values('Mail')
#web = extract_values('PageWeb')

#Renommer & r&organiser les colonnes 

newdf.columns = ['Logo', 'Nom', 'Interlocuteur', 'Adresse', 'Code', 'Ville', 'Pays',
       'Mail', 'Telephone']


dftest = newdf.append(df)
dfv4 = dftest
dfv4 = dfv4[['Logo', 'Nom','Interlocuteur','Adresse','Code','Ville','Pays','Mail','Telephone','PageWeb']]

#dfv4.to_excel('dfv4.xls')








    