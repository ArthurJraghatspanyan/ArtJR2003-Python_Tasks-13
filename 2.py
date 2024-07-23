#Ստեղծել ծրագիր, որը կներառի օգտատերերի տվյալների ներմուծումը, պահպանումը բառարանում և ցուցակում, ապա ցույց կտա օգտատերերին ըստ ներմուծված անվան(“Not found”, եթե այդպիսի օգտատեր գոյություն չունի)։ Յուրաքանչյուր օգտատեր պետք է ունենա հետևյալ դաշտերը՝ ID, անուն, ազգանուն, Էլ. փոստ, գաղտնաբառ և հեռախոսահամար:

users = {}

count = int(input("Enter count of users: "))

for i in range(count):
    user_id = int(input("Enter ID: "))
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    phone_number = input("Enter phone number: ")
    
    users[user_id] = {
        'ID': user_id,
        'Name': name,
	'Surname': surname,
        'Email': email,
        'Password': password,
        'Phone Number': phone_number
    }

search_name = input("Enter name you want to search: ")
found_user = "Not found"
for user in users.values():
    if user['Name'] == search_name:
        found_user = user
        break

print(found_user)

for user_id, user_data in users.items():
    print(f"ID: {user_id}, Name: {user_data['Name']}, Surname: {user_data['Surname']}, Email: {user_data['Email']}, Password: {user_data['Password']}, Phone Number: {user_data['Phone Number']}")
