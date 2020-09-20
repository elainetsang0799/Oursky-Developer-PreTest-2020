#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 17:19:26 2020

@author: lingg
"""
import time
import numpy as np

capacity = 3 #set capacity of the cache as 3
keylist = [] #list of data
lastaccessT = [] #access time
score = [] #score
compareS = [0] #compare of the score

def put(key, value, weight): #save the data
    Time = lastaccessT.append(time.time()) #save time with correct order
    mark = weight // -1 #calculate the score
    save = score.append(mark) #save marks with correct order
    if len(keylist) >= capacity: #if capacity is full
        compareS[0] = mark #save the new mark as the compare score
        for i in range(0,capacity -1): #check all the key
            if score[i] > compareS[0]:
                compareS[0] = score[i] #change the target of lowest score
                score.pop(i) #remove the score and access time of the key
                lastaccessT.pop(i)
                keylist[i] = [key, value, weight] #remove the lowest score key to the higher score key
    else:
        keyoflist = keylist.append([key, value, weight]) #add the key
                
    
def get(key):
    for i in range(0,len(keylist),1):
            if key == keylist[i][0]: #check the key is inside key list
                score[i] = (keylist[i][2]/(np.log(time.time() - lastaccessT[i])))*100#score = weight / ln(current_time - last_access_time)
                lastaccessT[i] = time.time() #save time with correct order
                return keylist[i]
            #else:return -1
    return -1