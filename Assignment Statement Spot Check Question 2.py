#Alexander ALlan
#23/09/2014
#Assignment Astatemtn Spot Check Question 2

WeightOfItem = int(input("Please enter the weight you have: "))
#Here I am asking for the aweight he is asking me ot calculate for.

OneHundredGs = (WeightOfItem // 100)
Remainder = (WeightOfItem % 100)
#Here I am working out how many 100g weights can go into his weight.

FiftyGs = (Remainder // 50)
Remainder = (Remainder % 50)
#Here I am working out how many 50g weights can go into his weight.

TenGs = (Remainder // 10)
Remainder = (Remainder % 10)
#Here I am working out how many 10g weights can go into his weight.

FiveGs = (Remainder // 5)
Remainder = (Remainder % 5)
#Here I am working out how many 15g weights can go into his weight.

TwoGs = (Remainder // 2)
Remainder = (Remainder % 2)

OneGs = (Remainder)
#Here I am working out how many 1g weights can go into his weight.

print("In {0}g, you can have {1} 100g weight(s), {2} 50g weight(s), {3} 10g weight(s), {4} 5g weight(s), {5} 2g weight(s) and {6} 1g weight(s).".format(WeightOfItem,OneHundredGs,FiftyGs,TenGs,FiveGs,TwoGs,OneGs))
#Here I am telling the user the final calculation.
