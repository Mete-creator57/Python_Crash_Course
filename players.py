
players = ['James','Thomas','Betsy','Mary','John']
print(players[2:])

# Looping Through a Slice
for player in players[:2]:
    print(player.title())

# Copying a List using slice
best_players = players[1:4]
print(best_players)
print(players)

# copying an entire list
fav_players = players[:]



