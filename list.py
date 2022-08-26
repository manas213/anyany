days_list = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
my_value = days_list[3]
print(my_value)

#append() method --> It is used to insert data into the existing list
#print(days_list)
#days_list.append("someday")
#print(days_list)

print ("Your recent days")
for day in days_list:
    print(day, end=".")

#pop() --> It is used to eject the list element/item from the list and return to us
#print(days_list)
#days_list.pop()
#print(days_list)

# But if you want to remove specific item then:
#days_list.pop(2)
#print(days_list)
