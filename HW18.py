#Walter Stepanek
#Home Work 18

'''
    1.
    Data are presented in an excel file here.
    There are two workbooks in this excel file, one is 'task1' the other one is task2'.
    Imagine you are asked to present these data in a poster (at lest 600 dpi for each figure).
    Use both the line chart and the bar chart to plot these data properly.
    The font of labels, legends, axis ticks, etc, embedded in the figure must be readable.
    The line width must be adjusted to a proper thickness.
'''
#Data import
import pandas as pd
df1 = pd.read_excel('data_tasks.xlsx',sheet_name='task1')
df2 = pd.read_excel('data_tasks.xlsx',sheet_name='task2')
#Data manipulation
dfLV = df2.iloc[:, 1:3]   #Las Vegas
dfLV.to_csv('manip.csv', header=False, index=False)
dfLV = pd.read_csv('manip.csv')
dfDGO = df2.iloc[:, 3:5]  #Durango
dfDGO.to_csv('manip.csv', header=False, index=False)
dfDGO = pd.read_csv('manip.csv')
dfDEN = df2.iloc[:, 5:7]  #Denver
dfDEN.to_csv('manip.csv', header=False, index=False)
dfDEN = pd.read_csv('manip.csv')

#Calculate C.I. for data **Assuming normalized data
def calcCI(df):
    upperCI =df['Temperature (C)']+2*df['Standard Deviation']
    lowerCI =df['Temperature (C)']-2*df['Standard Deviation']
    df = df.assign(Lower95CI=lowerCI,
              Upper95CI=upperCI)
    return df

df1 = calcCI(df1)
dfLV = calcCI(dfLV)
dfDGO = calcCI(dfDGO)
dfDEN = calcCI(dfDEN)

#Print Data Frames
print('Task 1', df1)
print('Las Vegas', dfLV)
print('Durango', dfDGO)
print('Denver', dfDEN)

#Plotting
#Task 1
import matplotlib.pyplot as plt
import numpy as np
#Line Plot
plt.errorbar(df1.iloc[:,0],df1.iloc[:,1],yerr=(df1['Upper95CI']-df1['Lower95CI'])/2, linewidth=1, capsize=5, c = 'black')
plt.plot(df1.iloc[:,0], df1.iloc[:,1], linewidth=5)
plt.title('Task 1', fontsize=24)
plt.xlabel('Time - Line', fontsize=14, fontweight = 'bold')
plt.ylabel('Temperature (C)', fontsize=14, fontweight = 'bold')
plt.legend(['Temperature', '95% Confidence Interval'], loc = 'upper right')
plt.savefig('Task1Line.png', dpi=600)
plt.show()

#Bar Plot
tempBar = list(df1.iloc[:,1])
errBar = list((df1['Upper95CI']-df1['Lower95CI'])/2)
r1 = np.arange(len(list(df1.iloc[:,0])))
r1 += 1
plt.bar(r1, tempBar, label = 'Temperature', yerr=errBar, capsize = 10) 
plt.title('Task 1 - Bar', fontsize = 24)
plt.xlabel(df1.columns[0], fontweight = 'bold')
plt.ylabel('Temperature (C)', fontweight = 'bold')
plt.legend(['Temperature', 'Standard Deviation'], loc = 'upper right')
plt.savefig('Task1Bar.png', dpi=600)
plt.show()

#Task 2
#Line Plot
xRange = dfLV.index + 1
plt.plot(xRange, dfLV.iloc[:,0], linewidth=3, c = 'red')
plt.errorbar(xRange, dfLV.iloc[:,0], yerr=(dfLV['Upper95CI']-dfLV['Lower95CI'])/2, linewidth=1, color='red', capsize=5)
plt.plot(xRange, dfDGO.iloc[:,0], linewidth=3, c = 'black')
plt.errorbar(xRange, dfDGO.iloc[:,0], yerr=(dfDGO['Upper95CI']-dfDGO['Lower95CI'])/2, linewidth=1, color='black', capsize=5)
plt.plot(xRange, dfDEN.iloc[:,0], linewidth=3, c = 'lightblue')
plt.errorbar(xRange, dfDEN.iloc[:,0], yerr=(dfDEN['Upper95CI']-dfDEN['Lower95CI'])/2, linewidth=1, color='lightblue', capsize=5)
plt.xlabel('Time Point (Hour)', fontsize =  14, fontweight = 'bold')
plt.ylabel('Temperature (C)', fontsize = 14, fontweight = 'bold')
plt.title('Task 2 - Line', fontsize = 24)
plt.legend(['Las Vegas', 'Durango', 'Denver'], loc = 'upper right')
plt.savefig('Task2Line.png', dpi=600)
plt.show()

#Bar Plot
barWidth=0.25
r1 = xRange
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
plt.bar(r1, dfLV.iloc[:,0], width=barWidth, yerr=(dfLV['Upper95CI']-dfLV['Lower95CI'])/2, label= 'Las Vegas', capsize=5)
plt.bar(r2, dfDGO.iloc[:,0], width=barWidth, yerr=(dfDGO['Upper95CI']-dfDGO['Lower95CI'])/2, label='Durango', capsize=5)
plt.bar(r3, dfDEN.iloc[:,0], width=barWidth, yerr=(dfDEN['Upper95CI']-dfDEN['Lower95CI'])/2, label='Denver', capsize=5)
plt.xlabel('Time Point (Hour)', fontsize=14, fontweight = 'bold')
plt.xticks([r+barWidth for r in r1], [1,2,3,4,5,6])
plt.ylabel('Temperature (C)', fontsize=14, fontweight = 'bold')
plt.title('Task 2 - Bar', fontsize=24)
plt.legend(['Las Vegas', 'Durango', 'Denver'])
plt.savefig('Task2Bar.png', dpi=600)
plt.show()
