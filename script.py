letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}
#print(letter_to_points)
letter_to_points[" "] = 0 

#define a function to return points 
def score_word(word):
  point_total = 0
  for point in word:
    point_total += letter_to_points.get(point, 0)
  return point_total
    #get method gets the value of the letter and if the letter isnt there then the get method adds zero to the total.
brownie_points = score_word("BROWNIE")
#print(brownie_points)
# Brownie string returns 15 

player_to_words = { "player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}
 #player words is a key:value variable
 #items return object in player to words dictionary  
for player, words in player_to_words.items():
  player_points = 0
  # iterating through each letter in word then adding to player points 
  for word in words:
    player_points += score_word(word) 
  player_to_points[player] = player_points

# word nerd is leading by one point
print(player_to_points)
