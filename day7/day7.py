from utils.data import get_data
import re

def rank_with_Js(hand):
    if 'J' not in hand:
        return rank(hand)
    results = []
    for char in set(hand):
        if char!='J':
            hand_updated = hand.replace('J',char).replace('J',char).replace('J',char).replace('J',char).replace('J',char)
            results.append((char,rank(hand_updated)))
    results.sort(key=lambda x: x[1],reverse=True)
    if results:
        return results[0][1]
    return rank(hand)
def rank(hand):
    sorted_hand = ''.join(sorted(hand))
    if re.fullmatch(r"(.)\1{4}",sorted_hand): #5 of a kind
        # print(hand,7)
        return 7
    if re.fullmatch(r".*(.)\1{3}.*",sorted_hand): #4 of a kind
        # print(hand,6)
        return 6
    if re.fullmatch(r".*(.)\1{2}.*(.)\2{1}.*",sorted_hand) or re.fullmatch(r".*(.)\1{1}.*(.)\2{2}.*",sorted_hand): #full house - 3 of the same and 2 of the same
        # print(hand,5)
        return 5
    if re.fullmatch(r".{0,2}(.)\1{2}.{0,2}",sorted_hand): #3 of a kind
        # print(hand,4)
        return 4
    if re.fullmatch(r".*(.)\1{1}.*(.)\2{1}.*",sorted_hand): #2 pairs
        # print(hand,3)
        return 3
    if re.fullmatch(r".{0,3}(.)\1{1}.{0,3}",sorted_hand): #1 pair
        # print(hand,2)
        return 2
    # print(hand,1)
    return 1 #just a high card

def rank_extra(hand1,hand2,wildcard=False):
    importance = {val:i for i,val in enumerate('23456789TJQKA') }
    if wildcard:
        importance = {val:i for i,val in enumerate('J23456789TQKA') }
    for i in range(5):
        if importance[hand1[i]]>importance[hand2[i]]:
            return 1
        if importance[hand2[i]]>importance[hand1[i]]:
            return 0

def part1(data):
    arr = [tuple(row.split(' ')) for row in data]
    n = len(arr)
    # print(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            rank1 = rank(arr[j][0])
            rank2 = rank(arr[j + 1][0])
            if rank1 > rank2:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                continue
            if (rank1 == rank2) and (rank_extra(arr[j][0],arr[j+1][0])>0):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    for i,tup in enumerate(arr):
        print(i,tup)
    return sum([(i+1)*int(tup[1]) for i,tup in enumerate(arr)])

def part2(data):
    arr = [tuple(row.split(' ')) for row in data]
    n = len(arr)
    # print(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            rank1 = rank_with_Js(arr[j][0])
            rank2 = rank_with_Js(arr[j + 1][0])
            if rank1 > rank2:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                continue
            if (rank1 == rank2) and (rank_extra(arr[j][0],arr[j+1][0],wildcard=True)>0):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return sum([(i+1)*int(tup[1]) for i,tup in enumerate(arr)])

if __name__=='__main__':
    data_dict =get_data(7)
    data = data_dict['data.txt']

    result_part1 = part1(data)
    print("part1:",result_part1)

    result_part2 = part2(data)
    print("part2:",result_part2)
