from utils.data import get_data
import re

def part1(data):
    result = []
    for card in data:
        card_results = []

        numbers, winning_numbers = [el.split(' ') for el in card.split(':')[1].split('|')]
        numbers = [number for number in numbers if number!='']
        winning_numbers = [number for number in winning_numbers if number!='']

        for number in numbers:
            if (number in winning_numbers):
                card_results.append(number)
        if card_results:
            result.append(2**(len(card_results)-1))

    return sum(result)

def part2(data):
    #clean data
    cards_data = []
    for i in range(len(data)):
        numbers, winning_numbers = [el.split(' ') for el in data[i].split(':')[1].split('|')]
        numbers = [number for number in numbers if number!='']
        winning_numbers = [number for number in winning_numbers if number!='']
        cards_data.append((numbers,winning_numbers))


    #solve
    indices = list(range(len(cards_data)))
    return count_wins(cards_data, indices)

def count_wins(cards_data,indices):
    if len(indices)==0:
        return len(cards_data)

    won_card_indices = []
    for i in indices:
        count=0
        numbers, winning_numbers = cards_data[i]
        for number in numbers:
            if number in winning_numbers:
                count+=1
        for j in range(1,count+1):
            won_card_indices.append(i+j)

    return len(won_card_indices) + count_wins(cards_data,won_card_indices)


if __name__=='__main__':
    data_dict =get_data(4)
    data = data_dict['data.txt']

    result_part1 = part1(data)
    print("part1:",result_part1)

    result_part2 = part2(data)
    print("part2:",result_part2)
