print("Welcome to the tip calculator!")

# Get bill amount
total_bill = input("What was the total bill?\n")

# Get desired tip
desiredtip = input("How much tip would you like to give? 10, 12, or 15 percent?\n")

# Calculate total bill with tips
desiredtip_multiple = int(desiredtip) / 100
total_bill_with_tips = int(total_bill) * (1 + desiredtip_multiple)

# Calculate per pax amount owed
total_pax = input("How many people to split the bill?\n")
per_pax_total = round((total_bill_with_tips / int(total_pax)),2)

# Show what each pax owes
print(f"Each person should pay: \n${per_pax_total}")

# Example Input
# ```
# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7
# ```

# # Example Output
# ```
# Each person should pay: $19.93
# ```

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.