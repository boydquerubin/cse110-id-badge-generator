# badge generator
first_name = input("Enter your first name: ").title()
last_name = input("Enter your last name: ").upper()
email = input("Enter your email address: ")

phone_number = input("Enter your phone number: ")
formatted_phone_number = f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"

job_title = input("Enter your job title: ").title()
id_number = int(input("Enter your ID Number: "))
hair_color = input("Enter your hair color: ").title()
eye_color = input("Enter your eye color: ").title()
month = input("Enter current month: ").title()
training = input("Are you in training, 'Yes' or 'No': ").title()

print("\n" * 20)
print("The ID Card is: ")
print("-" * 40)
print(f"{last_name}, {first_name}")
print(f"{job_title}")
print(f"ID: {id_number}\n")
print(f"{email}")
print(f"{formatted_phone_number}\n")
print(f"Hair: {hair_color:<15} Eyes: {eye_color}")
print(f"Month: {month:<15} Training: {training}")
print("-" * 40)