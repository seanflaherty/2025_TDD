#from  ..src.fizzbuzz import divide_by_three
#from fizzbuzz import divide_by_three
from ..src.fizzbuzz import divide_by_three

# 	1. If the integer is divisible by 3, return the string "Fizz."
def test_divide_by_three():
    assert divide_by_three(9) == "Fizz", "Expected 9 should return Fizz."
    #assert divide_by_three(8) == "", "Expected empty string."

# 	2. If the integer is divisible by 5, return the string "Buzz."
# 	3. If the integer is divisible by 3 and 5, return the string "FizzBuzz."
# If the integer is not divisible by 3 and 5, return the string "Not FizzBuzz."