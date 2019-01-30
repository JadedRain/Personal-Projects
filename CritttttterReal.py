import time
from datetime import datetime
import calendar

class Critter(object):
    #A virtual pet
    def __init__(self,name,hunger,boredom):
        self.name = name
        self.__hunger = hunger
        self.__boredom = boredom

    def __passTime(self):
        dt = datetime.now()
        rTime = dt.second / 100
        self.__hunger+=rTime
        self.__boredom+=rTime

    def play(self):
        print("You decide to play with",self.name+"!")
        dt = datetime.now()
        playTime = int(input("How long do you want to play with (seconds)"+self.name))
        play = dt.second/100*playTime
        self.__boredom-=play
        time.sleep(playTime)
        if self.__boredom<0:
            self.__boredom = 0
        self.__passTime()

    def talk(self):
        print(self.name,"is",self.mood)
        self.__passTime()

    def eat(self):
        print("You decide to feed",self.name+"!")
        dt = datetime.now()
        feedTime = int(input("How long do you want to feed (seconds) "+self.name))
        food = dt.second/ 100 * feedTime
        self.__hunger-= food
        time.sleep(feedTime)
        if self.__hunger<0:
            self.hunger=0
        self.__passTime()

    @property
    def mood(self):
        unhappiness = self.__hunger + self.__boredom
        if 5 > unhappiness:
           mood = "Happy"
        elif unhappiness <= 10:
            mood = "Okay"
        elif unhappiness <= 15:
            mood = "Frustrated"
        else:
            mood = "Mad"
        return mood

def main():
    name = input("Enter your critter's name!: ")
    crit = Critter(name,0,0)
    choice = None
    while choice != 0:
        print("""
        Talk:1
        Eat:2
        Play:3
        Quit:0
        """)
        choice = int(input("Choice: "))
        if choice == 0:
            print("GoodBye")
        elif choice == 1:
            crit.talk()
        elif choice == 2:
            crit.eat()
        elif choice == 3:
            crit.play()
        else:
            print("Not a valid option!")
main()