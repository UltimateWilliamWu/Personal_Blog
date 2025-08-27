from itertools import chain
from random import seed, shuffle
from collections import defaultdict

def Cards(number):
    group, order = number // 8, number % 8
    all_ace_cards = [127153, 127169, 127185, 127137]
    if order > 0:
        order += 5
    if order > 10:
        order += 1
    return chr(all_ace_cards[group] + order)


def Divide(number, cards):
    groups = [[] for _ in range(number)]
    cards.reverse()
    for card in range(len(cards)):
        groups[card % number].append(cards[card])
    return groups


def handle_discard(result, discard_cards, discard_group, group_cards):
    if len(group_cards) == 0:
        if discard_cards:
            result.append(f"Adding to the cards that have been discarded all cards in the stack.")
        else:
            result.append(f"Discarding all cards in the stack.")
    elif len(discard_group) == 1:
        if discard_cards:
            result.append(f"Adding to the cards that have been discarded the card before the ace.")
        else:
            result.append(f"Discarding the card before the ace.")
    elif len(discard_group) != 0:
        if discard_cards:
            result.append(
                f"Adding to the cards that have been discarded the {len(discard_group)} cards before the ace.")
        else:
            result.append(f"Discarding the {len(discard_group)} cards before the ace.")

    discard_cards.extend(discard_group)
    discard_group.clear()


def handle_keep(result, cards, group_cards):
    if len(group_cards) == 1:
        if not cards:
            result.append(f"Keeping the ace, turning it over.")
        else:
            result.append(f"Also keeping the ace, turning it over.")
    elif len(group_cards) == 2:
        if not cards:
            result.append(f"Keeping the ace and the card after, turning them over.")
        else:
            result.append(f"Also keeping the ace and the card after, turning them over.")
    elif len(group_cards) != 0:
        if not cards:
            result.append(f"Keeping the ace and the {len(group_cards) - 1} cards after, turning them over.")
        else:
            result.append(f"Also keeping the ace and the {len(group_cards) - 1} cards after, turning them over.")

    cards.extend(group_cards[::-1])
    group_cards.clear()


def display_discard_cards(discard_cards):
    if discard_cards:
        return "[" * (len(discard_cards) - 1) + Cards(discard_cards[-1])
    return ""


def display_cards(cards, last_show=False, group_number_show=0):
    result = ""
    stack_num = 1
    for card in cards:
        if len(card) == 0:
            result += " " * 12
        elif last_show and group_number_show == stack_num:
            result += "[" * (len(card) - 1) + Cards(card[-1]) + " " * (12 - len(card))
        else:
            result += "]" * len(card) + " " * (12 - len(card))
        stack_num += 1
    return result.rstrip()


def process_group(result, groups, discard_groups, discard_cards, cards, group_number):
    number_words = {
        1: "First", 2: "Second", 3: "Third", 4: "Fourth",
        5: "Fifth", 6: "Sixth", 7: "Seventh", 8: "Eighth"
    }

    group_cards = groups[group_number - 1]
    group_cards.reverse()

    discard_group = discard_groups[group_number - 1]
    turn_over = 1

    while group_cards:
        if group_cards[-1] % 8 == 0:
            break
        discard_group.append(group_cards.pop())
        turn_over += 1

    if len(group_cards) == 0:
        result.append(f"No ace in {number_words[group_number].lower()} stack, after it has been turned over.")
    else:
        if len(group_cards) == 1:
            result.append(
                f"{number_words[turn_over]} (and last) card in {number_words[group_number].lower()} stack, after it has been turned over, is an ace.")
        else:
            result.append(
                f"{number_words[turn_over]} card in {number_words[group_number].lower()} stack, after it has been turned over, is an ace.")

    result.append(display_cards(groups, True, group_number))
    result.append(display_cards(discard_groups, True, group_number))
    result.append(display_discard_cards(discard_cards))
    result.append("]" * len(cards))
    result.append("")

    handle_discard(result, discard_cards, discard_group, group_cards)
    handle_keep(result, cards, group_cards)

    result.append(display_cards(groups))
    result.append("")
    result.append(display_discard_cards(discard_cards))
    result.append("]" * len(cards))
    result.append("")


def simulate(times, input_content):
    results = {}
    for time in range(times):
        result, is_Win, cards_num = initialize_shuffle_play(time + input_content)
        if is_Win:
            results[cards_num] = results.get(cards_num, 0) + 1
    print("Number of cards left when winning | Frequency")
    print("---------------------------------------------")
    for number in sorted(results):
        frequency = results[number] / times
        print(f"{number:33} | {frequency:9.2%}")


def play_game(number, cards, discard_cards):
    result = []
    if number == 4:
        result.append(f"Distributing the cards in the deck into {number} stacks.")
    else:
        result.append(f"Distributing the cards that have been kept into {number} stacks.")

    groups = Divide(number, cards)
    result.append(display_cards(groups))
    result.append("")
    result.append(display_discard_cards(discard_cards))
    result.append("")
    result.append("")

    cards = []
    discard_groups = [[] for _ in range(number)]

    for group_number in range(1, number + 1):
        process_group(result, groups, discard_groups, discard_cards, cards, group_number)

    return result, cards, discard_cards


def initialize_shuffle_play(input_seed):
    cards = list(range(32))
    seed(input_seed)
    shuffle(cards)
    print("\nDeck shuffled, ready to start!")
    print("]" * 32)
    print("")

    discard_cards = []
    result = []
    for i in range(4, 1, -1):
        print_results, keep_cards, discarded_cards = play_game(i, cards, discard_cards)
        cards = keep_cards
        discard_cards = discarded_cards
        result.extend(print_results)

    win_result = False
    result.append(f"Displaying the {len(cards)} cards that have been kept.")
    if set(cards[:4]) == {0, 8, 16, 24}:
        result.append("You won!")
        win_result = True
    else:
        result.append("You lost!")

    result.append("")
    result.append("")
    result.append(display_discard_cards(discard_cards))
    last_line = ""
    for card in cards[::-1]:
        last_line += Cards(card)
    result.append(last_line)
    return result, win_result, len(cards)


# 主程序入口
if __name__ == "__main__":
    final_result, is_win, cards_number = initialize_shuffle_play(int(input("Please enter an integer to feed the seed() function: ")))
    for line in final_result:
        print(line.rstrip())
