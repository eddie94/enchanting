from item import *
import time
import os

def title_call():
    print('''
        □□□□□□□□    □               □□□
                     □    □         □□□□□□□□□□     □
                     □    □□□□                           □
                     □    □               □□□            □
                     □    □              □    □           □□□□□□
                                            □□□            □
                     □□□□                 □              □
                   □        □               □              □
                   □        □               □
                     □□□□            □□□□□□□□□□
        ''')
    print("1. 게임하기 \t 2. 안하기")

def game_scene():

    check_lose = False
    cash = 1000000
    item = my_item()

    while not check_lose:
        enchant_down()
        print("1. 강화하기 \t 2. 팔기 \t 3. 끝")
        print("돈 : %d \t 강화수치 : %d \t 판매가:%d" % (cash, item.enchant,item.price))

        if cash < 50000:
            print("you lost")
            check_lose = True

        menu_select = int(input())

        if menu_select == 1:
            enchant_effect()
            success = reinforce(item)
            cash -= 25000
            if not success:
                failure()
                cash -= item.price
                item = my_item()
            else:
                successful()
        elif menu_select == 2:
            item_price = item.sell_item()
            cash += item_price
            cash -= 100000
        elif menu_select == 3:
            break

def menu_select():
    num = int(input())
    return num

def enchant_up():
    print('''
    
    
    □□□□□□□□□□
    □               □       □□□□□□□□□□□□□□□□□□□□□□□
    □               □       □                                       □
    □               □       □                                       □
    □               □       □                                       □
    □               □       □                                       □
    □               □    □                                          □
    □      □□     □□□□               □□□□□□□□             □
    □      □□     □                    □            □             □
    □               □                    □            □             □
    □      ■■     □                    □            □              □
    □      ■■     □□□□               □            □             □
    □               □     □              □□□□□□□□             □
    □               □       □                                        □
    □               □        □                                       □
    □               □        □                                       □
    □               □        □                                       □
    □               □        □□□□□□□□□□□□□□□□□□□□□□□
    □□□□□□□□□□
        ''')

def enchant_down():
    print('''


        □□□□□□□□□□
        □               □       □□□□□□□□□□□□□□□□□□□□□□□
        □               □       □                                       □
        □               □       □                                       □
        □               □       □                                       □
        □               □       □                                       □
        □               □    □                                          □
        □      ■■     □□□□               □□□□□□□□             □
        □      ■■     □                    □            □             □
        □               □                    □            □             □
        □      □□     □                    □            □              □
        □      □□     □□□□               □            □             □
        □               □     □              □□□□□□□□             □
        □               □       □                                        □
        □               □        □                                       □
        □               □        □                                       □
        □               □        □                                       □
        □               □        □□□□□□□□□□□□□□□□□□□□□□□
        □□□□□□□□□□
            ''')

def enchant_effect():
    enchant_up()
    time.sleep(1)
    os.system('cls')
    enchant_down()
    os.system('cls')
    for i in range(4):
        enchant_up()
        time.sleep(0.5)
        os.system('cls')
        enchant_down()
        time.sleep(0.5)
        os.system('cls')
    for i in range(8):
        enchant_up()
        time.sleep(0.25)
        os.system('cls')
        enchant_down()
        time.sleep(0.25)
        os.system('cls')

def failure():
    os.system('cls')
    print('''
              □□□□□□          □          □□□□□□□       □          
              □                   □□               □             □        
              □                  □  □              □             □      
              □□□□           □□□□             □             □   
              □                □      □            □             □     
              □               □        □           □             □        
              □              □          □    □□□□□□□       □□□□□□    
          ''')
    time.sleep(2)
    os.system('cls')

def successful():
    os.system('cls')
    print('''
                 □□□□□□   □      □   □□□□□  □□□□□   □□□□□   □□□□□  □□□□□                                                                     
                 □             □      □   □          □           □           □          □                           
                 □             □      □   □          □           □           □          □                         
                 □□□□□□   □      □   □          □           □□□□□   □□□□□  □□□□□                                                    
                           □   □      □   □          □           □                   □          □              
                           □   □      □   □          □           □                   □          □                   
                 □□□□□□   □□□□□   □□□□□  □□□□□   □□□□□   □□□□□  □□□□□                                                                                                                                                                     
          ''')
    time.sleep(2)
    os.system('cls')