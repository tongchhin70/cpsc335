#Design an algorithm that returns the index of the preferred starting city.
#By: Group 10 - Tristan Caluag, Tong Chhin, Kenneth Cho, Kenneth Ly

distance= [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10


def fuel_distance(dist, gas, mpg):
  city = 0 
  balance = 0
  
  for i in range(len(dist)):
    net_fuel = (gas[i] * mpg) - dist[i] # Calculate the net fuel after reaching the next city
    
    balance += net_fuel # Update the balance with the net fuel after reaching the next city
    
    if balance < 0: # If the balance is negative, it means we cannot reach the next city from the current starting city
      balance = 0 # Reset the balance to 0 for the next starting city
      city = i + 1 # Move to the next city as the new starting point

  return city

preferred_city = fuel_distance(distance, fuel, mpg)

print(f"Preferred Start City:{preferred_city}\n")



