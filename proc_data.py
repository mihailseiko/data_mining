#!/usr/bin/env python3
import pandas as pd
import numpy as np
import csv
import sys

infile="~/Documents/kaggle/train3.csv"
#outfile="~/Documents/kaggle/proc_train.csv"

def main():
    fp = pd.read_csv(infile)
    data = fp.ix[:,:].fillna("NA")
    dataT = data.values.tolist()
    
    current_id = 1
    count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    summ = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    current_arr = np.zeros(23)

#    for x in range(2,5):
#        print(x)

   
    for instance in dataT:
        for i in range(0,23):
            if str(instance[i]) != "NA":
                count[i] += 1
                summ[i] += instance[i]


    for i in range(0,23):
        if count[i] != 0:
            summ[i] /= count[i]
    
    for instance in dataT:
        for i in range(0,23):
            if (str(instance[i]) == "NA"):
                instance[i] = summ[i]    

    #print(str(instance[6]).isdigit())
    #print(dataT)
  
    for instance in dataT:
    	print(instance)
	print("\n")
   	   
    # dataout = []
    #current_arr = np.zeros(23)
    #for instance in dataT:
    #print(instance[0])



'''

        current_len += 1
        attr = np.array(row[1:])
        if int(row[0]) == current_id:
            current_arr = current_arr + attr
        else: # next id
            current_arr /= (current_len-1)
            current_arr = np.append(np.array([current_id]), current_arr)
            dataout.append(list(current_arr))
            current_id = row[0]
            current_len = 1
            current_arr = attr
    current_arr /= current_len
    current_arr = np.append(np.array([current_id]) ,current_arr)
    dataout.append(list(current_arr))
    current_id = row[0]
    current_len = 1
    current_arr = attr
    #print(fp.columns.tolist())
    #exit()
    dataout = dataout[::-1]
    dataout.append(fp.columns.tolist())
    dataout = dataout[::-1]
    print(dataout)
    for row in dataout:
        print(row)
    with open('output.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(dataout)

'''

if __name__ == "__main__":
    main()
