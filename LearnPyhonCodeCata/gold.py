import re
from string import digits


def new_line():
    print('\n')
#Most digits
def find_longest(arr):
    return max(arr, key=lambda x: len(str(x)))
#print(find_longest([1,400,20,401,11]))
#MEETING
s="Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"
def meeting(s):
    return "".join(sorted(["({}, {})".format(i[1].upper(),i[0].upper())for i in [n.split(":") for n in s.split(";")]]))
#print(meeting(s))

#Title Case
#my soltuion
title='ab'
minor='ab'
def title_case(title, minor_words=''):

    if len(title)>2:
        finish_s = ''
        title_to_words = title.split(' ')
        minor_s = ''
        minor_to_words = minor_words.split()
        for y in minor_to_words:
            minor_s+=y.lower() + ' '
            minor_s.upper()
        for x in title_to_words:
            finish_s += x.capitalize() + ' '
        for xy in minor_s.lower().split(" "):
            if title.lower().find(xy) == -1:
                continue
            else:
                asd=xy
                asd_c=asd.capitalize()
                finish_s=finish_s.replace(asd_c,asd)

        finish_s = finish_s[:-1]
        finish_s = finish_s[0].upper() + finish_s[1:]
        return finish_s
    else:
        return title
# The best solution
'''
def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])
'''
#print(title_case(title,minor))

#Your order, please
#MY SOLUTION
def order(sentence):
    numb=[1,2,3,4,5,6,7,8,9,0]
    bejrut = sentence.split(" ")
    sum=""
    sum3=""
    for x in bejrut:
        for y in numb:
            if x.find(str(y)) == -1:
                print("no there")
            else:
                sum += str(y)+x+" "
    asd=sum.split(" ")
    del asd[-1]
    sum2 = sorted(asd, key= lambda x:x[::1])
    for z in sum2:
        sum3+=z[1:]+" "
    return sum3[:-1]
# BEST ->> def order(sentence):
#     return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))
#print(order("is2 Thi1s T4est 3a"))


#a -> 1
#e -> 2
#i -> 3
#o -> 4
#u -> 5

def encode(st):
    sts=""
    for x in st:
        for y in x:
            if y=='a':
                sts+='1'
            elif y=='e':
                sts+='2'
            elif y=='i':
                sts+='3'
            elif y=='o':
                sts+='4'
            elif y=='u':
                sts+='5'
            else:
                sts+=y

    return sts

#Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern
def decode(st):
    sts = ""
    for x in st:
        for y in x:
            if y == '1':
                sts += 'a'
            elif y == '2':
                sts += 'e'
            elif y == '3':
                sts += 'i'
            elif y == '4':
                sts += 'o'
            elif y == '5':
                sts += 'u'
            else:
                sts += y
    return sts
#BEST SOLUTION
#def encode(s, t=str.maketrans("aeiou", "12345")):
#    return s.translate(t)

#def decode(s, t=str.maketrans("12345", "aeiou")):
#    return s.translate(t)
#print(encode('arek'))
#print(decode('1r2k'))

#Modify the kebabize function so that it converts a camel case string into a kebab case.
def kebabize(string):
    list=re.findall('.[^A-Z]*',string)
    ss=""
    for x in list:
        ss+=x+'-'
    remove_digits = str.maketrans('', '', digits)
    return ss[:-1].lower().translate(remove_digits)
print(kebabize('myCamelCasedString'))

#Best SOLUTION
''''
def kebabize(s):
    return ''.join(c if c.islower() else '-' + c.lower() for c in s if c.isalpha()).strip('-')
'''''
#Round by 0.5 steps
def solution(n):
    def truncate(n,decimals=0):
        multiplier = 10 ** decimals
        return int(n*multiplier)/multiplier
    return truncate(n)
print(solution(4.25))