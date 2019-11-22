from random import randint, uniform
print(randint(1, 6))
print(uniform(1, 6))

print( "y" in "Python" )
print( "x" in "Python" )
print( "p" in "Python" )
print( "th" in "Python" )
print( "to" in "Python" )
print( "y" not in "Python" )

x = 1
y = 0
print( ( x == 0) or ( y == 0) or ( x / y == 1) )
x = "ik ben arthur"
if "i" in x:
    print("het werkt")
else:
    print("het werkt niet")
