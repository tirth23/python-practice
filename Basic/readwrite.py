f=open(r"Basic\readwrite.py","r+")
print(f.read())
f.write("print('1')")
x=f.readline()
if (x==""):
    print("print('2')")
f.close()
