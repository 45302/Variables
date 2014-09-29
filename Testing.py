#task 5.1
#Alexander Allan
#21/09/2014
#Homework data testing

Age = int(input("Please enter your age: "))
if Age >= 50:
    print("You are able to vote.")
else:
    print("You are not currently old enough to vote, sorry.")
Retirement_Years_Left = (65 - Age)
print("You have another {0} year(s) until you can vote.".format(Retirement_Years_Left))
