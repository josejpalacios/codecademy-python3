tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}
# Create empty dictionary
spread = {}
# Pop 13 and assign it to past key in spread
spread["past"] = tarot.pop(13)
# Pop 22 and assign it to present key in spread
spread["present"] = tarot.pop(22)
# Pop 10 and assign it to future key in spread
spread["future"] = tarot.pop(10)
# Iterate through spread items
for key, value in spread.items():
  # Print message
  print("Your {key} is the {value} card.".format(key=key, value=value))
