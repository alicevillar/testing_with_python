# CODE SOURCE: SOFTWARE ARCHITECTURE WITH PYTHON



# Questão 1:

def factorial(n):
if n == 0:
return 1
else:
return n*factorial(n-1)


''' 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

'''

# Questão 2:

# pylint -E stylelint.py = comando p/ buscar errors
# Output => stylelint.py:9:1: E0001: invalid syntax (<unknown>, line 9) (syntax-error)

# pylint -rn stylelint.py = >

# stylelint.py:9:1: E0001: invalid syntax (<unknown>, line 9) (syntax-error)


# OUTPUT => SyntaxError: Missing parentheses in call to 'print'. Did you mean print(encoded)?

