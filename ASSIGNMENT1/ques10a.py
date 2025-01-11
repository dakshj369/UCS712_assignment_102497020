import sys  
if len(sys.argv) != 2:
    print("Please give exactly one string.")
else:
    input_string = sys.argv[1]
    print("The length of the string is",len(input_string))