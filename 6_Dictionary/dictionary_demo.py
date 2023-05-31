user_details={
    "name": "Mr.Kevin",
    "email": "test@mail.com",
    "password": 123456,
    "discount": 10.5,
    "amount":[12, 20, 33],
    "favorite_color": ['green', 'yellow', 'orange'],
    "address" : {
        "present_address" :{
            "street": "123/A/7",
            "house_number": 123
        },
        "permanent_address" :{
            "street": "11/B",
            "house_number": 454
        }
    }
}

name = user_details["name"]
print(name)

print(user_details["address"]["permanent_address"]["house_number"])


for key , value in user_details.items():
    print(key, value)

# Create a list with all keys
all_key_list = []
for key , value in user_details.items():
    all_key_list.append(key)
print(all_key_list)