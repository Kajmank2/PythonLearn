#Predict your age!
import math

def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
        list =[age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
        multlist=[x*x for x in list]
        addlist=sum(multlist)
        squareList=math.sqrt(addlist)
        devielist=squareList/2
        return math.floor(devielist)
print(predict_age(65,60,75,55,60,63,64,45))

#return sum(a*a for a in age)**0.5//2
######### https://www.codewars.com/kata/5aff237c578a14752d0035ae/solutions/python #########