#Predict your age!
import math
import json
import os
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
        list =[age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
        multlist=[x*x for x in list]
        addlist=sum(multlist)
        squareList=math.sqrt(addlist)
        devielist=squareList/2
        return math.floor(devielist)
#print(predict_age(65,60,75,55,60,63,64,45))

#return sum(a*a for a in age)**0.5//2
######### https://www.codewars.com/kata/5aff237c578a14752d0035ae/solutions/python #########

def new_line():
    print('\n')
#REVERSE WORD
def reverse_words(text):
        words =[]
        for word in text.split(' '):
            word_arr =list(word)
            word_arr.reverse()
            words.append(str(''.join(word_arr)))
        return ' '.join(words)
#print(reverse_words("hello bitch its me"))

#BEST SOLUTION
#return ' '.join(s[::-1] for s in str.split(' '))

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
def men_from_boys(arr):
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
