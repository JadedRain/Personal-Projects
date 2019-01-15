class Human(object):

    def __init__(self,name,hairColor,eyeColor,limbCount,skinColor,height,weight,iq,gender):
        self.name = name
        self.hairColor = hairColor
        self.eyeColor = eyeColor
        self.limbCount = limbCount
        self.skinColor = skinColor
        self.height = height
        self.weight = weight
        self.iq = iq
        self.gender = gender
    def introduceSelf(self):
        print("Hello my name is "+self.name)
    def describeSelf(self):
        print("I have "+self.hairColor+" hair")
        print("I have "+self.eyeColor+" eyes")
        print("I am",self.height," tall")
        print("I weight",self.weight,"lbs")
        print("My gender is "+self.gender)
        print("I have",self.limbCount,"limbs")
        print("I have an iq of",self.iq)
    def learn(self):
        print("What is your favorite color!")
        color = input("Enter here:")
        print("Correct! your favorite color is",color)
        self.iq+=1
        print("Your iq is now",self.iq)
    def cry(self):
        print("You cry in a corner to yourself")
        print("You end up crying off some weight")
        self.weight-=10
        print("Your weight is now",self.weight,"lbs")
    def jump(self):
        print("You decide to jump...how many times?")
        jumps = input("Jumps: ")
        print("You decide to jump",jumps,"times")
        if int(jumps) > 5:
            self.weight-=2
        elif int(jumps) > 10:
            self.weigh-=25
        else:
            self.weight-=0

jade = Human("Jade","brown","green",4,"white","5' 10",124,90,"female")
jade.introduceSelf()
jade.describeSelf()
jade.learn()
jade.describeSelf()
jade.cry()
jade.describeSelf()
jade.jump()
jade.describeSelf()