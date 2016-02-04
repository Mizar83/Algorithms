# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 14:25:10 2015

@author: chiarabiscaro
"""
import numpy

def Partition(list1,l,r):
    """
    Partions the elements of list1 around a pivot, in this case
    the first element of the list. Modifies the list in place and returns
    index of pivot final position
    """
    p = list1[l]
    i = l + 1
    for j in range(l+1,r):
        if list1[j] < p:
            list1[j], list1[i] = list1[i], list1[j]
            i = i+1
    list1[l], list1[i-1] = list1[i-1], list1[l]
    return i-1
    
    
def ChoosePivotLast(list1,l,r):
    """
    chooses a pivot p from last element of list1 and 
    swaps the first element in the list with it
    """
    list1[l], list1[r-1] = list1[r-1], list1[l] 
    
    
def ChoosePivotMedian(list1,l,r):
    """
    chooses a pivot p from median of 3 element of list1 and 
    swaps the first element in the list with it
    """
    if r-l < 3:
        return
    
    if r-l % 2 == 0:
        median = (r-l)/2 - 1
    else:
        median = (r-l)/2
        
    if list1[l] > list1[median]:
        if list1[median] < list1[r-1]:
            list1[r-1],list1[l] = list1[l], list1[r-1]
        else:
            list1[median],list1[l] = list1[l],list1[median]
    elif list1[l] < list1[r-1]:
        if list1[median] > list1[r-1]:
            list1[r-1],list1[l] = list1[l],list1[r-1]
        else:
            list1[median],list1[l] = list1[l],list1[median]
    
def Quicksort(list1, l, r, t):
    """
    Sorts the elements of list1 in place, gives number of comparisons, comp
    l is the left index of the list (0) and r is the last one + 1 (len(list)).
    Type of pivot t: 1= first element, 2: last element, 3: median
    """    
    if r-l < 1 : 
        return 0
        
    if t == 2:
        ChoosePivotLast(list1,l,r)
    elif t == 3:
        ChoosePivotMedian(list1,l,r)
    
    comp = 0        
    i = Partition(list1,l,r)
    comp += (r - l) - 1         

    comp += Quicksort(list1,l,i,t)
    comp += Quicksort(list1,i+1,r,t)
        
    return comp
        
#test1 = [5,3,2,1,4]
#comp = Quicksort(test1, 0, len(test1),1)
#i = Partition(test1, 0, len(test1))
#print test1, comp
#test2=[8,9,10]
#ChoosePivotMedian(test2,0,len(test2))
#print test2

       
integer_file = open("Quicksort.txt", 'r')

int_array = []
for number in integer_file:
    int_array.append(int(number))
    
comp = Quicksort(int_array, 0, len(int_array), 3)
print comp
