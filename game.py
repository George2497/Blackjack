import random
class Blackjack():
  def __init__(self):
    self.limit = 21
    self.resetHands()

  @staticmethod
  def welcome():
    print("Welcome, the aim of the game is to get as close to 21 as you can \n" \
    "press 'H' to hit to get another card or press ENTER to quit \n" \
    "Goodluck!")

  def goodbye(self):
    print("Thank you for playing, goodbye!")

  def resetHands(self):
    self.card1 = random.randint(1, 10)
    self.card2 = random.randint(1, 11)
    self.hand = self.card1 + self.card2

  def game(self):
    while True:
      print(f"Your current hand is {self.hand} \n")
      
      userInput = input("Press 'H' to hit, 'K' to keep your hand or ENTER to quit: ")

      if userInput == "":
        self.goodbye()
        return
      
      if userInput.lower() == 'h':
        hit = random.randint(1, 11)
        self.hand += hit
        print(f"You drew {hit} your hand is now {self.hand}")
      
      if userInput.lower() == 'k':
        print(f"You have kept your hand at {self.hand}")
        self.restart()
        return

      if self.hand > self.limit:
        print(f"You're Bust! You hand is {self.hand} \n")
        self.restart()
        return
      elif self.hand == self.limit:
        print(f"Blackjack! You win! Your hand was {self.hand} \n")
        self.restart()
        return
    
  def restart(self):
    choice = input("Press 'R' to restart the game or press ENTER to quit: ")
    if choice.lower() == "r":
      self.resetHands()
      self.game()
    else:
      self.goodbye()

def main():
  play = Blackjack()
  play.welcome()
  play.game()

if __name__=="__main__":
  main()