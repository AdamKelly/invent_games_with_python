# Figlet takes ASCII text and renders it in ASCII art fonts.
# Source = https://github.com/pwaller/pyfiglet
from pyfiglet import Figlet
import random
import time

def main():
    menu()

def menu():
    f = Figlet(font='slant')
    print(f.renderText('Magic 8 Ball'))
    choice = input("""
    A: Ask a question
    Q: Quit

    Please enter your choice: """).lower()

    if choice == 'a':
        magic8ball()
    elif choice == 'q':
        quit()
    else:
        print("That was not a valid choice")


def magic8ball():
    # A tuple is used to store potential answers
    # Source of responses - http://www.otcpas.com/advisor-blog/magic-8-ball-messages/
    print('\nPlease ask your question now ', end='')
    # Wait for 5 seconds
    time.sleep(5)
    print('\n....still thinking ')
    time.sleep(2)

    responses = (
        "As I see it, yes.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don’t count on it.",
        "It is certain.",
        "It is decidedly so.",
        "Most likely.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Outlook good.",
        "Reply hazy, try again.",
        "Signs point to yes.",
        "Very doubtful.",
        "Without a doubt.",
        "Yes.",
        "Yes – definitely.",
        "You may rely on it.",
    )

    print(random.choice(responses))
    time.sleep(2)


menu()

if __name__ == "__main__":
    main()