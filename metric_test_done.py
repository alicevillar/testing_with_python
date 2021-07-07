# CODE SOURCE: SOFTWARE ARCHITECTURE WITH PYTHON

"""
2 Module metricTest.py
3
4 Metric example - Module which is used as a testbed for static
checkers.
5 This is a mix of different functions and classes doing
different things.
7 """

def fn_function(num_1,num_2):
    """ Function fn that return the sum of x and y"""
    return num_1 + num_2

def optimal_route(expected_time, start_time,favorite_route='SBS1K', favorite_option='bus'):
    """  find_optimal_route_to_my_office_from_home """
    distance = (expected_time - start_time).total_seconds() / 60.0
    if distance <= 30:
        return 'car'

    # If d>30 but <45, first drive then take metro
    if distance > 30:
        return ('car', 'metro')

    # If d>45 there are a combination of optionsWriting Modifiable and Readable Code
    # First volvo,then connecting bus
    if 45 < distance < 60:
        return ('bus:335E', 'bus:connector')
    # Might as well go by normal bus # return random.choice(('bus:330','bus:331',':'))

    return ':'.join((favorite_option, favorite_route))

class CobraClass():
    """ A class which does almost nothing """
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def f_function(self):
        """ Function f to return num_2 """
        return self.num_2

    def g_function_cobra(self):
        """ Function g to check """
        if self.num_1 > self.num_2:
            return self.num_1 + self.num_2
        return self.num_1 + self.num_2

class DominoClass(CobraClass):
    """ D class """
    def __init__(self,num_1, num_2):
        super().__init__(num_1, num_2)
        self.num_1 = num_1
        self.num_2 = num_2

    def f_function(self):
        """ Function that return the value of y + x """
        if self.num_1 > self.num_2:
            return self.num_1 - self.num_2
        return self.num_1 + self.num_2

    def g_function_domino(self):
        """ Function that return the value of y - x """
        if self.num_1 > self.num_2:
            return self.num_1 + self.num_2
        return self.num_2 - self.num_1

# Your code has been rated at 10.00/10 :)


# parentesis, indentation, importing, deleted "Chapter 2 ",
# changed the order expected_time & start_time
# deleted import random because was not being used
# deleted unecessary "else" in the last function
# name of the last function has to be a string
# In the last function, argument name "y" doesn't conform to snake_case naming style (invalid-name)
# functions names must be pascal case
# explicar o que cada funcao faz
# inserir comentário dentro da funcao (qdo a função nao for um getter nem setter nem construtor)
# else desnecessário na função def f_function
# Unused argument 'x' (unused-argument) = criar variaveis para colovar o x e o y
# nome da primeira funçao está mto grande. FOi preciso reduzir.
# o nome do arquivo tem q respeitar o snake case
# retirar o module "object" da primeira função porque é redundante
# nome das funções tem que ser uma variável no estilo snakecase
# improve  (chained-comparison)
# Class name "D_class" e C doesn't conform to PascalCase naming style (invalid-name)
# sobrecarga de operador - evitar - nao pode ter função com o mesmo nome em classes diferentes
# Final newline missing (missing-final-newline)
