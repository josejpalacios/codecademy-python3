# not (4 + 5 <= 9)
statement_one = False

# not (8 * 2) != 20 - 4
statement_two = True

# Finish graduation_reqs function
def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  # Added check for gpa >= 2.0 and not credits >= 120
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  # Added check for not gpa >= 2.0 and credits >= 120
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  # Added check for not gpa >= 2.0 and not credits >= 120
  if not (gpa >= 2.0) and not (credits >= 120):
    return "You do not meet either requirement to graduate!"
