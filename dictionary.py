'''
It is always represent in the form of:
my_dictionary = {"key":"value"}
'''
"""
We need dictionary to overcome the problem exist in list
"""
#For example:
#user_details = ["Manas", "Shrestha", 20, ["English", "Nepali", "Japanese"], 9800000011, ["Burger", "Pizza", "Momo"]]
user_details = {
    "first_name": "Manas",
    "last_name": "Shrestha",
    "age": 20,
    "language_spoken": ["English", "Nepali", "Japanese"],
    "contact": 9800000011,
    "fav_food": ["Burger", "Pizza", "Momo"]
}
print(user_details["first_name"])

for key, value in user_details.items():
    print(f"The key is:{key} and its value is: {value}.")

    
for key in user_details.keys():
    print(f"The key is:{key}.")


for value in user_details.values():
    print(f"The value is: {value}.")