#Predict your age!
import math
import json
import os
from collections import Counter
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8): # MY
        list =[age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
        multlist=[x*x for x in list]
        addlist=sum(multlist)
        squareList=math.sqrt(addlist)
        devielist=squareList/2
        return math.floor(devielist)
#print(predict_age(65,60,75,55,60,63,64,45))

#return sum(a*a for a in age)**0.5//2  # BEST
######### https://www.codewars.com/kata/5aff237c578a14752d0035ae/solutions/python #########

def new_line():
    print('\n')
#REVERSE WORD
def reverse_words(text): #MY
        words =[]
        for word in text.split(' '):
            word_arr =list(word)
            word_arr.reverse()
            words.append(str(''.join(word_arr)))
        return ' '.join(words)
#print(reverse_words("hello bitch its me"))
#return ' '.join(s[::-1] for s in str.split(' '))  #BEST

#BASIC PING
""""
hostname="192.168.8.1"
response=os.system("ping "+ hostname)

if response == 0:
    print("its up !")
else:
    print("its down")
    """
new_line()

#Sort Out The Men From Boys

                #My solution
arr=[20,33,50,34,43,46]
def men_from_boys(arr): # MY
    sort=[]
    sort2=[]
    for x in (arr):
        if  x % 2 == 0:
            sort.append(x)
            sort.sort()
        else:
            sort2.append(x)
            sort2.sort(reverse=True)
    arr=sort+sort2
    arr=list(dict.fromkeys(arr))
    return arr
        #best soultion
''''
def men_from_boys(arr):
    men = []
    boys = []
    for i in sorted(set(arr)):
        if i % 2 == 0:
            men.append(i)
        else:
            boys.append(i)
    return men + boys[::-1]
'''
new_line()
#sum of minimums !
def sum_of_minimums(numbers):
    return sum(map(min,numbers))
print(sum_of_minimums([[67,89,90,56], [11,12,14,54],[7,9,4,3], [9,8,6,7]]))

#Counting Array Elements
def count(array): # MY
    con=1
    diciton={}
    for x in array:
        if x in diciton:
            diciton[x]+=1
        else:
            diciton[x]=con
    return diciton
#def count(array): #BEST !
#    return Counter(array)
print(count(['a', 'a', 'b', 'b', 'b','c']))

new_line()
#Sorted? yes? no? how?
arr=[15, 7, 3, -8]
def is_sorted_and_how(arr): #my soloution
    asc=[]
    dsc=[]
    for x in arr:
        asc.append(x)
    for x in arr:
        dsc.append(x)
    dsc.sort(reverse=True)
    asc.sort()
    if asc==arr:
        return 'yes, ascending'
    elif dsc==arr:
        return 'yes, descending'
    else:
        return 'no'
    '''
    if arr == sorted(arr):# BEST
        return 'yes, ascending'
    elif arr == sorted(arr)[::-1]:
        return 'yes, descending'
    else:
        return 'no'
        '''

