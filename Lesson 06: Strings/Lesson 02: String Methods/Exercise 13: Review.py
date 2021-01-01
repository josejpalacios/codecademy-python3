highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)
# Use split
highlighted_poems_list = highlighted_poems.split(",")
# Print highlighted_poems_list
print(highlighted_poems_list)
# highlighted_poems_list is a list splitted by commas

# Create empty list
highlighted_poems_stripped = []
# Iterate through highlighted_poems_list
for poem in highlighted_poems_list:
  # Strip whitespace
  poem_stripped = poem.strip()
  # Append to highlighted_poems_stripped
  highlighted_poems_stripped.append(poem_stripped)
# Print highlighted_poems_stripped
print(highlighted_poems_stripped)

# Create empty list
highlighted_poems_details = []
# Iterate through highlighted_poems_stripped
for poem in highlighted_poems_stripped:
  # Split using colon
  info = poem.split(":")
  # Append to highlighted_poems_details
  highlighted_poems_details.append(info)

# Create three empty lists
titles = []
poets = []
dates = []

# Iterate through highlighted_poems_details
for info in highlighted_poems_details:
  # Append title info to titles
  titles.append(info[0])
  # Append poet to poets
  poets.append(info[1])
  # Append date to dates
  dates.append(info[2])

# Loop through indices
for index in range(0, len(titles)):
  # Print message
  print("The poem {title} was published by {poet} in {date}.".format(title=titles[index], poet=poets[index], date=dates[index]))
