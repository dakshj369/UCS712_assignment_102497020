import sys  
if len(sys.argv) != 3:
    print("Please give exactly two numbers.")
else:
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        result = num1 + num2
        print("The sum of  is",result)
    except:
        print("Please give valid numbers.")