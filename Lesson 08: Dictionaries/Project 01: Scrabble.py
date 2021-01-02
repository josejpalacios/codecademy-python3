# Starting code
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# ===================================
# Build your Point Dictionary Section
# ===================================
# Task 1: Create dictionary using list comprehension and zip
letter_to_points = {letters:points for letters, points in zip(letters, points)}

# Task 2: Add key value pair to dictionary
letter_to_points[" "] = 0

# ====================
# Score a Word Section
# ====================
# Task 3: Write function score_word
def score_word(word):
  # Task 4: Create variable point_total
  point_total = 0
  # Task 5: Iterate through word and add point values to point_total
  for letter in word:
    # Add point value from dictionary to point_total. Default to 0 if letter is not in dictionary
    # Task 15: Extra - Make input work with lowercase letters
    point_total += letter_to_points.get(letter.upper(), 0)
  # Task 6: Return point_total
  return point_total
# Task 7: Test score_word function with BROWNIE
brownie_points = score_word("BROWNIE")
# Task 8: Print brownie_points. Should print 15.
print(brownie_points)

# ====================
# Score a Game Section
# ====================
# Task 9: Create dictionary
player_to_words ={
  "player1": ["BLUE", "TENNIS", "EXIT"],
  "wordNerd": ["EARTH", "EYES", "MACHINE"],
  "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
  "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

# Task 10: Create empty dictionary
player_to_points = {}

# Task 11: Iterate through items in player_to_words. Create player_points and set to 0.
for player, words in player_to_words.items():
  # Create variable
  player_points = 0
  # Task 12: Iterate through words and add value of word using score_word
  for word in words:
    # Add value of word to player_points
    player_points += score_word(word)
  # Task 13: Add key value pair to player_points using player and player_points
  player_to_points[player] = player_points
# Task 14: Print player_to_points. wordNerd should be winning by 1 point.
print(player_to_points)

# ===================================
# Ideas for Further Practice! Section
# ===================================
# Task 15: Extra Functions
# - update_point_totals: Nested loop from Task 11 to Task 13 to be called when a word is played
# - play_word: Takes a player and word and adds word to player's list of words
# Able to score lowercase inputs as well - Code is labeled as Task 15: Extra above.
# Write update_point_totals function
def update_point_totals():
  # Iterate through player_to_words
  for player, words in player_to_words.items():
    # Create variable
    player_points = 0
    # Iterate through words
    for word in words:
      # Add value of word to player_points
      player_points += score_word(word)
    # Add key value pair to player_points using player and player_points
    player_to_points[player] = player_points

# Write play_word function
def play_word(player, word):
  # Append word to players list of words
  player_to_words.get(player).append(word)
  # Call update_point_totals
  update_point_totals()
  # Print player_to_points
  print(player_to_points)

# Test play_word function
play_word("player1", "COOKIE")
# Test play_word function
play_word("wordNerd", "Water")
