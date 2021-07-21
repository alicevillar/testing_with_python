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
### Questions: 

  * What happens when the code is run? 
  * Can you modify this code for a more favourable outcome? 
  * What amendments have you made to the code?
 
 
### Answer:

In this exercise, the code had identation errors. After fixing identation, I changed it for a more favorable out come by checking if the input a positive integer. Note that there are rules for the factorial calculation that we need to check. Thus, I added these checks:
* n must be an integer
* n must be greater or equal to 1 (n≥1)
Finally, I added the input() function to read the value entered by the user, called the function and printed the result. 

 | Click here to see the solution for Lab Question 1 | [stylelint.py](https://github.com/alicevillar/pylint_challenges/blob/main/stylelint.py) 

### :arrow_forward: Three ways to calculate factorial

After doing Lab Question 1, I wanted to go further so I tested three ways to calculate factorial: 

* a) Using a function from the math module: The math library has a function to calculate factorial and the code only take one line. 
* b) Using for loop:
* c) Using recursion.  

| Click here to see the solution | [calculating_factorial_3ways.py](https://github.com/alicevillar/pylint_challenges/blob/main/calculating_factorial_3ways.py) 


## 2. Lab Question 2

```
pip install pylint
Run pylint on pylintTest.py

=> Review each of the code errors returned. 
=> Can you correct each of the errors identified by pylint? 
=> Before correcting the code errors, save the pylintTest.py file with a new name (it will be needed again in the next question).
```
 | Lab Question 1 | [Solution](https://github.com/alicevillar/Python_Lab_Challenges/blob/main/lists/lists_exercise1.py)   


  Note that the factorial function is defined only for positive integers;                   
 pylint -E stylelint.py = comando p/ buscar errors                                          
 Output => stylelint.py:9:1: E0001: invalid syntax (<unknown>, line 9) (syntax-error)       
                                                                                             
  pylint -rn stylelint.py = >                                                                
                                                                                             
 stylelint.py:9:1: E0001: invalid syntax (<unknown>, line 9) (syntax-error)                 
                                                                                             
 OUTPUT => SyntaxError: Missing parentheses in call to 'print'. Did you mean print(encoded)?
 
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
 
 
 
