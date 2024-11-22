computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]
index = 0
for c in computer_games:
    print(c)
computer_games_sorted = sorted(computer_games)

for i in computer_games_sorted:
    index += 1
    print(f'{index}. {i}')

