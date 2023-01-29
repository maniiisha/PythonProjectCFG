import random
import requests
import time

# prompt the user to enter their name
name = input("What is your name? ")

# welcome the user by name
print("Welcome, {}! Let's play the Pokémon game.".format(name))


# FETCHING A RANDOM POKEMON FROM THE API
def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return dict(name=pokemon['name'], id=pokemon['id'], height=pokemon['height'], weight=pokemon['weight'],
                experience=pokemon['base_experience'])


# FETCHING A POKEMON BY ITS NAME OR ID NUMBER FROM THE API
def fetch_certain_pokemon(poke_name):
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(poke_name)
    response = requests.get(url)
    pokemon = response.json()
    return dict(name=pokemon['name'], id=pokemon['id'], height=pokemon['height'], weight=pokemon['weight'],
                experience=pokemon['base_experience'])


def game():
    # INITILIZING THE SCORE AT 0 AND ASKING THE USER THE WINNING SCORE
    user_score = 0
    computer_score = 0
    winning_score = int(input(
        "You will play rounds with your opponent until one of you wins. The player with the most wins will be declared the ultimate winner. \nHow many points is your goal?"))

    # LOOP THE GAME UNTIL THE WINNING SCORE
    while user_score < winning_score and computer_score < winning_score:
        # GET TWO RANDOM POKEMONS AND IF THEY ARE THE SAME CHANGE IT TO ANOTHER ONE
        pokemon_one = random_pokemon()
        pokemon_two = random_pokemon()
        while pokemon_one == pokemon_two:
            pokemon_two = random_pokemon()
        print('You were given 1-{} and 2-{}'.format(pokemon_one['name'], pokemon_two['name']))
        pokemon_choice = input('Which pokemon do you want to choose').lower()
        #check if the pokemon choice is valid
        if pokemon_choice != pokemon_one['name'] and pokemon_choice != pokemon_two['name']:
            print('Invalid answer')
        # USER PICKS ONE OF THE OPTIONS AND FETCH A RANDOM POKEMON FOR THE COMPUTER
        elif pokemon_choice == pokemon_one['name'] or pokemon_two['name']:
            print('You have chosen {}'.format(pokemon_choice))
            opponent_pokemon = random_pokemon()
            time.sleep(1)
            print('The opponent chose {}'.format(opponent_pokemon['name']))
            time.sleep(1)
            my_pokemon = fetch_certain_pokemon(pokemon_choice)
            # USER PICKS THE HIGHEST SCORE WITHIN THE STATS
            print('Your stats are id:{}, weight:{}, height:{}, experience:{}'.format(my_pokemon['id'],
                                                                                     my_pokemon['weight'],
                                                                                     my_pokemon['height'],
                                                                                     my_pokemon['experience']))
            time.sleep(2)
            stat_choice = input('Which stat do you want to use?').lower()
            print('You have chosen {}'.format(stat_choice))
            my_stat = my_pokemon[stat_choice]
            time.sleep(1)
            # COMPUTER PICKS THE HIGHEST STAT
            choice_list = [opponent_pokemon['id'], opponent_pokemon['height'], opponent_pokemon['weight'],
                           opponent_pokemon['experience']]

            if opponent_pokemon['id'] == max(choice_list):
                computer_stat_choice = 'id'
            elif opponent_pokemon['height'] == max(choice_list):
                computer_stat_choice = 'height'
            elif opponent_pokemon['weight'] == max(choice_list):
                computer_stat_choice = 'weight'
            elif opponent_pokemon['experience'] == max(choice_list):
                computer_stat_choice = 'experience'
            opponent_stat = opponent_pokemon[computer_stat_choice]
            print('Your opponent has chosen {}, and its value is {}'.format(computer_stat_choice,
                                                                            opponent_pokemon[computer_stat_choice]))
            time.sleep(2)
            # USER STAT IS HIGHER THAN COMPUTER, USER WINS
            if my_stat > opponent_stat:
                user_score += 1
                print('Yay {}! You Win! Your Score: '.format(name), user_score, 'Computer Score: ', computer_score)
                print('---')  # THIS PRINT AND SLEEP IS ONLY FOR FORMATTING AND MORE READABILITY
                time.sleep(1)

            # USER STAT IS LESS THAN COMPUTER, COMPUTER WINS
            elif my_stat < opponent_stat:
                computer_score += 1
                print('Oh no {}! You Lose! Your Score: '.format(name), user_score, 'Computer Score: ', computer_score)
                print('---')
                time.sleep(1)
            # DRAW
            else:
                print('Draw!')
                print('---')
                time.sleep(1)
    # GAME IS OVER WHEN THE WINNING SCORE IS ACHIEVED
    if user_score or computer_score == winning_score:
        print('Game Over!')
        play_again_answer = input('Do you want to play again? (y/n)').lower()
        if play_again_answer == 'y':
            game()
        elif play_again_answer == 'n':
            print('Okay Bye!')


game()
