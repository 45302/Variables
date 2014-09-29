#Alexander Allan
#23/09/2014
#Assignment Statement Spot Check

Width = float(input("Please enter the width of the pool: "))
Length = float(input("Please enter the length of the pool: "))
Depth = float(input("Please enter the depth of the pool: "))
#Here is me asking for specific information about the pool.

MainSectionVolume = (Length * Width * Depth)
CircleRadius = (Width / 2)
CircleVolume = (3.14 * CircleRadius**2)
HalfCircleVolume = ((CircleVolume / 2) * Depth)
PoolVolume = (MainSectionVolume + HalfCircleVolume)
#Here I have just calculated the total volume of the pool.

print("The volume of the swimming pool you have is {0} metres squared.".format(round(PoolVolume,2)))
#Here I am telling the user the volume of the pool.
