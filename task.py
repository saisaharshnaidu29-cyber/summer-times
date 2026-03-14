print("type a weather given below")
print("1. sunny 2. rainy 3. cloudy 4. snowy 5. windy")

choice = input("enter the number to know what to wear: ")

if choice == "1":
    print("wear a t-shirt and shorts")
elif choice == "2":
    print("wear a raincoat and carry an umbrella")
elif choice == "3":
    print("wear a light jacket")
elif choice == "4":
    print("wear a heavy coat and boots")
elif choice == "5":
    print("wear a windbreaker and secure loose items")
else:
    print("invalid input, please enter a valid weather condition")