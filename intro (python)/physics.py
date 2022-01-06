# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c = 3 * 10 ** 8
train_force = 0

# Write your code below: 
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  print(c_temp)
f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  print(f_temp)
c0_in_fahrenheit = c_to_f(0)

def get_force(mass, acceleration):
  train_force = mass * acceleration
  print('The GE train supplies ' + str(train_force) + ' Newtons of force.')
get_force(train_mass, train_acceleration)

def get_energy(mass, c):
  return mass * c ** 2
bomb_energy = get_energy(bomb_mass, c)
print('A 1kg bomb supplies ' + str(bomb_energy) + ' Joules.')

def get_work(mass, acceleration, distance):
  work = mass * distance * acceleration
  print('The GE train does ' + str(work) + ' Joules of work over Y meters.')
train_work = get_work(train_mass, train_acceleration, train_distance)
