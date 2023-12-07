f = open("in.in").readlines()
#f.append("J3345 1")

letter_vals = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "J": 1
}

hands_and_bids_vals = []

for line in f:
    line = line.strip()
    hand, bid = line.split()
    bid = int(bid)
    val = 0
    int_hand = []
    for c in hand:
        if c.isdigit():
            int_hand.append(int(c))
        else:
            int_hand.append(letter_vals[c])
    pair = 0
    three = 0
    four = 0
    five = 0
    jokers = int_hand.count(1)
    for i in int_hand:
        num = int_hand.count(i)
        if i != 1: num = num + jokers
        if num == 2: pair += 1
        if num == 3: three += 1
        if num == 4: four += 1
        if num == 5: five += 1

    print("before", jokers, pair, three)
    while jokers >0:
        if five: break
        elif four: break
        elif three and jokers == 2: 
            pair = 0
            jokers = 0
        elif 1 < three <= 3 and jokers == 1:
            jokers = 0
            pair = 0
        elif pair == 4 and jokers: 
            pair = 2
            jokers = 0
        else: jokers = 0


    print("after", jokers, pair, three)
    if five or jokers == 5: val = 6000
    elif four or jokers == 4: val = 5000
    elif (three and pair) or three == 4 : val = 4000
    elif three: val = 3000
    elif pair == 4: val = 2000
    elif pair: val = 1000
    hands_and_bids_vals.append((int_hand, bid, val))



print(hands_and_bids_vals)
sorted_hands = sorted(hands_and_bids_vals, key = lambda x: (x[2], x[0]))
print(sorted_hands)

total = 0

for i, hands in enumerate(sorted_hands):
    total += (i+1)*hands[1]

print(total)


