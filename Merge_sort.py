# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 15:39:41 2015

@author: chiarabiscaro
"""

def merge(list1, list2):
    """
    Merge two sorted lists.
    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    """   
    result = []
    idx1 = 0
    idx2 = 0
    
    while idx1 < len(list1) or idx2 < len(list2):
        if idx1 < len(list1) and idx2 < len(list2):
            if list1[idx1] <= list2[idx2]:
                result.append(list1[idx1])
                idx1 += 1
            else:
                result.append(list2[idx2])
                idx2 += 1
        elif idx1 < len(list1):
            result.append(list1[idx1])
            idx1 += 1
        elif idx2 < len(list2):
            result.append(list2[idx2])
            idx2 +=1
        
    return result
                
def merge_sort(list1):
    """
    Sort the elements of list1.
    Return a new sorted list with the same elements as list1.
    """
    if len(list1) <= 1:
        return list1
    
    left = list1[:len(list1)/2]
    right= list1[len(list1)/2:]
    
    left = merge_sort(left)
    right = merge_sort(right)                    
    
    return merge(left,right)
