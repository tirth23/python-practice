def hollowRhombus(rows): 
      
    for i in range (1, rows + 1): 
        # Print trailing spaces 
          
        for j in range (1, rows - i + 1): 
            print (end=" ") 
              
        # Print stars after spaces 
        # Print stars for each solid rows 
          
        if i == 1 or i == rows: 
            for j in range (1, rows + 1): 
                print ("*",end="") 
                  
        # stars for hollow rows 
        else: 
            for j in range (1,rows+1): 
                if (j == 1 or j == rows): 
                    print ("*",end="") 
                else: 
                    print (end=" ") 
        # Move to the next line/row 
        print() 

hollowRhombus(5)


def hollowRhombus(rows): 
      
    for i in range (1, rows + 1): 
        # Print trailing spaces 
          
        for j in range (2, i + 1): 
            print (end=" ") 
              
        # Print stars after spaces 
        # Print stars for each solid rows 
          
        if i == 1 or i == rows: 
            for j in range (1, rows + 1): 
                print ("*",end="") 
                  
        else: 
            for j in range (1,rows+1): 
                if (j == 1 or j == rows): 
                    print ("*",end="") 
                else: 
                    print (end=" ") 
        # Move to the next line/row 
        print() 

hollowRhombus(5)

def hollowRhombus(rows):

    for i in range(1, rows + 1):

        for j in range(2, i + 1):         #(1, i)
            print(end=" ")
        
        if i == 1 or i == rows:
            for j in range(1, rows + 1):
                print("*", end=" ")
        else:
            for j in range(1, rows + 1):
                if j == 1 or j == rows:
                    print("*", end=" ")
                else:
                    print(end="  ")

        print() 

hollowRhombus(5)

def hollowRhombus2(n):

    for i in range(1, n+1):

        for j in range(1, n*2):
            
            if j >= i and j <= i+4:
                print("* ", end="")
            else:
                print(end=" ")

        print()

hollowRhombus2(5)