# Create applicant_selector function
def applicant_selector(gpa, ps_score, ec_count):
  # If:
  #    gpa >= 3.0 and ps_score >= 90 and ec_count >= 3
  if (gpa >= 3.0) and (ps_score >= 90) and (ec_count >= 3):
    # Return message
    return "This applicant should be accepted."
  # Else if:
  #    gpa >= 3.0 and ps_score >= 90 and not ec_count >= 3
  elif (gpa >= 3.0) and (ps_score >= 90) and not (ec_count >= 3):
    # Return message
    return "This applicant should be given an in-person interview."
  # Else
  else:
    # Return message
    return "This applicant should be rejected."
