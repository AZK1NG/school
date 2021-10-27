
## 1 ##
# name = input("enter your name: ")
#print("Hello " , name)
## 1 ##

## 4 ##
# width = 17
# height = 12.0
# print (width // 2)
# print(width / 2.0)
# print(height / 3)
## 4 ##

## 5 ##
# celsius = float(input("Enter temperature in celsius: "))
# fahrenheit = 1.8 * celsius + 32
# print("the new teperature" , fahrenheit)
## 5 ##





# num1 = float(input("Enter your first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter your second number: "))

# if op == "+":
#    print(num1 + num2)
# elif op == "-":
#    print(num1 - num2)
# elif op == "/":
#    print(num1 / num2)
# elif op == "*":
#    print(num1 * num2)
# else:
#    print("Invalid operator")




# monthConversions = {
#    "Jan": "January",
#    "Feb": "February",
#    "Mar": "March",
#    "Apr": "April",
#    "May": "May",
#    "Jun": "June",
#    "Jul": "July",
#    "Aug": "August",
#    "Sep": "Sepptember",
#    "Oct": "October",
#    "Nov": "November",
#    "Dec": "December",
#}

##print(monthConversions["Dec"])
# print(monthConversions.get("Dec", "Not a valid key"))



#i = 1
#while i <= 10:
#    print (i)
#    i = i + 1

# print("done with loop")


#from types import TracebackType


#secretword = "dog" 
#guess = ""
#guesscount = 0
#guesslimit = 3
#outofguesses = False

#while guess != secretword and not (outofguesses):
#    if guesscount < guesslimit:
#        guess = input("enter guess: ")
#        guesscount += 1   
#    else:
#        outofguesses = True

#if outofguesses:
#    print ("out of guesses, you lose!")
#else:
#    print ("you win!")



#for letter in "northshore":
#    print(letter)




#friends = [ "karen", "jim", "kevin"]
#for name in friends:
#    print(name)




#for i in range(3, 10):
#    print (i)



#def rtp(basenum, pownum):
#    result = 1
#    for i in range(pownum):
#        result = result * basenum
#    return result
#
#print(rtp (3, 3))




#numbergrid = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9],
#    [0]
#]
#
#for row in numbergrid:
#    for col in row:
#        print(col)







# def translate(phrase):
#    translation = ""
#    for letter in phrase:
#        if letter.lower() in "aeiou":
#            if letter.isupper():
#                translation = translation + "K"
#            else:
#                translation = translation + "k"
           
#          else:
#            translation = translation + letter
#    return translation


# print(translate(input("enter a phrase: ")))

# ]



# try:
#     answer = 10/0
#     number = int(input("enter a number: "))
#     print(number)

# except ZeroDivisionError:
#     print("divided by zero ")
# except ValueError:
#     print("invalid input")




##########################################################

###r is the rate of which you work
###h is the hours worked 

#h = int(input( "enter the numer hours you work up to 40: "))
#r = int(input( "enter the rate of which you work: "))
#p = (h * r)
#otr = 1.5
#oth = int(input( "enter the amount of hours you worked 40 hours: "))
#otp = otr = 1.5

###this tells you if you went over the max 
#if (h > 41):
#    print("your rate is " , h)


#############################################################







######3.1
#h = 0 
#r = 0
#p = 0
#ot = 0
#h =float(input("enter hours worked: "))
#r =float(input("enter pay rate: "))
#if (h>40):
#    ot = h - 40
#    p = 40 * r + ot * 15
#else:
#    print("hours is it 40")
#print("Pay: " , p )





#######3.2
#gracefulness = "Error, please enter numeric input  "

#hours = input('Enter Hours: ')
#try:
#  float(hours)>=0
#except:
#  print (gracefulness)
#  hours = input('Enter Hours: ')

#rate = input('Enter Rate: ')
#try:
##  float(rate) >=0
#except:
#  print (gracefulness)
#  rate = input('Enter Rate: ')

#hours = float(hours)
#rate = float(rate)

#if hours > 40:
#  extra_time = hours - 40
#else:
#  extra_time = 0

#extra_pay = 0.5 * rate * extra_time
#pay = hours * rate + extra_pay
#print ('Pay: '),
#print (pay)

#######




#i =  2
#while i <= 10000:
#    print(i)
#    i += 1
#
#print("done")







#def hw():
#    print("hello world")
#    print("Coach O is a millionaire ")
#    return(1)
#a = hw()
#print("hey this is right")
#hw()
#print(a)







#name1 = input("enter your first : ")
#name2 =input("enter your last : ")
#
#def name(name1 , name2):
#    print("your name is ")  , name1 , name2
#
#    return
#name(name1 , name2)





