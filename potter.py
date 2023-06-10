import requests
from random import *
from pprint import pprint


#api for harry potter characters


MAIN_CHARACTERS = ["Harry Potter", "Hermione Granger", "Ron Weasley", "Draco Malfoy", "Minerva McGonagall", "Cedric Diggory", "Severus Snape", "Rubeus Hagrid", "Neville Longbottom", "Luna Lovegood", "Ginny Weasley", "Sirius Black", "Remus Lupin", "Bellatrix Lestrange", "Lord Voldemort", "Dolores Umbridge", "Lucius Malfoy", "Argus Filch", "Vernon Dursley", "Marge Dursley", "Dudley Dursley", "Albus Dumbledore", "Madam Pomfrey", "Quirinus Quirrel", "Fred Weasley", "George Weasley", "Nearly Headless Nick", "Dobby", "Moaning Myrtle", "Peter Pettigrew", ]
MAIN_SPELLS = ["Aberto", "Accio", "Alohomora", "Ascendio", "Confundo", "Crucio", "Erecto", "Homenum Revelio", "Immobulus", "Incendio", "Obliviate", "Petrificus Totalus", "Reparo", "Sectumsempra", "Tarantallegra", "Unbreakable Vow", "Wingardium Leviosa", "Lumos", "Imperio"]
EVIL_CHARS = ["Bellatrix Lestrange", "Lord Voldemort", "Vernon Dursley", "Marge Dursley", "Dudley Dursley", "Peter Pettigrew", "Lucius Malfoy"]
GOOD_CHARS = ["Rubeus Hagrid", "Sirius Black", "Remus Lupin", "Nearly Headless Nick", "Dobby", "Moaning Myrtle"]

all_chars = 'https://hp-api.onrender.com/api/characters'
all_students = 'https://hp-api.onrender.com/api/characters/students'
all_staff = 'https://hp-api.onrender.com/api/characters/staff'
all_spells = 'https://hp-api.onrender.com/api/spells'


student_response = requests.get(all_students)
student_data = student_response.json()

staff_response = requests.get(all_staff)
staff_data = staff_response.json()

staff_names = []
for t in staff_names:
    new_t = t['name']
    staff_names.append(new_t)

student_names = []
for s in student_data[:20]:
    new_name = s['name']
    student_names.append(new_name)


def roll_dice():
    roll = randint(0, 10)
    return roll

def your_rand_name():
    name = choice(student_names)
    student_names.pop(student_names.index(name))
    if name in MAIN_CHARACTERS:
        MAIN_CHARACTERS.pop(MAIN_CHARACTERS.index(name))
    return name

def random_student():
    name = choice(student_names)
    return name

def random_staff():
    name = choice(staff_names)
    return name

def random_char():
    roll = roll_dice()
    if roll == 6:
        name = choice(EVIL_CHARS)
    elif roll < 6:
        name = choice(MAIN_CHARACTERS)
    elif roll > 6 and roll < 9:
        name = choice(GOOD_CHARS)
    else:
        name = "Albus Dumbledore"

    return name

def start_of_game():
    ans = input("Would you like to play as a random student (1), or yourself (2)?")
    if ans == '1':
        your_rand_name()
        print(you + random_student())
        play_wizard_fantasy()
    elif ans == '2':
        play_wizard_fantasy()
    else:
        print("Bad input, please type either 1 or 2.")
        start_of_game()

def next():
    input('(press enter)')

def new_game():
    input("Press enter to start a new game!")
    start_of_game()

def play_wizard_fantasy():
    next()
    print(first_friend + random_student())
    next()
    print(nemesis + random_char())
    next()
    print(your_crush + random_char())
    next()
    print(your_admirerer + random_char())
    next()
    print(savior + random_char())
    next()
    print(your_bf_gf + random_char())
    next()
    print(breaks_up + random_char())
    next()
    print(scandal + random_char() + " and " + random_char())
    next()

def random_ending():
    roll = randint(1, 3)
    if roll == 1:
        return tragic_ending + random_char()
    elif roll == 2:
        return happy_ending + random_char()
    else:
        return surprise_ending + random_char()




you = "You are: "

first_friend = "This person becomes your first friend upon arriving at Hogwarts: "

nemesis = "This person killed your parents when you were a baby and gave you a scar: "

your_crush = "After catching their eye at dinner, this person has become your crush: "

your_admirerer = "This person has developed passionate romantic feelings for you: "

savior = "After you get lost in the Forbidden Forest looking for magic mushrooms, this person saves your from spiders: "

your_bf_gf = "You start dating this person: "

breaks_up = "This person breaks up your relationship: "

scandal = "You walk in on these people snogging in the Room of Requirement: "

tragic_ending = "This person kills you with a gleam in their eye: "

happy_ending = F"This person saves you from being killed by {random_char()} and you end up marrying them and living happily every after: "

surprise_ending = "This person is revealed as your secret guardian, and they impart to you their magical knowledge and hoard of gold: "

#list of plot points
plot_points = [first_friend, nemesis, your_crush, your_admirerer, savior, your_bf_gf, breaks_up, scandal]
endings = [tragic_ending, happy_ending, surprise_ending]

# start_of_game()
