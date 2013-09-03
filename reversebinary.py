#!/usr/bin/env python
# encoding: utf-8

#
# Solution by Wouter Bolsterlee <uws@xs4all.nl>, 2013
#


"""
Reversed Binary Numbers
Problem ID: reversebinary
https://www.spotify.com/us/jobs/tech/reversed-binary/

Yi has moved to Sweden and now goes to school here. The first years of
schooling she got in China, and the curricula do not match completely
in the two countries. Yi likes mathematics, but now... The teacher
explains the algorithm for subtraction on the board, and Yi is bored.
Maybe it is possible to perform the same calculations on the numbers
corresponding to the reversed binary representations of the numbers on
the board? Yi dreams away and starts constructing a program that
reverses the binary representation, in her mind. As soon as the
lecture ends, she will go home and write it on her computer.

Task
Your task will be to write a program for reversing numbers in binary.
For instance, the binary representation of 13 is 1101, and reversing
it gives 1011, which corresponds to number 11.

Input
The input contains a single line with an integer N, 1 ≤ N ≤ 1000000000.

Output
Output one line with one integer, the number we get by reversing the
binary representation of N.

Sample input 1
13

Sample output 1
11

Sample input 2
47

Sample output 2
61
"""


import sys


def reversebinary(n):
    # Simply (ab)use Python's bin() and int() built-ints to format a
    # string, reverse it, and interpret it again! Batteries included! :)
    return int(bin(n)[-1:1:-1], 2)


def test_reversebinary():
    assert reversebinary(13) == 11
    assert reversebinary(47) == 61


def main():
    n = int(sys.stdin.readline().strip())
    assert 1 < n < 1000000000
    print(reversebinary(n))


if __name__ == '__main__':
    main()
