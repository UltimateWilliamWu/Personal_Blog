from itertools import chain
from random import seed, shuffle
from collections import defaultdict
import unicodedata


def Cards(num):
    group, order = num // 13, num % 13
    groups = ["Hearts", "Diamonds", "Clubs", "Spades"]
    orders = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
    name = f"PLAYING CARD {orders[order]} OF {groups[group]}"
    return unicodedata.lookup(name)


def Display_Cards(all_cards):
    display_result = []
    for i in all_cards:
        display_result.append("\t" + "\t".join(i))
    return display_result


def update(all_cards, wait_for_match, num):
    wait_for_match.remove(num)
    row, col = 12 - num % 13, num // 13 - 1
    all_cards[row][col] = Cards(num)
    if 0 < row < 6:
        wait_for_match.append(num + 1)
    elif 6 < row < 12:
        wait_for_match.append(num - 1)


def is_valid_number(num):
    num = num.strip()
    if num == "":
        return False
    if num[0] == "-":
        num = num[1:]
    return num.isdigit()


def simulate(times, index):
    all_results = {}
    for time in range(times):
        result, cards_num = play_game(index + time)
        all_results[cards_num] = all_results.get(cards_num, 0) + 1
    print("Number of cards left | Frequency")
    print("--------------------------------")
    for num in sorted(all_results, reverse=True):
        frequency = all_results[num] / times
        print(f"{num:20} | {frequency:9.2%}")


def play_one_game(num, result, wait_for_match, cards, placed_cards):
    number_words = {
        1: "first", 2: "second", 3: "third"
    }
    result.append(f"Starting {number_words[num]} round...")
    result.append("")

    checked = []
    for num in cards[::-1]:
        current_card = cards.pop()
        if current_card in wait_for_match:
            result.append("Placing card from top of stack of cards left 😊️")
        else:
            result.append("Cannot place card from top of stack of cards left ☹️")
            checked.append(current_card)
        result.append("]" * len(cards))
        if checked:
            result.append("[" * (len(checked) - 1) + Cards(checked[-1]))
        else:
            result.append("")

        if current_card in wait_for_match:
            update(placed_cards, wait_for_match, num)
            result.extend(Display_Cards(placed_cards))
            result.append("")
            while checked and checked[-1] in wait_for_match:
                result.append("Placing card from top of stack of cards put aside 😊️")
                result.append("]" * len(cards))
                update(placed_cards, wait_for_match, checked.pop())
                if checked:
                    result.append("[" * (len(checked) - 1) + Cards(checked[-1]))
                else:
                    result.append("")
                result.extend(Display_Cards(placed_cards))
                result.append("")
            if checked:
                result.append("Cannot place card from top of stack of cards put aside ☹️")
                result.append("")
        else:
            result.append("")
    return checked


def play_game(seed_):
    seed(seed_)
    cards = sorted(set(range(52)) - {6, 19, 32, 45})
    shuffle(cards)
    result = ["All 7s removed and placed, rest of deck shuffled, ready to start!", "]" * len(cards)]
    all_cards = [["", "", "", ""] for _ in range(13)]
    all_cards[6] = [Cards(19), Cards(32), Cards(45), Cards(6)]
    wait_for_match = [5, 7, 18, 20, 31, 33, 44, 46]
    result.append("")
    result.extend(Display_Cards(all_cards))

    checked = []
    for num in range(1, 4):
        result.append("")
        checked = play_one_game(num, result, wait_for_match, cards, all_cards)
        if not checked:
            break
        else:
            cards = checked[::-1]
    if not wait_for_match:
        result.append("You placed all cards, you won 👍")
    else:
        result.append(f"You could not place {len(checked)} cards, you lost 👎")
    return result, len(checked)


if __name__ == '__main__':
    seed_input = int(input("Please enter an integer to feed the seed() function: "))
    result_show, left_cards_num = play_game(seed_input)
    line_num = len(result_show)
    print(f"\nThere are {line_num} lines of output; what do you want me to do?\n")
    while True:
        print("Enter: q to quit")
        print(f"       a last line number (between 1 and {line_num})")
        print(f"       a first line number (between -1 and -{line_num})")
        print(f"       a range of line numbers (of the form m--n with 1 <= m <= n <= {line_num})")
        user_input = input("       ")
        need_to_print = []
        if user_input == "q":
            break
        else:
            lst = user_input.split("--")
            if len(lst) == 2 and is_valid_number(lst[0]) and is_valid_number(lst[1]):
                m, n = int(lst[0]), int(lst[1])
                if 1 <= m <= n <= line_num:
                    need_to_print = result_show[m - 1:n]
            elif len(lst) == 1 and is_valid_number(lst[0]):
                number = int(lst[0])
                if 1 <= number <= line_num:
                    need_to_print = result_show[:number]
                elif -line_num <= number <= 1:
                    need_to_print = result_show[number:]
        if need_to_print:
            print()
            for line in need_to_print:
                print(line.rstrip())
        print()
