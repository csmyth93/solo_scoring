def get_names():
    names = []
    while True:
        name = input("Enter players name: ")
        if name != 'done':
            print(f'{name} added to the list of players')
            names.append(name)
            continue
        else:
            break
    return names


def get_player_scores(players):
    for player in players:
        scores = []
        while True:
            score = input(f"What are {player}'s final cards? ")
            if score != 'end':
                scores.append(score)
                continue
            else:
                break
    return scores


if __name__ == '__main__':
    players = get_names()
    print(players)
    scores = get_player_scores(players)
    print(scores)
