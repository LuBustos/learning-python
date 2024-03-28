"""Module providing a function printing python version."""

total_players = {
    "player_1": 0,
    "player_2": 1
}

indicate = {
    "Y": "Same",
    "X": "Lose",
    "Z": "Win"
}

hands = {
    "Rock": "Rock",
    "Paper": "Paper",
    "Scissors": "Scissors"
}

player_1_hand = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
}

contrary_hand = {
    "Rock": "X",
    "Paper": "Y",
    "Scissors": "Z"
}

player_2_hand = {
    "X": {"choose": "Rock", "point": 1},
    "Y": {"choose": "Paper", "point": 2},
    "Z": {"choose": "Scissors", "point": 3}
}

result_points = {
    "lost": 0,
    "draw": 3,
    "win": 6
}


def read_file(path):
    """Reading txt files"""
    with open(file=path, mode="r", encoding='UTF-8') as file_handle:
        content = file_handle.readlines()
        return content


def round_match(hand_1, hand_2):
    """return match's result"""
    if hand_1 == hand_2:
        return result_points["draw"]

    if ((hand_1 == hands["Rock"] and hand_2 == hands["Scissors"]) or
        (hand_1 == hands["Scissors"] and hand_2 == hands["Paper"] or
            (hand_1 == hands["Paper"] and hand_2 == hands["Rock"]))):
        return result_points["lost"]

    return result_points["win"]


def play(matchs: list[str], is_part2: bool):
    """Play function"""
    total_points = 0
    for match in matchs:
        players = match.replace("\n", "").split(" ")
        player_1 = players[total_players["player_1"]]
        player_2 = players[total_players["player_2"]]
        choose_player_1 = player_1_hand[player_1]
        if is_part2:
            next_player2_value = round_ends_as_indicated(
                choose_player_1, player_2)
            choose_player_2 = player_2_hand[next_player2_value]["choose"]
            total_points += player_2_hand[next_player2_value]["point"]
        else:
            choose_player_2 = player_2_hand[player_2]["choose"]
            total_points += player_2_hand[player_2]["point"]

        total_points += round_match(choose_player_1, choose_player_2)
    return total_points


GUESS_HANDS = {
    "Paper": "Z",
    "Rock": "Y",
    "Scissors": "X"
}


def round_ends_as_indicated(player_1, player_2):
    """Guess next hand function"""
    if indicate[player_2] == indicate["Y"]:
        return contrary_hand[player_1]

    if indicate[player_2] == indicate["X"]:
        if player_1 == hands["Paper"]:
            return "X"

        if player_1 == hands["Rock"]:
            return "Z"

        return "Y"

    return GUESS_HANDS.get(player_1)


def main():
    """Main function"""
    data = read_file(
        "advent-of-code-2022/Day 02 - Rock Paper Scissors/input.txt")
    total_part_1 = play(matchs=data, is_part2=False)
    # PART 1
    print("Part 1", total_part_1)
    # PART 2
    total_part_2 = play(matchs=data, is_part2=True)
    print("Part 2", total_part_2)


main()
