# Function to convert number into string 
# Switcher is dictionary data type here 
def numbers_to_strings(argument): 
	switche = { 
		0: "zero", 
		1: "one", 
		2: "two", 
	} 

	# get() method of dictionary data type returns 
	# value of passed argument if it is present 
	# in dictionary otherwise second argument will 
	# be assigned as default value of passed argument 
	return switche.get(argument, "nothing") 

# Driver program 
if __name__ == "__main__": 
	argument=2
	print(numbers_to_strings(argument)) 
