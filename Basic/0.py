print([[(x, y) for x in range(4)] for y in range(5)])
print([(x, y) for x in range(4) for y in range(5)])
print([[None for j in range(3)] for i in range(2)])
print([[0 for j in range(3)]*2])
print([2]*3)
colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [(x,y) for x in colours for y in things ]
print(coloured_things)
l = [None]
l[0] = 5
b = "Hello, World!"
print(b[5:2:-1])
print([print(x, y) for x in range(5) for y in range(5)])
#first inner print will be executed then outer print so at that time none will be printed
l = [print("a")]
print(l)