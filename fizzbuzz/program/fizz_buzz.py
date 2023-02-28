def fizz_buzz(numbers):
    if numbers % 3 == 0 and numbers % 5 == 0:
        return "FizzBuzz"
    if numbers % 3 == 0:
        return "Fizz"
    if numbers % 5 == 0:
        return "Buzz"