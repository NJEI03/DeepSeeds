# import random

# # 🖼️ Array of ASCII art diagrams
# ascii_art_diagrams = [
#     r"""
#      /\_/\
#     ( o.o )
#      > ^ <
#     """,

#     r"""
#      _______
#     |       |
#     |       O
#     |      /|\
#     |      / \
#     |
#     =========
#     """,

#     r"""
#     _______
#    /       \
#   |  (• ◡•)  |
#    \_______/
#     """,

#     r"""
#      __
#     /  \
#    |    |
#    |____|
#   /      \
#  /________\
#     """
# ]

# # 📝 Array of creative writing prompts
# story_prompts = [
#     "Write a story about a robot who wants to be human.",
#     "Describe a world where plants can talk to people.",
#     "Create a mystery involving a time-traveling detective.",
#     "Tell a bedtime story set on a spaceship.",
#     "Imagine a dragon who’s afraid of fire.",
#     "Write about a kid who finds a magical notebook.",
#     "Narrate a short poem about loneliness and the moon.",
#     "Describe an ancient civilization powered by sound."
# ]

#If-else pair
age = int(input('What is your age? '))

if age > 16 :
    print("You are can play basketball.")
else:
    print('Wait until you are 16 to play basketball.')

#if - else - elif chain

# command = input('Enter "exit" to quit or "continue" to keep going: ')

# if command == 'exit':
#     print("Exiting the program.")
# elif command == 'continue':
#     print("Continuing enjoying.")
# else:
#     print("Invalid command. Please enter 'exit' or 'continue'.")
#Grading system
marks = float(input('Enter your marks: '))
if marks >=80:
    print("Grade: A👌")
elif marks >= 70 and marks < 80:
    print("Grade: B+✌")
elif marks >= 60 and marks < 70:
    print("Grade: B👍")
elif marks >= 50 and marks < 60:
    print("Grade: C✔")
elif marks >= 40 and marks < 50:
    print("Grade: D😒")
else:
    print("Very poor performance my friend! You need to work harder😢.")