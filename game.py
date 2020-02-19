from random import choice

data = []
name = ''


def option(options):
    print("Okay, let's start")
    options = options.split(',')
    if len(options) == 3 or len(options) == 1:
        return "basic"
    elif len(options) == 5:
        return "medium"
    else:
        return "hard"


def new_rating():
    global data, name
    refresh = open("rating.txt", "w")
    for key, value in data.items():
        refresh.write(key + " " + str(value) + '\n')
    refresh.close()


def basic(user_version):
    global data, name
    win = dict(rock="paper", paper="scissors", scissors="rock")
    computer_version = choice(["paper", "rock", "scissors"])
    if win[user_version] == computer_version:
        print(f"Sorry, but computer chose {win[user_version]}")
    elif user_version == computer_version:
        print(f"There is a draw ({user_version})")
        data[name] += 50
    else:
        print(f"Well done. Computer chose {computer_version} and failed")
        data[name] += 100


def medium(user_version):
    global data
    global name
    win = dict(rock="paper spock",
               paper="scissors lizard",
               scissors="rock spock",
               lizard='rock scissors',
               spock='lizard rock')
    computer_version = choice(["paper", "rock", "scissors", "lizard", "spock"])
    if computer_version in win[user_version].split():
        print(f"Sorry, but computer chose {computer_version}")
    elif user_version == computer_version:
        print(f"There is a draw ({user_version})")
        data[name] += 50
    else:
        print(f"Well done. Computer chose {computer_version} and failed")
        data[name] += 100


def hard(user_version):
    global data, name
    win = dict(rock="fire scissors snake human wolf sponge tree",
               fire="scissors paper snake human tree wolf sponge",
               scissors="air tree paper snake human wolf sponge",
               snake='human wolf sponge tree paper air water',
               human='tree wolf sponge paper air water dragon',
               tree='wolf dragon sponge paper air water devil',
               wolf='sponge paper air water dragon lightning devil',
               sponge='paper air water devil dragon gun lightning',
               paper='air rock water devil dragon gun lightning',
               air="fire rock water devil gun dragon lightning",
               water=' devil dragon rock fire scissors gun lightning',
               dragon='devil lightning fire rock scissors gun snake',
               devil='rock fire scissors gun lightning snakes human',
               lightning='gun scissors rock tree fire snake human',
               gun='rock tree fire scissors snake human wolf')
    computer_version = choice(["paper", "rock", "scissors", 'fire', 'snake', 'human', 'tree', 'wolf',
                               'sponge', 'air', 'water', "dragon", 'devil', "lightning", "gun"])
    if user_version in win[computer_version].split():
        print(f"Sorry, but computer chose {computer_version}")
    elif user_version == computer_version:
        print(f"There is a draw ({user_version})")
        data[name] += 50
    else:
        print(f"Well done. Computer chose {computer_version} and failed")
        data[name] += 100


def start():
    global name, data
    name = input("Enter your name: ")
    name = name.strip()
    print("Hello,", name)
    option_type = input()
    file1 = open("rating.txt", "r")
    data = file1.read().split("\n")
    file1.close()
    data = [whose for user_data in data for whose in [user_data.split()] if len(whose) != 0]
    data = dict(data)
    for key, value in data.items():
        data[key] = int(value)
    if name not in data.keys():
        data[name] = 0
    return option_type


type_of_game = option(start())
if type_of_game == "basic":
    while True:
        user_input = input()
        if user_input == "!exit":
            print("Bye!")
            new_rating()
            break
        elif user_input == "!rating":
            print("Your rating:", data[name])
        else:
            basic(user_input)
elif type_of_game == "medium":
    while True:
        user_input = input()

        if user_input == "!exit":
            print("Bye!")
            new_rating()
            break
        elif user_input == "!rating":
            print("Your rating:", data[name])
        else:
            medium(user_input)
else:
    while True:
        user_input = input()
        if user_input == "!exit":
            print("Bye!")
            new_rating()
            break
        elif user_input == "!rating":
            print("Your rating:", data[name])
        else:
            hard(user_input)