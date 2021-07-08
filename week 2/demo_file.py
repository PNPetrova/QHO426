age = int(input("What is your age: "))

if age < 20:
  print("You area a child!")
elif age > 65:
  print("You are old mate!")
elif age <= 30 and age >= 20:
  print("You are a groen up child!")
elif age > 30 and age < 65:
  print("You are an adult!")