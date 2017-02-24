print("------------------------")
print("| Cost plan for a trip |")
print("------------------------\n\n")

bus = float(input("Cost for the bus: "))
hotel = float(input("Cost for the hotel per participant: "))
events = float(input("Total costs for all events: "))
num_pa = float(input("Number of participants: "))

total = bus + events + (hotel * num_pa)
total_p_pa = total / num_pa

print("\nTotal expenses for the trip:          $%.2f USD." % total)
print("Total expenses for every participant: $%.2f USD." % total_p_pa)
