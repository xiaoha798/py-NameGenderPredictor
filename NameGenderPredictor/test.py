# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 09:22:10 2020

@author: Hadrien
"""

from NameGenderPredictor import predict_gender

while(True):
    name=input('Write a name: ')
    if name.lower()=='x':
        break
    else:
        p=predict_gender(name)
        print('Male probability is '+str(p))
        