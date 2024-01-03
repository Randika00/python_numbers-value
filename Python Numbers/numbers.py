def classify_number(num):
    if num < 0:
        print("The number is negative.")
    elif num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")

# Taking input from the user
number = int(input("Enter a number: "))

# Calling the function to classify the number
classify_number(number)
