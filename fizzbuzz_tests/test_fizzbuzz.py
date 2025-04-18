# imports
from ..src.fizzbuzz import divide_by_three, divide_by_five, divide_by_three_and_five

# 	1. If the integer is divisible by 3, return the string "Fizz."
def test_divide_by_three():
    assert divide_by_three(9) == "Fizz", "Expected 9 should return Fizz."
    assert divide_by_three(8) == "", "Expected empty string."

# 	2. If the integer is divisible by 5, return the string "Buzz."
def test_divide_by_five():
    assert divide_by_five(15) == "Buzz", "Expected 15 should return Buzz."
    assert divide_by_five(8) == "", "Expected empty string."

# 	3. If the integer is divisible by 3 and 5, return the string "FizzBuzz."
def test_divide_by_three_and_five():
    assert divide_by_three_and_five(15) == "FizzBuzz", "Expected 15 should return FizzBuzz."
    assert divide_by_five(8) == "", "Expected empty string."
#   4. If the integer is not divisible by 3 and 5, return the string "Not FizzBuzz."