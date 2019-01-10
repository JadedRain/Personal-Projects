##word = input("Enter a word")
##pos1 = word.find("Game")
##pos2 = word.find("Game",pos1+1)
##
##substring = word[pos1:pos2]
##
##print(substring)

name = input("Please enter your first and last name")
split = name.find(" ")
print("Hello",name[:split])
print("Nice to see you in good health",name[split+1:])

firstname = name[:split]
lastname = name[split+1:5]


