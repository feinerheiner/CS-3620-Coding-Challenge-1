# Part 1
# Calculate simple interest by gathering three things (principle, number of years, rate of interest).
# Get user input for p (p = principle).
# Get user input for n (n = number of years).
# Get user input for r (r = rate of interest).
# Convert user inputs p, n, r to int().Links to an external site.
# Calculate the simple interest of p, n, r (multiple p, n, r, and then divide by 100).
# Print out the simple interest value.
print("Part 1")
p = float(input("Enter the principle: "))
n = int(input("Enter the number of years: "))
r = float(input("Enter the rate of interest: "))

if r > 1:
    r /=100

count = 0
while count < n:
    x = p * r
    p += x
    format_p = "{:.2f}".format(p)
    print("$" + str(format_p))
    count += 1
print()

# Part 2
# Create a list of your favorite food items, the list should have a minimum of 5 elements.
# List out the 3rd element in the list.
# Add additional items to the current list and display the list.
# Insert an element named tacos at the 3rd index of the list and print out the list elements.
print("Part 2")
favFoods = ["Pizza", "Sushi", "Watermelon", "Popcorn", "Dr. Pepper"]
print(favFoods[2])
favFoods.append("Yellow Curry")
favFoods.append("Sandwiches")
print(favFoods)
favFoods.insert(3, "Tacos")
print(favFoods)
print()

# Part 3
# Using a for-loop and a range function, print "I am a programmer" 5 times.
# Create a function that displays out the square values of numbers from 1 to 9.
print("Part 3")
for i in range(5):
    print("I am a programmer")
