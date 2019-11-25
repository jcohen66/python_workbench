from collections import Counter

new = Counter()

player = {'player1': 7, 'player2': 11}
new.update(player)

print(new)

add_player = {'player3': 12, 'player4': 20}
new.update(add_player)
print(new)

print(len(new))
print(sum(new.values()))