import re
input = open("input.txt", "r")
bingo_calls = []
bingo_cards = []


def setup_bingo(input):
    bingo_calls = []
    bingo_cards = []
    card_count = -1
    for each in input:
        line = each.split("\n")[0]
        if line == '':
            card_count+=1
            bingo_cards.append([])
        elif card_count ==-1:
            bingo_calls = line.split(",")
        else: # must be a line for the bingo card
            row = re.split("  | ", line)
            empty = []
            for i in range(0, len(row)):
                if row[i] =="":
                    empty.append(i)
            for each in empty:
                row.pop(each)
            bingo_cards[card_count].append(row)

    return bingo_cards, bingo_calls

def check_of_value(value):
    for card in bingo_cards:
        for row in card:
            for i in range(0, len(row)):
                if row[i] == value:
                    row[i] = "*"
    if not check_for_bingo(value):
        return False
    else:
        return True


def print_bingo_cards():
    for card in bingo_cards:
        for row in card:
            print(row)
        print("")

def check_for_bingo(value):
    for card in bingo_cards:
        col_arr_count = [0,0,0,0,0]
        for row in card:
            line_count=0
            for i in range(0, len(row)):
                if row[i] == "*":
                    line_count +=1
                    col_arr_count[i] = col_arr_count[i] +1
            if line_count==5:
                if calculate_board_last(card):
                    print("bingo", calulate_value(card, value))
                    #return True
                #return False
        for each in col_arr_count:
            if each ==5:
                if calculate_board_last(card):
                    
                    print("bingo", calulate_value(card, value))
                    #return True
                #return False
    #print("no bingo")
    return False

def calulate_value(card, call):
    sum = 0
    for row in card:
        for value in row:
            if value != "*":
                sum+=int(value)
   
    sum = sum*int(call)
    return sum

def calculate_board_last(card):
    if len(bingo_cards) == 1:
        import pdb; pdb.set_trace()
        
    #import pdb; pdb.set_trace()
    bingo_test.append(card)
    try:
        bingo_cards.pop(bingo_cards.index(card))
        print(card)
        return True
    except ValueError:
        print("already removed")
    
bingo_test = []
bingo_cards_won = 0
bingo_cards_num = len(bingo_cards)
bingo_cards, bingo_calls = setup_bingo(input)
#import pdb; pdb.set_trace()
for call in bingo_calls:
    #print(call)
    if check_of_value(call) == True:
        break 
#print_bingo_cards()
#print(bingo_calls)