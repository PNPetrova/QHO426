print("Program Started!")

print("Please enter an ascii code:")
code = int(input())

if code in range(32,126):
 print("The character represented by the ascii value {} is: {}".format(code, chr(code)))
else:
  print("Invalid code")
  
print("Program Ended")