value_dct= {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
for i in range(2, 10):
    value_dct[str(i)] = i
from collections import Counter

# Const definition
ONE_PAIR = 15
TWO_PAIR = 16
THREE_OF_A_KIND = 17
STRAIGHT = 18
FLUSH = 19
FULL_HOUSE = 20
FOUR_OF_A_KIND = 21 
STRAIGHT_FLUSH = 22
ROYAL_FLUSH = 23

def highest_value(hand):
    value = [item[0] for item in hand]
    value.sort(key = lambda x: value_dct[x])
    return value_dct[value[-1]]

def is_one_pair(hand):
    value = [item[0] for item in hand]
    dct = Counter(value)
    values, c = 0, 0
    for key, value in dct.items():
        if dct[key] == 2:
            values, c = key, c + 1
    if c == 1:
        return [True, value_dct[values]]
    return [False]

def is_two_pair(hand):
    value = [item[0] for item in hand]
    dct = Counter(value)
    values, c = [], 0
    for key, value in dct.items():
        if dct[key] == 2:
            values.append(key)
            c += 1
    if c == 2:
        values.sort()
        return [True, value_dct[values[0]], value_dct[values[1]]]
    return [False]

def is_three_of_a_kind(hand):
    value = [item[0] for item in hand]
    dct = Counter(value)
    for key, value in dct.items():
        if dct[key] == 3:
            return [True, value_dct[key]]
    return [False] 

def is_straight(hand):
    value = sorted([value_dct[item[0]] for item in hand])
    for i in range(len(value) - 1):
        if value[i] + 1 != value[i + 1]:
            return [False]
    return [True, max(value)]

def is_flush(hand):
    s = set()
    for item in hand:
        s.add(item[1])
    return len(s) == 1

def is_full_house(hand):
    value = [item[0] for i in hand]
    dct = Counter(hand)
    three, pair = 0, 0
    for key, value in dct.items():
        if value == 3:
            three = key
        elif value == 2:
            pair = key
        else:
            return [False]
    return [True, value_dct[three], value_dct[pair]]

def is_four_of_a_kind(hand):
    value = [item[0] for item in hand]
    dct = Counter(hand)
    key = 0
    for key, value in dct.items():
        if value == 4:
            return [True, key]
    return [False]

def is_straight_flush(hand):
    check_result = is_straight(hand)
    if check_result[0] and is_flush(hand):
        return [True, check_result[1]]
    return [False]

def is_royal_flush(hand):
    value = "".join(sorted([item[0] for item in hand]))
    if value == "AJKQT" and is_flush(hand):
        return [True]

def get_rank(hand):
    print(hand)
    if is_royal_flush(hand):
        return ROYAL_FLUSH
    else: 
        check_result = is_straight_flush(hand)
        if check_result[0]:
            return [STRAIGHT_FLUSH, check_result[1]]
        else: 
            check_result = is_four_of_a_kind(hand)
            if check_result[0]:
                return [FOUR_OF_A_KIND, check_result[1]]
            else:
                check_result = is_full_house(hand)
                if check_result[0]:
                    return [FULL_HOUSE, check_result[1], check_result[1]]
                else:
                    check_result = is_flush(hand)
                    if check_result:
                        return [FLUSH]
                    else:
                        check_result = is_straight(hand)
                        if check_result[0]:
                            return [STRAIGHT, check_result[1]]
                        else:
                            check_result = is_three_of_a_kind(hand)
                            if check_result[0]: 
                                return [THREE_OF_A_KIND, check_result[1]]
                            else:
                                check_result = is_two_pair(hand)
                                if check_result[0]:
                                    return [TWO_PAIR, check_result[1], check_result[2]]
                                else:
                                    check_result = is_one_pair(hand)
                                    if check_result[0]:
                                        return [ONE_PAIR, check_result[1]]
                                    else:
                                        return [highest_value(hand)]

def compare_hand(player1, player2):
    player1.sort(key = lambda x: value_dct[x[0]], reverse = True)
    player2.sort(key = lambda x: value_dct[x[0]], reverse = True)
    for index in range(len(player1)):
        if value_dct[player1[index][0]] > value_dct[player2[index][0]]:
            return 1
        else: 
            if value_dct[player1[index][0]] < value_dct[player2[index][0]]:
                return 0
    return 0

def compare_last_card(player1, player2):
    card1, card2 = 0, 0
    dct1, dct2 = Counter(player1), Counter(player2)
    for key, value in dct1:
        if value == 1:
            card1 = key
            break
    for key, value in dct2:
        if value == 1:
            card2 = key
            break
    if value_dct[card1] > value_dct[card2]:
        return 1
    return 0

result = 0
with open("poker.txt", "r") as f:
    data = f.readlines()
for item in data:
    cards = item.split()
    first_hand, second_hand = cards[:5], cards[-5:]
    rank1, rank2 = get_rank(first_hand), get_rank(second_hand)
    print(rank1, rank2)
    if rank1[0] > rank2[0]:
        result += 1
    elif rank1[0] == rank2[0]:
        if rank1[0] in [ONE_PAIR, STRAIGHT_FLUSH, STRAIGHT, THREE_OF_A_KIND, FOUR_OF_A_KIND]:
            if rank1[1] > rank2[1]:
                result += 1
            elif rank1[1] == rank2[1]:
                result += compare_hand(first_hand, second_hand)
        elif rank[0] == TWO_PAIR:
            if rank[1] > rank2[1]:
                result += 1
            elif rank1[1] == rank2[1]:
                if rank1[2] > rank2[2]:
                    result += 1
                elif rank1[2] == rank2[2]:
                    result += compare_last_card(first_hand, second_hand)
        elif rank[0] == FLUSH:
            result += compare_hand(first_hand, second_hand)
        elif rank[0] == FULL_HOUSE:
            if rank[1] > rank2[1]:
                result += 1
            elif rank1[1] == rank2[1]:
                if rank1[2] > rank2[2]:
                    result += 1
print(result)

