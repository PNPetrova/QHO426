print("Program Started!")

print("Please enter an ascii code:")
code = int(input())

if (code >= 32 and code <= 126):
 print("The character represented by the ascii value {} is: {}".format(code, chr(code)))
else:
  print("Not recognized")

print("Program Ended")