class Critter(object):

    total = 0

    def __init__(self,name):
        print("New Creature discovered")
        self.name = name
        Critter.total+=1

    def __str__(self):
        rep = self.name
        return rep

    @staticmethod
    def status():
        print("\nThe total number of critters is",Critter.total)

    def talk(self):
        print("Hello, i'm an instance of class Critter. "+self.name)

cirt = Critter("Jade")
cirt2 = Critter("Tom")
cirt3 = Critter("Emily")
obj = cirt.__str__()
if obj == "Jade":
    print("Hello bob")
print(cirt)
Critter.status()