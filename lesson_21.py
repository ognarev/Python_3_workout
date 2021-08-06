# Classes. My first cat class
import random

class TwitSimulator():
    "Twit model"
    max_symbols = 320

    def __init__(self, id, user, text):
        self.id = id
        self.user = user
        self.text = text
        self.lang = "en"
        self.quote_count = 0
        self.reply_count = 0
        self.retweet_count = 0
        self.favorite_count = 0

    def send(self):
        pass
    
    def delete(self):
        pass

class CatC():
    "My first cat class."
    #what my cat has
    legs_max = 4
    tail_max = 1
    colors = ['#4D4F5A', '#9d3922', '#078080', '#88ccbb']
    states = ['sleeping', 'eating', 'walking', 'running', 'jumping', 'brawling']
    moods = ['happy', 'angry', 'sleepy', 'tired', 'hungry', 'joyfull', 'creepy']
    
    def __init__(self, nickname='wild'):
        self.nickname = nickname
        self.legs = self.legs_max
        self.tail = self.tail_max
        self.color = random.choice(self.colors)
        self.state = random.choice(self.states)
        self.mood = random.choice(self.moods)

    #what my cat can do
    def get_info(self):
        if self.nickname == 'wild': print(f"This cat has no nickname, it's wild cat.")
        else: print(f"This cat nickname is {self.nickname}.")
        print(f"It has {self.color} fur color. {self.legs} legs and {self.tail} tail")

    def do_murmur(self):
        "Just start mur-mur"
        n = 2
        while n > 0:
            print("mur-murrrrr-mur")
            n -= 1
    
    def do_sleep(self):
        "The cat go to sleep"
        self.state = "sleeping"
        print(f"The cat is sleeping now.")
    
    def change_state(self):
        "The cat will do some random stuff if not sleeping."
        if self.state == "sleeping":
            print("Wake up, sleepy :)")
        self.state == random.choice(self.states)
        print(f"The cat is {self.state} now.")

# cat = CatC("Rosalinda")
# cat.get_info()
# cat.do_murmur()
# cat.do_sleep()
# cat.change_state()