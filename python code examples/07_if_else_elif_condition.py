# required_age = 10

# ali_age = 5

# # question : can ali go to scholl
# if ali_age == required_age:
#     print("Ali ca join school")
# elif ali_age < required_age:
#     print("ali can join school school")
# elif ali_age<= required_age:
#     print("ali join higher secondry school")
    
# else:
#     print("ali can not go to school.")


# Example 01
print("     Title : Weather Conditions   ")

weather = input("Enter your weather condition then i will suggest your activity:  ")
weather = weather.lower() # convert upper letter into lower letter.
print(weather)
if weather == "sunny":
    print("Go for a picnic!")
elif weather == "rainy":
    print("Stay indoor and make a cup of tea and enjoy rainy weather!")
elif weather == 'snowy':
    print("Build a snowman and play with it!")
elif weather == "windy":
    print("Fly a kite and enjoy winding weather!")
else:
    print("Invalid your weather condition!")