 <h1>Pylint Challenges</h1>

This repository contains Pylint exercises from CODIO. It was part of Module 3 (“Secure Software Development”) Unit 4 (Exploring Programming Language Concepts) of my MSc in Computer Science at the University of Essex, UK.

<h2>Table of Contents</h2>

<!-- TOC -->
- [1. Lab Question 1](#1-question-1)
- [2. Lab Question 2](#2-question-2)
- [3. Lab Question 3](#3-question-3)
- [4. Lab Question 4](#4-question-4)
- [5. Lab Question 5](#5-question-5)
<!-- /TOC -->


## 1. Lab Question 1

Run styleLint.py: 
```
def factorial(n):
""" Return factorial of n """
if n == 0:
return 1
else:
return n*factorial(n-1)
```
### :paperclip: Task: 

  * What happens when the code is run? 
  * Can you modify this code for a more favourable outcome? 
  * What amendments have you made to the code?
 
 
### :paperclip: Answer:

In this exercise, the code had identation errors. After fixing identation, I changed it for a more favorable out come by checking if the input a positive integer. Note that there are rules for the factorial calculation that we need to check. Thus, I added these checks:
* n must be an integer
* n must be greater or equal to 1 (n≥1)
Finally, I added the input() function to read the value entered by the user, called the function and printed the result. 

 | Click here to see the solution for Lab Question 1 | [stylelint.py](https://github.com/alicevillar/pylint_challenges/blob/main/stylelint.py) 

### :round_pushpin: Three ways to calculate factorial

After doing Lab Question 1, I wanted to go further so I tested three ways to calculate factorial: 

* a) Using a function from the math module: The math library has a function to calculate factorial and the code only take one line. 
* b) Using for loop:
* c) Using recursion.  

| Click here to see the solution | [calculating_factorial_3ways.py](https://github.com/alicevillar/pylint_challenges/blob/main/calculating_factorial_3ways.py) 


## 2. Lab Question 2

pip install pylint, then run pylint on pylintTest.py:
```
 3  import string
 4
 5  shift = 3
 6  choice = raw_input("would you like to encode or decode?")
 7  word = (raw_input("Please enter text"))
 8  letters = string.ascii_letters + string.punctuation + string.digits
 9  encoded = ''
10  if choice == "encode":
11      for letter in word:
12          if letter == ' ':
13              encoded = encoded + ' '
14          else:
15              x = letters.index(letter) + shift
16              encoded=encoded + letters[x]
17  if choice == "decode":
18      for letter in word:
19          if letter == ' ':
20              encoded = encoded + ' '
21          else:
22              x = letters.index(letter) - shift
23              encoded = encoded + letters[x]
24
25  print encoded

```

### :paperclip: Task: 

  * Review each of the code errors returned. Can you correct each of the errors identified by pylint? 
  * Before correcting the code errors, save the pylintTest.py file with a new name (it will be needed again in the next question).
 
### :paperclip: Answer:

I have corrected all the errors identified by pylist and finally received this response in the terminal: "Your code has been rated at 10.00/10 (previous run: 9.50/10, +0.50)". I saved the new code in the file named pylint_test_done.py. Please click the linkk below to see it: 

 | Click here to see the solution to Lab Question 2 | [pylint_test_done.py](https://github.com/alicevillar/pylint_challenges/blob/main/pylint_test_done.py)   

 
## 3. Lab Question 3

```
pip install flake8
Run flake8 on pylintTest.py

=> Review the errors returned. In what way does this error message differ from the error message returned by pylint?
=> Run flake8 on metricTest.py. Can you correct each of the errors returned by flake8? What amendments have you made to the code?
```
 | Lab Question 1 | [Solution](https://github.com/alicevillar/Python_Lab_Challenges/blob/main/lists/lists_exercise1.py)   

 
## 4. Lab Question 4

```
pip install mccabe
Run mccabe on sums.py. What is the result?
Run mccabe on sums2.py. What is the result?

=> What are the contributors to the cyclomatic complexity in each piece of code?
```
 | Lab Question 1 | [Solution](https://github.com/alicevillar/Python_Lab_Challenges/blob/main/lists/lists_exercise1.py)   

 
#### Lab Question 5 (e-portfolio entry)

```
From Section 5 of the Firdaus et al (2014) reading, select a test technique from the following categories:

* Specification-based techniques
* Structure-based techniques
* Experience-based techniques
<br>

=> Discuss the scenario(s) in which each technique would be important to be used.
```
 | Lab Question 1 | [Solution](https://github.com/alicevillar/Python_Lab_Challenges/blob/main/lists/lists_exercise1.py)  
 
 
 
