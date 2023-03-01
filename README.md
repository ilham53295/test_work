# Python Unittest Homework
## Prime_numbers
Results
```
mac@Macs-MacBook-Pro-3 prime_number % python3  -m unittest -v tests/test_number_utils.py
test_give_13_17_23_is_prime (tests.test_number_utils.PrimeListTest) ... ok
test_give_2_3_is_prime (tests.test_number_utils.PrimeListTest) ... ok
test_give_4_10_is_Not_prime (tests.test_number_utils.PrimeListTest) ... ok
test_give_4_5_6_is_not_prime (tests.test_number_utils.PrimeListTest) ... ok
test_give_n1_0_1_is_Not_prime (tests.test_number_utils.PrimeListTest) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```
## FizzBuzz Test
Results
```
mac@Macs-MacBook-Pro-3 fizzbuzz % python3 -m unittest -v tests/test_fizz_buzz.py   
test_15_is_a_fizz_buzz (tests.test_fizz_buzz.FizzBuzzTest) ... ok
test_18_is_fizz (tests.test_fizz_buzz.FizzBuzzTest) ... ok
test_30_is_fizz_Buzz (tests.test_fizz_buzz.FizzBuzzTest) ... ok
test_3_is_a_fizz (tests.test_fizz_buzz.FizzBuzzTest) ... ok
test_5_is_a_buzz (tests.test_fizz_buzz.FizzBuzzTest) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```
## starcase
Results
```
mac@Macs-MacBook-Pro-3 starcase % python3 -m unittest -v tests/test_starcase.py
test_give_2_with_hash_should_be_hh (tests.test_starcase.TestStarcase) ... ok
test_give_5_with_hash_should_be_hh (tests.test_starcase.TestStarcase) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
## CatAndMouse
Results
```
mac@Macs-MacBook-Pro-3 cat_and_mouse % python3 -m unittest -v tests/test_cat_and_mouse.py
test_1_2_3_in_CatMouse (tests.test_cat_and_mouse.TestCatsMouse) ... ok
test_1_2_4_in_CatMouse (tests.test_cat_and_mouse.TestCatsMouse) ... ok
test_1_3_2_in_CatMouse (tests.test_cat_and_mouse.TestCatsMouse) ... ok
test_3_3_3_in_CatMouse (tests.test_cat_and_mouse.TestCatsMouse) ... ok
test_8_3_4_in_CatMouse (tests.test_cat_and_mouse.TestCatsMouse) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```
## Funny String
Results
```
mac@Macs-MacBook-Pro-3 funny-string % python3 -m nose2 -v --with-coverage                       
test_2_in_FunnyString (test_FunnyString.TestFunnyString) ... ok
test_abcd_in_FunnyString (test_FunnyString.TestFunnyString) ... ok
test_acxz_in_FunnyString (test_FunnyString.TestFunnyString) ... ok
test_bvxz_in_FunnyString (test_FunnyString.TestFunnyString) ... ok
test_nbvc_in_FunnyString (test_FunnyString.TestFunnyString) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
Name                        Stmts   Miss  Cover
-----------------------------------------------
program/FunnyString.py          9      0   100%
tests/test_FunnyString.py      23      0   100%
-----------------------------------------------
TOTAL                          32      0   100%
```