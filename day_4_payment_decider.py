names_string="Harry, James, Jack"
names = names_string.split(", ")
# names_string contains the input values provided.
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
random_selection=random.randint(0,len(names)-1)
print(f"{names[random_selection]} is going to buy the meal today!")