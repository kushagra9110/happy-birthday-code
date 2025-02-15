import time
import sys

def typewriter(message, speed=0.1):
    """Simulates typing effect."""
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def birthday_wish():
    message = """
    *********************************************
    *                                           *
    *    Happy Birthday to the most amazing     *
    *   best friend and my beautiful girl anya ji!   
    *                                           *
    *    You bring so much joy into my life,    *
    *   and I'm so grateful to have you by my   *
    *   side. Here's to another year of love,   *
    *   laughter, and unforgettable memories!   *
    *                                           *
    *   May all your dreams come true, and may  *
    *   this year be filled with endless joy!   *
    * I don't know about the future but i'm damn sure that one day i'll surely visit pakistan and i'll meet you.*
    * I don't know wether we we will be toegther or not as partners but i want to be with you forever as a friend bhi chlega bs aap saath rehna mere.*
    * I'll always protect you from everything i promise and you will never ever feel alone till i'm alive.*
      I'm sorry for my mistakes but i'm bringing a change in myself too just for my anya ji*
    *********************************************
    """
    typewriter(message, speed=0.05)

    print("💖🎂💐🎉🎁 Happy Birthday! MY CUTU MY WORLD 💖🎂💐🎉🎁")
    print("You're my favorite person in the world, and I love you deeply. 💖")

if __name__ == "__main__":
    birthday_wish()
