# CODE SOURCE: SOFTWARE ARCHITECTURE WITH PYTHON

"""
2 Module metricTest.py
3
4 Metric example - Module which is used as a testbed for static
checkers.
5 This is a mix of different functions and classes doing
different things.
6
7 """

""" A function which performs a sum """

def fn(x, y):
    """ Function fn that return the sum of x and y"""
    return x + y

def optimal_route(expected_time, start_time,favorite_route='SBS1K', favorite_option='bus'):
    """  find_optimal_route_to_my_office_from_home """
    d = (expected_time - start_time).total_seconds() / 60.0
    if d <= 30:
        return 'car'

    # If d>30 but <45, first drive then take metro
    if d > 30 and d < 45:
        return ('car', 'metro')

    # If d>45 there are a combination of optionsWriting Modifiable and Readable Code
    # First volvo,then connecting bus

    if d > 45:
        if d < 60:
            return ('bus:335E', 'bus:connector')
        # Might as well go by normal bus # return random.choice(('bus:330','bus:331',':'))
    elif d > 80:
        ':'.join((favorite_option, favorite_route))
    elif d > 90:  # Relax and choose favorite route
        return ':'.join((favorite_option, favorite_route))

""" A class which does almost nothing """

class C_class():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def f_function(self):
        """ Function f_function that doesn't do anything """
        pass

    def g_function(self, x, y):
        """ Function g to check """
        if self.x > self.x:
            return self.x + self.y
        elif self.x > self.x:
            return self.x + self.y

""" D class """
class D_class(C_class):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def f_function(self):
        """ Function that return the value of y + x """
        if self.x > self.y:
            return self.x - self.y
        return self.x + self.y

    def g_function(self):
        """ Function that return the value of y - x """
        if self.x > self.y:
            return self.x + self.y

        return self.y - self.x

# parentesis, indentation, importing, deleted "Chapter 2 ", changed the order expected_time & start_time
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

'''   
def getX():
    return self.X # getter

def setX(new_x): 
    self.X = new_x 
    return self.X # setter
'''
