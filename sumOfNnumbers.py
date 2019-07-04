n = int( input( "How many numbers: " ) )

sum = 0.00
str = ""
list = []

for i in range( 0, n ):
    number = float( input( "Input number: " ) )
    list.append( number )
    sum += number

for j in list:
    print( f"{j} + ", end="" )

print( "\b\b = ", sum )
