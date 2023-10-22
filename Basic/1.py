a = 300
b = 400
if not a >= b:               #>= evaluated first
    print("yes")
else:
    print("no")

x = print("abc")
print(x)

a = 0
b = 0
if not a >= 0:
    print("yes")
else:
    print("no")


#and has more priority than or
#left to right associativity

'''3 or 4 and 0
3
>>> 4 and 0
0
>>> 4 and 0 or 3
3
>>> 0 and 4 or 3
3
>>> 4 and 0 and 3
0
>>> 0 and 4 and 3 or 5
5
>>> 3 or 5
3
>>> 5 or 3
5
>>> 3 and 5
5
>>> 5 and 3
3
>>> 0 and 3
0
>>> 3 and 0
0
>>> 0 and 4 or 9
9
>>> 4 or 3 and 0
4
>>> 4 and 0 or 4
4
>>> 4 and 0 or 3
3
>>> 0 and 4 or 0
0
>>> 0 and 4 or 3
3
>>> 4 or 3 or 2 and 0
4
>>> 4 and 3 and 2 or 3
2'''

'''def yo(y="t", h):    #default argument can not be before any non default arg
    print(y,h)'''

def yo1(y, h="t"):
    print(y,h)

yo1(a)

l=[1]
if l==[]:
    print("yes")