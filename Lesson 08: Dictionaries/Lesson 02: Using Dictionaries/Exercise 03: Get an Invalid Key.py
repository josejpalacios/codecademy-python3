# Key not in dictionary results in KeyError: 'Landmark 81'

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"], "energy": "Not a Zodiac element"}
# KeyError - Fixed by adding key energy
print(zodiac_elements["energy"])
