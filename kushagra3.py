
import time
import random
import sys

# Fun function to simulate typing effect
def typewriter(message, speed=0.05):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def print_balloons():
    balloons = [
        "🎈 🎈 🎈 🎈 🎈 🎈 🎈 🎈 🎈 🎈",
        "🎉 🎉 🎉 🎉 🎉 🎉 🎉 🎉 🎉 🎉",
        "🎂 🎂 🎂 🎂 🎂 🎂 🎂 🎂 🎂 🎂",
        "🎁 🎁 🎁 🎁 🎁 🎁 🎁 🎁 🎁 🎁"
    ]
    random.shuffle(balloons)
    for balloon in balloons:
        print(f"\n{balloon}")
        time.sleep(0.5)

def birthday_wish():
    # Start with a beautiful animated typing effect
    message = """
    *********************************************
    *                                           *
    *   To my best friend and the love of my    *
    *   life, the most amazing girl...         *
    *                                           *
    *   You make my world brighter with your    *
    *   smile, and your heart is more precious  *
    *   than words can describe. On this special *
    *   day, I just want to remind you how much *
    *   you mean to me.                         *
    *                                           *
    *   I hope this year brings you all the     *
    *   happiness you deserve and more!         *
    *                                           *
    *   I love you more than anything! 💖        *
    *                                           *
    *********************************************
    """
    typewriter(message, speed=0.04)

    print_balloons()
    
    print("\n🎉🎂🎁 HAPPY BIRTHDAY TO MY AMAZING GIRL! 🎁🎂🎉")
    print("You're my everything, and I'm beyond lucky to have you. 💖")

if __name__ == "__main__":
    birthday_wish()
