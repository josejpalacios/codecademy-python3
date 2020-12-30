# Starting code
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

# =========================
# Create Some Lists Section
# =========================
# Task 1: Create list called subjects
subjects = ['physics', 'calculus', 'poetry', 'history']

# Task 2: Create list called grades
grades = [98, 97, 85, 88]

# Task 5
subjects.append("computer science")
grades.append("100")

# Task 3: Create zip object using subjects and grades. Convert zip to list
gradebook = list(zip(subjects, grades))

# Task 6
gradebook.append(('visual arts', 93))

# Task 4: Print gradebook
print(gradebook)

# =========================
# Add More Subjects Section
# =========================
# Task 5: Append to subjects and grades before creating gradebook.
# Code is above

# Task 6: Append to gradebook before printing out.
# Code is above

# ==========================
# One Big Gradebook! Section
# ==========================
# Task 7: Create list with items from both gradebook lists
full_gradebook = gradebook + last_semester_gradebook
