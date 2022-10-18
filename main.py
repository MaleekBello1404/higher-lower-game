from game_data import data
from art import logo,vs
import random
from replit import clear
# def comparison():


# select = random.randint(0,number_of_data-1)
def comparison(value):
    # value = 0
    name = (data[value]["name"])
    description = (data[value]["description"])
    country = (data[value]["country"])
    return f"{name}, a {description}, From {country}"
    


def calc(user_guess,value_a, value_b):
    if value_a > value_b:
        return user_guess == "a"
    else:
        return user_guess == "b"

def game():
    print(logo)
    number_of_data = len(data)
    values = []
    value_b = (random.randint(0, number_of_data - 1))
    game_on = True
    score = 0
    while game_on:
        value_a = value_b
        value_b = (random.randint(0, number_of_data - 1))
        if value_a == value_b:
            value_b = (random.randint(0, number_of_data - 1))
        values.append(value_a)
        values.append(value_b)
        # print(values)
        
        print(f"Compare A: {comparison(value_a)}")
        print(vs)    
        print(f"Compare B: {comparison(value_b)}")
        
        
        
        user_answer = input("Who has more followers A or B: ").lower()
        
        value_a_followers = 0
        value_b_followers = 0
        value_a_followers = (data[value_a]["follower_count"])
        value_b_followers = (data[value_b]["follower_count"])
        
        
        result = calc(user_answer,value_a_followers, value_b_followers)
        # print(result)
        clear()
    
        
        if result:
            score += 1
            print(f"You're correct, Your current score: {score}")
        else:
            print(f"Sorry, that's wrong, Final score: {score}")
            game_on = False
         
game()
