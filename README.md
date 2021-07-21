 <h1>Pylint Challenges</h1>

This repository contains Pylint exercises from CODIO. It was part of Module 3 (“Secure Software Development”) Unit 6 (Using Linters to Support Python Testing) of my MSc in Computer Science at the University of Essex, UK.

<h2>Table of Contents</h2>

<!-- TOC -->
- [1. Lab Question 1](#1-question-1)
- [2. Lab Question 2](#2-question-2)
- [3. Lab Question 3](#3-question-3)
- [4. Lab Question 4](#4-question-4)
- [5. Lab Question 5](#5-question-5)
<!-- /TOC -->


## 1. LAB QUESTION 1

Run the following code: [styleLint.py](https://github.com/alicevillar/pylint_challenges/blob/main/styleLint.py) 
 
### :paperclip: TASK: 

  * What happens when the code is run? 
  * Can you modify this code for a more favourable outcome? 
  * What amendments have you made to the code?
 
### :paperclip: MY SOLUTION:

In this exercise, the code had identation errors. After fixing identation, I changed it for a more favorable out come by checking if the input a positive integer. Note that there are rules for the factorial calculation that we need to check. Thus, I added these checks:
* n must be an integer
* n must be greater or equal to 1 (n≥1)
Finally, I added the input() function to read the value entered by the user, called the function and printed the result. 

 | Click here to see the solution for Lab Question 1 | [stylelint_done.py](https://github.com/alicevillar/pylint_challenges/blob/main/stylelint_done.py) 

### :round_pushpin: Three ways to calculate factorial

After doing Lab Question 1, I wanted to go further so I tested three ways to calculate factorial: 

* a) Using a function from the math module: The math library has a function to calculate factorial and the code only take one line. 
* b) Using for loop:
* c) Using recursion.  

| Click here to see the solution | [calculating_factorial_3ways.py](https://github.com/alicevillar/pylint_challenges/blob/main/calculating_factorial_3ways.py) 


## 2. LAB QUESTION 2

pip install pylint, then run pylint on [pylintTest.py](https://github.com/alicevillar/pylint_challenges/blob/main/pylintTest.py):

### :paperclip: TASK: 

  * Review each of the code errors returned. Can you correct each of the errors identified by pylint? 
  * Before correcting the code errors, save the pylintTest.py file with a new name (it will be needed again in the next question).
 
### :paperclip: MY SOLUTION:

I have corrected all the errors identified by pylist and finally received this response in the terminal: 

```
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.50/10, +0.50)
```

I saved the new code in the file named pylint_test_done.py. Please click the linkk below to see it. 

 | Click here to see the solution to Lab Question 2 | [pylint_test_done.py](https://github.com/alicevillar/pylint_challenges/blob/main/pylint_test_done.py)   

 
## 3. LAB QUESTION 3
 
pip install flake8
Run flake8 on [pylintTest.py](https://github.com/alicevillar/pylint_challenges/blob/main/pylintTest.py)

### :paperclip: TASK: 

  * Question A: Review the errors returned. In what way does this error message differ from the error message returned by pylint?
  * Question B: Run flake8 on [metricTest.py](https://github.com/alicevillar/pylint_challenges/blob/main/metricTest.py). Can you correct each of the errors returned by flake8? What amendments have you made to the code?
 
### :paperclip: MY SOLUTION TO QUESTION A:

PyLint has a lot more types of checks than flake8. When comparing Pylint vs flake8, the [Slant community](https://www.slant.co/versus/12630/12632/~pylint_vs_flake8) recommends Pylint for most people. In the question“What are the best Python code linters?” Pylint is ranked 1st while flake8 is ranked 2nd. The most important reason people chose Pylint is: Pylint gives very detailed reports of your code. Pylint prefixes each of the problem areas with a R, C, W, E, or F, meaning:

* [R]efactor for a “good practice” metric violation
* [C]onvention for coding standard violation
* [W]arning for stylistic problems, or minor programming issues
* [E]rror for important programming issues (i.e. most probably bug)
* [F]atal for errors which prevented further processing

### :paperclip: MY SOLUTION TO QUESTION B:

After running pylint multiple times on my file metric_test_done.py, I finally reached the score 10.00. Here is the response shown in the terminal:

```
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

Please click the link below to see the my code after all the corrections suggested by pylint: 

| Lab Question 3B | [metric_test_done.py](https://github.com/alicevillar/pylint_challenges/blob/main/metric_test_done.py)   

 
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
 
 
 
