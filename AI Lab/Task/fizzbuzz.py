def fizz_buzz():
    a, b = 1, 2
    print("1")
    print("2")
    while True:
        next_number = a + b
        print(f"\nNext number: {next_number}")
        if next_number % 3 == 0 and next_number % 5 == 0:
            correct_answer = "Fizz Buzz"
        elif next_number % 3 == 0:
            correct_answer = "Fizz"
        elif next_number % 5 == 0:
            correct_answer = "Buzz"
        else:
            correct_answer = ""
        
        user_input = input("Enter 'Fizz', 'Buzz', 'Fizz Buzz', or press Enter: ")
        if user_input.lower() == correct_answer.lower() or (correct_answer == "" and user_input == ""):
            print("Correct!")
            a, b = b, next_number
        else:
            print("Game Over!")
            print(f"The correct answer was {correct_answer}.")
            break

fizz_buzz()