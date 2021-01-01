authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

# Split by comma
author_names = authors.split(',')
# Get last names
author_last_names = [name.split(' ')[1] for name in author_names]
