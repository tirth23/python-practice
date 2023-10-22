inventory = open(r"C:\Users\Tirth Patel\Documents\PythonPractice\Basic\readfl.py", 'r')
eof = False
while eof == False:
    line = inventory.readline()
    if line != '':                          #'' means null
        if line != "\n":          
            print(line, end="")             #else is not written bcoz blank line i.e., \n(new line) not needed to print
    else:
        print("\nEnd of file", end="")

        eof = True


inventory.close()