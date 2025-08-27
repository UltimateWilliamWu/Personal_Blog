from Assignment.Ass1.solitaire_1 import initialize_shuffle_play

if __name__ == "__main__":
    final_result, is_win, cards_number = initialize_shuffle_play(int(input("Please enter an integer to feed the seed() function: ")))
    for line in final_result:
        print(line.rstrip())