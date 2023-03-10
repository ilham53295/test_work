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
## Alternation Character
Results
```
mac@Macs-MacBook-Pro-3 alternation-characters % python3 -m nose2 -v --with-coverage
test_AAAAA_in_alt_characters (test_alternation_characters.TestAltCharacter) ... ok
test_AAAABBBB_in_alt_characters (test_alternation_characters.TestAltCharacter) ... ok
test_AABBCC_in_alt_characters (test_alternation_characters.TestAltCharacter) ... ok
test_ABCDEFGHIJKLMNOPQRSTUVWXYZabc_in_alt_characters (test_alternation_characters.TestAltCharacter) ... ok
test_BBBBBBB_in_alt_characters (test_alternation_characters.TestAltCharacter) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
Name                                   Stmts   Miss  Cover
----------------------------------------------------------
program/alternation_characters.py          6      0   100%
tests/test_alternation_characters.py      23      0   100%
----------------------------------------------------------
TOTAL                                     29      0   100%
```
## Caesar Cipher
Results
```
mac@Macs-MacBook-Pro-3 Caesar Cipher % python3 -m nose2 -v --with-coverage
test_abcdefghijklmnopqrstuvwxyz_in2_caesarcipher (test_Caeser_Cipher.TestCaesarCipher) ... ok
test_abcdefghijklmnopqrstuvwxyz_in_caesarcipher (test_Caeser_Cipher.TestCaesarCipher) ... ok
test_I_Love_You_in_caesarcipher (test_Caeser_Cipher.TestCaesarCipher) ... ok
test_middle_Outz_in_caesarcipher (test_Caeser_Cipher.TestCaesarCipher) ... ok
test_Never_fall_in_love_in_caesarcipher (test_Caeser_Cipher.TestCaesarCipher) ... ok
test_XO2XO0_in_caesarcipher (test_Caeser_Cipher.TestCaesarCipher) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
Name                          Stmts   Miss  Cover
-------------------------------------------------
program/Caesar_Cipher.py         10      0   100%
tests/test_Caeser_Cipher.py      27      0   100%
-------------------------------------------------
TOTAL                            37      0   100%
```
## Two Character
Results
```
mac@Macs-MacBook-Pro-3 Two-Character % python3 -m nose2 -v --with-coverage
test_give_ac_to_two_character (test_two_character.TestTwoCharacter) ... ok
test_give_asgxcugdsugcewuigcvkejwvcyewbcekwjcgv_to_two_character (test_two_character.TestTwoCharacter) ... ok
test_give_Hello_World_two_character (test_two_character.TestTwoCharacter) ... ok
test_give_ILoveYou_to_Two_Character (test_two_character.TestTwoCharacter) ... ok
test_give_zxcvbnmlkhgfd_to_two_character (test_two_character.TestTwoCharacter) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.004s

OK
Name                          Stmts   Miss  Cover
-------------------------------------------------
program/two_character.py         10      0   100%
tests/test_two_character.py      28      0   100%
-------------------------------------------------
TOTAL                            38      0   100%
```
## Grid Challenge
Results
```
mac@Macs-MacBook-Pro-3 Grid-Challenge % python3 -m nose2 -v --with-coverage
None
test_give_exampleList_1_to_grid (test_grid_challenge.TestGridChallenge) ... ok
test_give_exampleList_2_to_grid (test_grid_challenge.TestGridChallenge) ... ok
test_give_exampleList_3_to_grid (test_grid_challenge.TestGridChallenge) ... ok
test_give_exampleList_4_to_grid (test_grid_challenge.TestGridChallenge) ... ok
test_give_exampleList_5_to_grid (test_grid_challenge.TestGridChallenge) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
Name                           Stmts   Miss  Cover
--------------------------------------------------
program/grid_challenge.py          7      0   100%
tests/test_grid_challenge.py      28      0   100%
--------------------------------------------------
TOTAL                             35      0   100%
```