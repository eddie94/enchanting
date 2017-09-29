import random

class my_item():

    def __init__(self):
        self.price = 100000
        self.enchant = 0

    def sell_item(self):
        price = self.price
        self.price = 100000
        self.enchant = 0
        return price

def reinforce(item):
    index = random.random()
    prob = index * 100
    success = False

    if item.enchant == 0:
        if prob >= 0 and prob <=100:
            success = True
            item.enchant = 1
            item.price *= 1.2
        else:
            success = False
    elif item.enchant == 1:
        if prob >= 0 and prob <=95:
            success = True
            item.enchant = 2
            item.price *= 1.2
        else:
            success = False
    elif item.enchant == 2:
        if prob >= 0 and prob <=90:
            success = True
            item.enchant = 3
            item.price *= 1.2
        else:
            success = False
    elif item.enchant == 3:
        if prob >= 0 and prob <=80:
            success = True
            item.enchant = 4
            item.price *= 1.2
        else:
            success = False
    elif item.enchant == 4:
        if prob >= 0 and prob <=80:
            success = True
            item.enchant = 5
            item.price *= 1.2
        else:
            success = False
    elif item.enchant == 5:
        if prob >= 0 and prob <=80:
            success = True
            item.enchant = 6
            item.price *= 1.2
        else:
            success = False
    elif item.enchant == 6:
        if prob >= 0 and prob <=80:
            success = True
            item.enchant = 7
            item.price *= 1.2
        else:
            success = False
    elif item.enchant == 7:
        if prob >= 0 and prob <=70:
            success = True
            item.enchant = 8
            item.price *= 1.2
        else:
            success = False
    elif item.enchant == 8:
        if prob >= 0 and prob <=65:
            success = True
            item.enchant = 9
            item.price *= 1.2
        else:
            success = False
    elif item.enchant == 9:
        if prob >= 0 and prob <=60:
            success = True
            item.enchant = 10
            item.price *= 1.2
        else:
            success = False
    elif item.enchant == 10:
        if prob >= 0 and prob <=50:
            success = True
            item.enchant = 11
            item.price *= 1.2
        else:
            success = False
    elif item.enchant == 11:
        if prob >= 0 and prob <=40:
            success = True
            item.enchant = 12
            item.price *= 1.2
        else:
            success = False
    elif item.enchant == 12:
        if prob >= 0 and prob <=30:
            success = True
            item.enchant = 13
            item.price *= 1.2
        else:
            success = False
    elif item.enchant == 13:
        if prob >= 0 and prob <=20:
            success = True
            item.enchant = 14
            item.price *= 1.2
        else:
            success = False
    elif item.enchant == 14:
        if prob >= 0 and prob <=10:
            success = True
            item.enchant = 15
            item.price *= 1.2
        else:
            success = False
    elif item.enchant >= 15:
        if prob >= 0 and prob <=5:
            success = True
            item.enchant = 16
            item.price *= 1.2
        else:
            success = False

    return success

