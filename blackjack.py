import art
import os
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if sum(cards)>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"
    
def blackjack():
    print(art.logo)
    user_cards=[]
    computer_cards=[]
    is_gameover=False
    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
        
    while not is_gameover:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)  
        print(f"    Your's Cards: {user_cards}, Current Score: {sum(user_cards)}")
        print(f"    Computer's first card is {computer_cards[0]}")
        if user_score==0 or computer_score==0 or user_score>21:
            is_gameover=True 
        else:
            user_should_deal=input("Type 'y' to draw another card, type 'n' to pass: ")
            if user_should_deal=="y":
                user_cards.append(deal_cards())     
            else:
                is_gameover=True
                
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score=calculate_score(computer_cards)
        
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()=='y':
    clear()
    blackjack()
        
    