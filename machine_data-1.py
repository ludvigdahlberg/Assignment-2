#%%

import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt


'''
Submit your solutions in pdf format, with code and plots supporting your answers.
machine_data contains raw data of a part from 3 manufactures A, B, C
The system is run to failure under load
The load and the operation time is provided in each row

What is the range of load and time during operation for each manufacturer?
What is the most expected load value?
How are the load and time related?
Which distribution best describes the load?
Which distribution best describes the time?

Which manufacturer has the best performance and why?

'''
#%%
# read the data file into a dataframe
df = pd.read_csv('machine_data.csv')
df = df.drop(columns=['Unnamed: 0'],errors='ignore')
print(df)

print(df.shape)

#%% 
"""
Drop the index
"""

#%%
"""
Extract data for a given manufacturer
"""
df['manufacturef'] = df['manufacturef'].str.upper()
grpByManu = df.groupby('manufacturef')

dfa = grpByManu.get_group('A')
dfb = grpByManu.get_group('B')
dfc = grpByManu.get_group('C')

#%%

loada = dfa['load']
timea = dfa['time']

def print_range(d, name):
    print(f"\n{name}")
    print("Load range:", d['load'].min(), "-", d['load'].max())
    print("Time range:", d['time'].min(), "-", d['time'].max())
print_range(dfa, "A")
print_range(dfb, "B")
print_range(dfc, "C")


#%%
'''
Is there a relationship between load and time
'''
plt.scatter(dfa['load'], dfa['time'])
plt.title("Relation between load and time for (A)")
plt.xlabel("Load")
plt.ylabel("Time")
plt.show()

plt.scatter(dfb['load'], dfb['time'])
plt.title("Relation between load and time for (B)")
plt.xlabel("Load")
plt.ylabel("Time")
plt.show()

plt.scatter(dfc['load'], dfc['time'])
plt.title("Relation between load and time for (C)")
plt.xlabel("Load")
plt.ylabel("Time")
plt.show()
#%%
'''
Characteristics of data
mean, median, mode
'''
print("Mean load (A):",dfa['load'].mean())
print("Mean load (B):",dfb['load'].mean())
print("Mean load (C):",dfc['load'].mean())

print("Median load (A):",dfa['load'].median())
print("Median load (B):",dfb['load'].median())
print("Median load (C):",dfc['load'].median())

print("Mode load (A):",dfa['load'].mode())
print("Mode load (B):",dfb['load'].mode())
print("Mode load (C):",dfc['load'].mode())
#%%
'''
How is load distributed
Why does it matter
uniform, normal, exponential, weibull
'''
for name, d in [('A', dfa), ('B', dfb), ('C', dfc)]:
    d['load'].plot(kind='hist', bins=10)
    plt.title(f"Load distribution ({name})")
    plt.xlabel("Load")
    plt.show()

    d['time'].plot(kind='hist', bins=10)
    plt.title(f"Time distribution ({name})")
    plt.xlabel("Time")
    plt.show()

#%%
'''
variance, standard deviation
What is the meaning of 6sigma
'''
def variability(d, name):
    print(f"\n{name}")
    print("Load std:", d['load'].std())
    print("Time std:", d['time'].std())

variability(dfa, "A")
variability(dfb, "B")
variability(dfc, "C")


#%%
'''
Other plots that can be useful 
boxplot
'''
df.boxplot(column='time', by='manufacturef')
plt.title("Time distribution by manufacturer")
plt.suptitle("")
plt.ylabel("Time")
plt.show()

df.boxplot(column='load', by='manufacturef')
plt.title("Load distribution by manufacturer")
plt.suptitle("")
plt.ylabel("Load")
plt.show()



def summarize(d, name):
    print(f"\n--- {name} ---")
    print("Load mean:", d['load'].mean())
    print("Load median:", d['load'].median())
    print("Load std:", d['load'].std())
    print("Time mean:", d['time'].mean())
    print("Time median:", d['time'].median())
    print("Time std:", d['time'].std())

summarize(dfa, "A")
summarize(dfb, "B")
summarize(dfc, "C")

    
# %%
