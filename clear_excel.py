#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 13:58:38 2018

@author: buckz
"""

import os
import pandas as pd

filev1 = 'File_school_3i3s.xls'
filev2 = 'df.xls'
filev3 = 'frame_school_aerospace.xls'
df = pd.read_excel(filev2)

newdf = pd.read_excel(filev3, header=3)

df.dropna(axis=0, how='all', inplace=True)
df.dropna(axis=1, how='all', inplace=True)

dfcol = df.columns
for col in dfcol:
    if 'Unnamed' in col:
        del df[col]


df.drop('Typedemessagerie', axis=1, inplace=True)
df.drop('Nomcompletdeladressedemessagerie', axis=1, inplace=True)
df.drop('Initiales', axis=1, inplace=True)
df.drop('Priorité', axis=1, inplace=True)

df.to_excel('New_file_school_313s.xls')