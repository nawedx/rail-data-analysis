#Nawed Imroze
# coding: utf-8
import os
import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from pandas import ExcelWriter
import xlrd
from tkinter import * 

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

#For the year 2014-2015
df = pd.read_excel('OT-2014-15.xls')
df = df[['AU', 'EMPNAME', 'DESG', 'SUM(AMT)']]
df = (df[df['DESG']==("AC.COACH ATTD.")])
print(df)
sum_15 = df["SUM(AMT)"].sum()
pass_15 = 4294480
cost_pass15 = round(sum_15/pass_15, 2)
attd_no15 = df.count()['AU']
avg_OT15 = round(sum_15/attd_no15, 2)

#For the year 2015-2016
df = pd.read_excel('OT-2015-16.xls')
df = df[['AU', 'EMPNAME', 'DESG', 'SUM(AMT)']]
df = (df[df['DESG']==("AC.COACH ATTD.")])
print(df)
sum_16 = df["SUM(AMT)"].sum()
pass_16=4739961
cost_pass16 = round(sum_16/pass_16, 2)
attd_no16 = df.count()['AU']
avg_OT16 = round(sum_16/attd_no16, 2)

#For the year 2016-2017
df = pd.read_excel('OT-2016-17.xls')    
df = df[['AU', 'EMPNAME', 'DESG', 'SUM(AMT)']]
df = (df[df['DESG']==("AC.COACH ATTD.")])
print(df)
sum_17 = df["SUM(AMT)"].sum()
pass_17=5092085
cost_pass17 = round(sum_17/pass_17, 2)
attd_no17 = df.count()['AU']
avg_OT17 = round(sum_17/attd_no17, 2)

print("\n\nAnalysis for the year 2014-15\n")
print("The total OT claimed in 2014-15 is Rs.", sum_15)
print("The total number of passengers in 2014-15 is ", pass_15)
print("The Cost per passenger in 2014-15 is Rs.", cost_pass15)
print("The number of AC Coach Attendant who claimed OT = ", attd_no15)
print("Average OT claimed by AC Coach Attendant in 2014-15 is Rs. ", avg_OT15)

print("\n\nAnalysis for the year 2015-16\n")
print("The total OT claimed in 2015-16 is Rs.", sum_16)
print("The total number of passengers in 2015-16 is ", pass_16)
print("The Cost per passenger in 2015-16 is Rs.", cost_pass16)
print("The number of AC Coach Attendant who claimed OT = ", attd_no16)
print("Average OT claimed by AC Coach Attendant in 2015-16 is Rs. ", avg_OT16)

print("\n\nAnalysis for the year 2016-17\n")
print("The total OT claimed in 2016-17 is Rs.", sum_17)
print("The total number of passengers in 2016-17 is ", pass_17)
print("The Cost per passenger in 2016-17 is Rs.", cost_pass17)
print("The number of AC Coach Attendant who claimed OT = ", attd_no17)
print("Average OT claimed by AC Coach Attendant in 2016-17 is Rs. ", avg_OT17)

objects = ('2014-15', '2015-16', '2016-17')
x_pos = np.arange(len(objects))
costpass = [cost_pass15, cost_pass16, cost_pass17]
avgOT = [avg_OT15, avg_OT16, avg_OT17]

plt.bar(x_pos, costpass, align='center', alpha=0.5)
plt.xticks(x_pos, objects)
plt.ylabel('Cost per AC passenger')
plt.title('OT of AC Coach Attendant')
plt.show()

plt.plot(x_pos, costpass, '-o')
plt.xticks(x_pos, objects)
plt.text(0.9, 2.4, 'ECoR', fontdict=font)
plt.ylabel('Cost per AC passenger')
plt.title('OT of Coach Attendant')
plt.axis([-1, 3, 1, 3])
plt.show()

plt.plot(x_pos, avgOT, '-o')
plt.xticks(x_pos, objects)
plt.text(0.9, 2.4, 'ECoR', fontdict=font)
plt.ylabel('Average OT claimed')
plt.title('Average OT claimed by AC Coach Attendant over years')
plt.axis([-1, 3, 25000, 30000])
plt.show()

#import rail
