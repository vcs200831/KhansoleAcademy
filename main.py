import random


def generate_problem():
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    operation = random.choice(['+', '-', '*', '/'])
    return num1, num2, operation


def check_answer(num1, num2, operation, answer):
    if operation == '+':
        expected_answer = num1 + num2
    elif operation == '-':
        expected_answer = num1 - num2
    elif operation == '*':
        expected_answer = num1 * num2
    else:
        expected_answer = num1 / num2

    if answer == expected_answer:
        return True
    else:
        return False


def operation_symbol(operation):
    if operation == '/':
        return '÷'
    else:
        return operation


def main():
    print("Khansole Academy")
    correct_count = 0
    total_problems = 0

    while correct_count < 3:
        num1, num2, operation = generate_problem()
        print(f"What is {num1} {operation_symbol(operation)} {num2}?")
        total_problems += 1

        while True:
            try:
                user_answer = float(input("Your answer: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if check_answer(num1, num2, operation, user_answer):
            print(f"Your answer: {num1} {operation_symbol(operation)} {num2} = {user_answer}")
            correct_count += 1
            print(f"Correct! You've gotten {correct_count} correct in a row.")
        else:
            if operation == '/':
                print("Incorrect. The expected answer is {:.2f}".format(num1 / num2))
            else:
                print(
                    f"Incorrect. The expected answer is {num1} {operation_symbol(operation)} {num2} = {eval(str(num1) + operation + str(num2))}")
            correct_count = 0

        print()

    print(f"Congratulations! You mastered arithmetic. Total problems attempted: {total_problems}")


if __name__ == '__main__':
    main()
