##Logan Douglas
##10/5/18
##Nested if statment

num1 = float(input("Pick a number"))
num2 = float(input("Pick a number"))

if num1<=num2:
  if num1 == num2:
    print("Equal")
  else:
    print("Not equal")
  if num1 < num2:
      print("less than")
  elif num1 > num2:
      print("Greater than")
  else:
    print("They are just equal")
print("Done")
