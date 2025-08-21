from datetime import datetime


routes = {
    'Kochi to Trivandrum': {'time': '08:00 AM', 'price': 300},
    'Kozhikode to Kochi': {'time': '01:30 PM', 'price': 450},
    'Trivandrum to Palakkad': {'time': '10:00 AM', 'pre': 550},
    'Kochi to Bangalore': {'time': '09:00 PM', 'price': 900}
}

route_lst = list(routes.keys())

print("Welcome to Bus Ticket Reservation System")
print("Available routes: ")
print("-----------------------------")
for idx, (route, details) in enumerate(routes.items(), start=1):
    print(f"{idx}: Route: {route} | Time: {details['time']} | Price: ₹{details['price']}")
print("-----------------------------")

# Customer Name
while True:
    customer_name = input("Enter Customer Name: ")
    if customer_name.replace(" ", "").isalpha():
        break
    else:
        print("Invalid Name! Please enter letters only.")

# Age
while True:
    age_str = input("Enter Age: ")
    if age_str.isdigit():
        age = int(age_str)
        break
    else:
        print("Invalid age! Please enter numbers only.")

# Phone number
while True:
    phone_no_str = input("Enter Phone Number: ")
    if phone_no_str.isdigit() and 7 < len(phone_no_str) < 15:
        break
    else:
        print("Invalid phone number! Please enter valid digits.")

# Route selection
while True:
    choice = input("Enter your number of choice of route(1/2/3/4): ")
    if choice.isdigit():
        option=int(choice)
        if 1 <= option <= len(route_lst):
            selected_option = route_lst[option-1]
            break
    else:
        print("Enter a valid choice")

# No of Seats
seats = int(input("Enter your desired number of seats: "))

# Category
while True:
    print("Which category do you belong to:\n1. Student\n2. Senior\n3. General\n")
    cat = input("Enter the category (1/2/3): ")
    if cat in ("1", "2", "3"):
        if cat == "1":
            category = "Student"
        elif cat == "2":
            category = "Senior"
        else:
            category = "General"
        break
    else:
        print("Invalid choice!")

# Discount calculation
if category == "Student":
    discount_rate = 0.15
elif category == "Senior" and age > 60:
    discount_rate = 0.20
else:
    discount_rate = 0.0

departure=routes[selected_option]['time']
price=routes[selected_option]['price']

total_amt = price * seats
discount = total_amt * discount_rate
final_amt = total_amt - discount

booking_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Print ticket
print("-----------------------------")
print("  BUS TICKET - TRAVEL AGENCY  ")
print("-----------------------------")
print("Passenger name  :",customer_name)
print("Phone number    :",phone_no_str)
print("Age             :",age)
print("Category        :",category)
print("Route           :",selected_option)
print("Departure Time  :",departure)
print("Seats booked    :",seats)
print("Booking Time    :",booking_time)

print("------------------------------")
print("Ticket Price:   ",price)
print("Total amount:   ",total_amt)
print("Discount:       ",discount)
print("Final Amount:   ",final_amt)
print("------------------------------")

print("Thank you for booking with us!")
print("Have a safe journey,",customer_name,"!")

# Save ticket to file with timestamp
filename="ticket"+customer_name.replace(" ","")+phone_no_str+".txt"
f1=open(filename,"w")
f1.write("-----------------------------\n")
f1.write("  BUS TICKET - TRAVEL AGENCY \n ")
f1.write("-----------------------------\n")
f1.write("Passenger name: "+customer_name+'\n')
f1.write("Phone number:   "+phone_no_str+'\n')
f1.write("Age:            "+str(age)+'\n')
f1.write("Category:       "+category+'\n')
f1.write("Route:          "+selected_option+'\n')
f1.write("Departure Time: "+departure+'\n')
f1.write("Seats booked:   "+str(seats)+'\n')
f1.write("Booking Time:   "+booking_time+'\n')
f1.write("------------------------------\n")
f1.write("Ticket Price:   "+str(price)+'\n')
f1.write("Total amount:   "+str(total_amt)+'\n')
f1.write("Discount:       "+str(discount)+'\n')
f1.write("Final Amount:   "+str(final_amt)+'\n')
f1.write("------------------------------\n")
f1.write("Thank you for booking with us!\n")
f1.write("Have a safe journey,"+customer_name+"!"+'\n')
f1.close()
