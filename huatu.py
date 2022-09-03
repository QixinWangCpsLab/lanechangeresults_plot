import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns 
from pandas import DataFrame,Series
import statistics
from pylab import mpl

my_list1 = []
my_list2 = []
my_list3 = []
my_list4 = []
my_list5 = []
my_list6 = []
my_list7 = []
my_list8 = []
my_list9 = []
with open('our/sim0dot130/sim0to100_time_headways.m') as f:
    for line in f:
        if not line.startswith('%'):
            my_list1.append(line.strip("=").strip())
str1=','.join(my_list1)
# 字符串str转列表list1
list1 = str1.split(',')
# 列表list1转列表list2
list2 = []
for j in list1:
    list2.append(float(j))
# 列表list2转arr1
arr1 = np.array(list2)
with open('PerLC+/sim0dot130/sim0to100_time_headways.m') as f:
    for line in f:
        if not line.startswith('%'):
            my_list2.append(line.strip("=").strip())
str2=','.join(my_list2)
# 字符串str转列表list1
list11 = str2.split(',')
# 列表list1转列表list2
list22 = []
for j in list11:
    list22.append(float(j))
# 列表list2转arr1
arr2 = np.array(list22)
with open('ConLC+/sim0dot130/sim0to100_time_headways.m') as f:
    for line in f:
        if not line.startswith('%'):
            my_list3.append(line.strip("=").strip())
str3=','.join(my_list3)
# 字符串str转列表list1
list111 = str3.split(',')
list222 = []
for j in list111:
    list222.append(float(j))
arr3 = np.array(list222)


with open('our/sim0dot530/sim0to100_time_headways.m') as f:
    for line in f:
        if not line.startswith('%'):
            my_list4.append(line.strip("=").strip())
str4=','.join(my_list4)
# 字符串str转列表list1
List1 = str4.split(',')
# 列表list1转列表list2
List2 = []
for j in List1:
    List2.append(float(j))
# 列表list2转arr1
arr4 = np.array(List2)
with open('PerLC+/sim0dot530/sim0to100_time_headways.m') as f:
    for line in f:
        if not line.startswith('%'):
            my_list5.append(line.strip("=").strip())
str5=','.join(my_list5)
# 字符串str转列表list1
List11 = str5.split(',')
# 列表list1转列表list2
List22 = []
for j in List11:
    List22.append(float(j))
# 列表list2转arr1
arr5 = np.array(List22)
with open('ConLC+/sim0dot530/sim0to100_time_headways.m') as f:
    for line in f:
        if not line.startswith('%'):
            my_list6.append(line.strip("=").strip())
str6=','.join(my_list6)
# 字符串str转列表list1
List111 = str6.split(',')
List222 = []
for j in List111:
    List222.append(float(j))
arr6 = np.array(List222)


with open('our/sim0dot930/sim0to100_time_headways.m') as f:
    for line in f:
        if not line.startswith('%'):
            my_list7.append(line.strip("=").strip())
str7=','.join(my_list7)
# 字符串str转列表list1
LIst1 = str7.split(',')
# 列表list1转列表list2
LIst2 = []
for j in LIst1:
    LIst2.append(float(j))
# 列表list2转arr1
arr7 = np.array(LIst2)

with open('PerLC+/sim0dot930/sim0to100_time_headways.m') as f:
    for line in f:
        if not line.startswith('%'):
            my_list8.append(line.strip("=").strip())
str8=','.join(my_list8)
# 字符串str转列表list1
LIst11 = str8.split(',')
LIst22 = []
for j in LIst11:
    LIst22.append(float(j))
arr8 = np.array(LIst22)
with open('ConLC+/sim0dot930/sim0to100_time_headways.m') as f:
    for line in f:
        if not line.startswith('%'):
            my_list9.append(line.strip("=").strip())
str9=','.join(my_list9)
# 字符串str转列表list1
LIst111 = str9.split(',')
LIst222 = []
for j in LIst111:
    LIst222.append(float(j))
arr9 = np.array(LIst222)


#time headways
data_a = [arr1, arr4, arr7]
data_b = [arr2, arr5, arr8]
data_c = [arr3, arr6, arr9]

'''
# # #reset time costs
data_a = [arr1/100, arr4/100, arr7/100]
data_b = [arr2/100, arr5/100, arr8/100]
data_c = [arr3/100, arr6/100, arr9/100]
'''
'''
# # lanechanging time costs
data_a = [arr1/100, arr4/100, arr7/100]
data_b = [arr2/100, arr5/100, arr8/100]
data_c = [arr3/100, arr6/100, arr9/100]
'''

ticks = ['0.1', '0.5', '0.9']

#plt.figure()
plt.figure(figsize=(8,10))

bpr = plt.boxplot(data_a, positions=np.array(range(len(data_a)))*2.0-0.5, sym='.', widths=0.4,boxprops={'linewidth':8.0},capprops={'linewidth':8.0},medianprops={'linewidth':8.0},whiskerprops={'linewidth':8.0})
bpg = plt.boxplot(data_b, positions=np.array(range(len(data_b)))*2.0+0, sym='.', widths=0.4,boxprops={'linewidth':4.0},capprops={'linewidth':4.0},medianprops={'linewidth':4.0},whiskerprops={'linewidth':4.0})
bpb = plt.boxplot(data_c, positions=np.array(range(len(data_c)))*2.0+0.5, sym='.', widths=0.4,boxprops={'linewidth':1.0},capprops={'linewidth':1.0},medianprops={'linewidth':1.0},whiskerprops={'linewidth':1.0})


# draw temporary red and blue lines and use them to create a legend
plt.plot([], label='Our Proposed',linewidth=8.0, color='black')
plt.plot([], label='PerLC+',linewidth=4.0, color='black')
plt.plot([], label='ConLC+',linewidth=1.0, color='black')
plt.legend(loc = 2,fontsize='35')

#plt.legend()
plt.xticks(range(0, len(ticks)* 2 , 2), ticks)
plt.xlim(-2, len(ticks)*2)
plt.ylim(0, 250)
plt.xticks(fontsize=60)
plt.yticks(fontsize=60)
plt.tight_layout()

# plt.savefig('boxcompare.png')
# plt.title('Simulation Results for Performance Lane Changing Protocol: Lane Changing Success Rate and Time Costs (n=10)',fontsize=10)
# plt.ylabel("Lane Changing Time Costs/s") 
# plt.xlabel("Packet Loss Rate") # 我们设置横纵坐标的标题。
'''
plt.text(-0.5,500,'sr:100/100', horizontalalignment='center', size='x-large',  weight='heavy', fontsize='40',rotation='90') #380
plt.text(0,500,'sr:83/100', horizontalalignment='center', size='x-large',  weight='normal', fontsize='40',rotation='90') #350
plt.text(0.5,500,'sr:87/100', horizontalalignment='center', size='x-large',  weight='normal', fontsize='40',rotation='90') #620 514 350
plt.text(-0.5+2,810,'sr:100/100', horizontalalignment='center', size='x-large',  weight='heavy', fontsize='40',rotation='90') #700
plt.text(0+2,714,'sr:82/100', horizontalalignment='center', size='x-large',  weight='normal', fontsize='40',rotation='90') #514 # 
plt.text(0.5+2,714,'sr:85/100', horizontalalignment='center', size='x-large',  weight='normal', fontsize='40',rotation='90') # 514
plt.text(-0.5+4,820,'sr:89/100', horizontalalignment='center', size='x-large',  weight='heavy', fontsize='40',rotation='90') #710 720
plt.text(0+4,800,'sr:78/100', horizontalalignment='center', size='x-large',  weight='normal', fontsize='40',rotation='90') #750 
plt.text(0.5+4,800,'sr:82/100', horizontalalignment='center', size='x-large',  weight='normal', fontsize='40',rotation='90') #710 514
'''
plt.show()

