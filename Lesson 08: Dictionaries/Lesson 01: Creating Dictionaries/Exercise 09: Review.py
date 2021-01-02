songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# Create dictionary using list comprehension
plays = {songs: playcounts for songs, playcounts in zip(songs, playcounts)}
# Print plays
print(plays)
# Add key value
plays["Purple Haze"] = 1
# Update Respect value
plays["Respect"] = 94
# Create dictionary
library = {
  "The Best Songs": plays,
  "Sunday Feelings": {}
}
# Print library
print(library)
