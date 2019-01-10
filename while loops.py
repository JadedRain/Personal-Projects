##Logan Douglas
#10/12/18
##Period 4-5

##test = 5
##
##while True:
##  print(test)
##  test +=6
##  if test > 1000:
##    break
####
##count = 0
##while count >= 0:
##  count += 1
##  if count > 100:
##    break
##  if count == 5 or count == 25 or count == 50 or count == 75:
##    continue
##  print(count)



health = 10
trolls = 0
damage = 5


while health > 0:
  trolls +=1
  health-= damage
  print("Your hero has killed a troll adding up to",trolls,"Your hero took",damage,"damage")
