# Default given values
train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

# ===============================
# Turn up the Temperature Section
# ===============================
# Task 1: Create f_to_c function
def f_to_c(f_temp):
  # Convert fahrenheit to celsius store value in c_temp
  c_temp = (f_temp - 32) * 5/9
  # Return c_temp
  return c_temp

# Task 2: Test function with 100 F
f100_in_celsius = f_to_c(100)

# Task 3: Create c_to_f function
def c_to_f(c_temp):
  # Convert celsius to fahrenheit store value in f_temp
  f_temp = c_temp * (9/5) + 32
  # Return f_temp
  return f_temp

# Task 4: Test function with 0 C
c0_in_fahrenheit = c_to_f(0)

# =====================
# Use the Force Section
# =====================
# Task 5: Create get_force function
def get_force(mass, acceleration):
  # Return mass * acceleration
  return mass * acceleration

# Task 6: Test function with train_mass and train_acceleration
train_force = get_force(train_mass, train_acceleration)

# Task 7: Print message
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Task 8: Create get_energy function
def get_energy(mass, c=3*10**8):
  # Return mass * c squared
  return mass * c**2

# Task 9: Test function with bomb_mass and default value of c
bomb_energy = get_energy(bomb_mass)

# Task 10: Print message
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# ===================
# Do the Work Section
# ===================
# Task 11: Create get_work function
def get_work(mass, acceleration, distance):
  # Get force using get_force
  force = get_force(mass, acceleration)
  # Return force * distance
  return force * distance

# Task 12: Test function with train_mass, train_acceleration, and train_distance
train_work = get_work(train_mass, train_acceleration, train_distance)

# Task 13: Print message
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
