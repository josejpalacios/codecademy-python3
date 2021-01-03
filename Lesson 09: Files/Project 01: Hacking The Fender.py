# ================================
# Reading in the Passwords Section
# ================================
# Task 1: Import csv module
import csv

# Task 2: Create empty list
compromised_users = []

# Task 3: Open file
with open('passwords.csv') as password_file:
  # Task 4: Read csv file into dictionary
  password_csv = csv.DictReader(password_file)
  # Task 5: Iterate through lines from csv file. Save each row.
  for row in password_csv:
    # Create password_row variable
    password_row = row
    # Task 6: Print password_row['Username]
    #print(password_row['Username'])
    # Task 7: Remove print statement. Append usernames to compromised_users
    compromised_users.append(password_row['Username'])

# Task 8: Open new file compromised_users.txt in write-mode
with open('compromised_users.txt', 'w') as compromised_user_file:
  # Task 9: Iterate through compromised_users
  for compromised_user in compromised_users:
    # Task 10: Write each compromised_user to compromised_user_file
    compromised_user_file.write(compromised_user)
# Task 11: Exit out of with block. Finished with section.

# ==========================
# Notifying the Boss Section
# ==========================
# Task 12: Import json module
import json

# Task 13: Open new json file boss_message.json in write-mode
with open('boss-message.json', 'w') as boss_message:
  # Task 14: Create python dictionary to relay message
  boss_message_dict = {
    'recipient': 'The Boss',
    'message': 'Mission Success'
  }
  # Task 15: Write boss_message_dict to boss_message using json.dump()
  json.dump(boss_message_dict, boss_message)

# ===============================
# Scrambling the Password Section
# ===============================
# Task 16: Open new file new_passwords.csv in write-mode
with open('new_passwords.csv', 'w') as new_passwords_obj:
  # Task 17: Create multiline string
  slash_null_sig = """
   _  _     ___   __  ____             
  / )( \   / __) /  \(_  _)            
  ) \/ (  ( (_ \(  O ) )(              
  \____/   \___/ \__/ (__)             
   _  _   __    ___  __ _  ____  ____  
  / )( \ / _\  / __)(  / )(  __)(    \ 
  ) __ (/    \( (__  )  (  ) _)  ) D ( 
  \_)(_/\_/\_/ \___)(__\_)(____)(____/ 
          ____  __     __   ____  _  _ 
   ___   / ___)(  )   / _\ / ___)/ )( \
  (___)  \___ \/ (_/\/    \\___ \) __ (
         (____/\____/\_/\_/(____/\_)(_/
   __ _  _  _  __    __                
  (  ( \/ )( \(  )  (  )               
  /    /) \/ (/ (_/\/ (_/\             
  \_)__)\____/\____/\____/
  """
  # Task 18: Write slash_null_sig to new_passwords_obj
  new_passwords_obj.write(slash_null_sig)
# Task 19: Finished section and project
