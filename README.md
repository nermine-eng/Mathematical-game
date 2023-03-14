# Mathematical-game

Problem 1 : Play With Numbers

Some numbers have funny properties.

For example:


89 --> 8¹ + 9² = 89 * 1

695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n.

In other words Is there an integer k such as


 (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
 

If it is the case we will return k, if not return -1.

Note: n and p will always be given as strictly positive integers.

Example


digPow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
digPow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
digPow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
digPow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Problem 2 : To Binary

Given a non-negative integer n, write a function to_binary/ToBinary which returns that number in a binary format.


to_binary(1)  # should return 1 
to_binary(5)  # should return 101
to_binary(11) # should return 1011

Problem 3 : A to Z

Given a string as input, return a new string with each letter pushed to the right by its respective index in the alphabet.

We all know that A is a slow and Z is a fast letter. This means that Z gets shifted to the right by 25 spaces, A doesn't get shifted at all, and B gets shifted by 1 space.

You can assume the following things about your input:

    It will only contain uppercase letters from A to Z, no whitespaces or punctuation
    Input strings will not exceed 100 characters (although your output string might!)

Note that if 2 or more letters fall onto the same space after shifting, the latest character will be used. For example: "BA" -> " A"

Examples


"AZ"   -->  "A                         Z"
"ABC"  -->  "A B C"
"ACE"  -->  "A  C  E"
"CBA"  -->  "  A"
"HELLOWORLD"  -->  "     E H    DLL   OLO   R  W"

Problem 4 : Hangman

Hangman is a game where you must guess letters of the alphabet to complete a word given the length. You have decided you want to impress your friends with your hangman skills and create a program given a list of predefined words that can complete any hangman guess first time!
Task

    You must implement the Machine class that takes a word list and returns a player class that takes a length of the word you must guess.

    You must then make guesses returning letters of the alphabet to complete the word within 11 failed guesses, as a response you will receive a string representation of the letters found and the letters remaining unknown.

Examples


word: printable

guess: a
response: _____a___

guess: b
response: _____a___

guess: p
response: p____a___

Problem 5 : Infinite Sequence

Consider the following array:

[1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789, 12345678910, 1234567891011...]

If we join these blocks of numbers, we come up with an infinite sequence which starts with 112123123412345123456.... The list is infinite.

You will be given an number (n) and your task will be to return the element at that index in the sequence, where 1 ≤ n ≤ 10^18. Assume the indexes start with 1, not 0.

For example:


solve(1) = 1, because the first character in the sequence is 1. There is no index 0. 
solve(2) = 1, because the second character is also 1.
solve(3) = 2, because the third character is 2.

Problem 6 : The dots and parentheses

The following task has two parts.

    First you must figure out the principle behind the following encoding of natural numbers.
    The table below displays the encoding of the numbers from 0 to 11.

Number 	Code
0 	'.'
1 	'()'
2 	'(())'
3 	'(.())'
4 	'((()))'
5 	'(..())'
6 	'(()())'
7 	'(...())'
8 	'((.()))'
9 	'(.(()))'
10 	'(().())'
11 	'(....())'

Once you understand how the numbers are encoded, write a program which encodes a given natural number and return it as a string.

Values from 0 to 10000 will be checked
