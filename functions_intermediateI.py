#write a randInt function
import random
def randInt(min='', max=''):
    if min>max or max<0 or min<0:
        return False
    if min =='' and max == '':
        num = round(random.random() * 100)
    elif min=='':
        num = round(random.random() * max)
    elif max =='':
        num = round(random.random() *(100-min) + min)
    else: 
        num = round(random.random() *(max-min) +min) 
    return num

print(randInt(min=15, max=28))

# import random
# def randInteger(min='', max=''):
#     num = random.random() *100
#     return num 
# print(randInt()) 		    # should print a random integer between 0 to 100
# print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500

