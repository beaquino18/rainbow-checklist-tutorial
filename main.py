import random
print("Good morning Captain Rainbow! Here's your outfit for the week:")

colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
items = ['Hat', 'Bowtie', 'Top', 'Coat', 'Bottom', 'Gloves', 'Shoes']
days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
outfits =[]


def randomColor():
    for color in colors:
        print(color)


def readDays():
    for day in days:
        print(f"\n{day}")
        for item in items:
            print(f"{item}:")



readDays()