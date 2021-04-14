def new_line():
    print('\n')
#Most digits
def find_longest(arr):
    return max(arr, key=lambda x: len(str(x)))
print(find_longest([1,400,20,401,11]))
#MEETING
s="Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"
def meeting(s):
    return "".join(sorted(["({}, {})".format(i[1].upper(),i[0].upper())for i in [n.split(":") for n in s.split(";")]]))
print(meeting(s))

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
print(title_case(title,minor))

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
print(order("is2 Thi1s T4est 3a"))

