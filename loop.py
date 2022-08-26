#range (s, s, s) --> start, stop, step
for i in range (0, 10, 1):
    print(f"The value of i is: {i}")

days_list = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]
for days in days_list:
    print(f"Today is {days}")

for num in range (0, 10+1, 1):
    if num % 2 == 1:
        print(f"The value of num is {num}")
