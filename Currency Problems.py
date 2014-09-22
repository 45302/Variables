#Alexander Allan
#22/09/2014
#Currency problems

Value = int(input("Please enter the amount of money: £"))

Twenties = Value // 20
Remainder = Value % 20

Tens = Remainder // 10
Remainder = Tens % 10

Fives = Remainder // 5
Remainder = Fives % 5

Twos = Remainder // 2
Remainder = Twos % 2

Ones = Remainder // 1

print("In £{0}, you have {1} £20 note(s), {2} £10 note(s), {3} £5 note(s), {4} £2 coin(s) and {5} £1 coin(s).".format(Value,Twenties,Tens,Fives,Twos,Ones))
