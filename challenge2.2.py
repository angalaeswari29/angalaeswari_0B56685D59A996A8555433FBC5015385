#Implement a class called player that reperesents a cricket players. The player class should have a method called paly() which prints the player is playing cricket.derive two classes,Batsman and Bowler, from the player class.Ovderride the play() methode in each derived class to print "The batsman is batting" and "The blower is blowing",respectively.Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object. 
#define the base class player
class Player:
    def play(self):
        print("The player is playing cricket.")
# define the derived class Batsman
class Batsman(Player):
    def play(self):
        print("The batsman is batting.")
# define the derived class Bowler
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")
# create objects of Batsman and Bowler classes
batsman =Batsman()
bowler =Bowler()
#call the play() method for each object
batsman.play()
bowler.play()
