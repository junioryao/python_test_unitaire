import random
import inspect


def random_gen():

    # create an infinite loop , if random.randint(10,20) == 15 break the loop
    while (True):

        a = random.randint(10, 20)
        if a == 15:
            yield a
            break
        else:
            yield a


def decorator_to_str(func):
  
    # create new function  by adding the new requiered feature
    # args to accept any form of argurment
    def to_string(*args):
        #string the result 
        return str(func(*args))

    return to_string


@decorator_to_str
def add(a, b):
    return a + b


@decorator_to_str
def get_info(d):
    return d['info']
 

def ignore_exception(exception):
    # todo exercise 3
    #prefix decorator 

    def division(func):
        
        def func(*arg):

            try :    
                if len(arg ) > 0 :
                    if arg[1] == 0 :
                        return None 
                    elif not arg[1] == 0  :
                        return int( arg[0] / arg[1] ) 
                    else :
                        return None 
            except :

                return None 

        return func

    return division
   


@ignore_exception(ZeroDivisionError)
def div(a,b):
    return a / b


@ignore_exception(TypeError)
def raise_something(exception):
    raise exception



# exercise 4
class CacheDecorator:
    """Saves the results of a function according to its parameters"""

    def __init__(self):
        self.cache = {}

    def __call__(self, func):

        def _wrap(*a, **kw):
            if a[0] not in self.cache:
                self.cache[a[0]] = func(*a, **kw)
            return self.cache[a[0]]

        return _wrap


class MetaInherList(type):

    # Meta class inherite from the actual class type
    # new to create the desire object class
    # use too define the rules for a class

    '''
    specify from which class the inherit class will belong to 
    test = type("test",(),{})   classname , superclass , attribut of the class 

    '''

    def __new__(self, class_name, super_class, attrs):

        # changing the super class
        super_class = (list, Ex)
        return type(class_name, super_class, attrs)


class Ex:
    x = 4


class ForceToList(Ex, metaclass=MetaInherList):
    pass


# Metaclass to check an attribute name process with 3 arguments
# Exercise 6


class checkProcess(type):

    def __new__(self, classname, superclass, attrs):
        # return True or false if a class has an attribute name process
        # with 3 args or not

        val = False

        for i in attrs.keys():

            '''

            check if i is a string == process
            then check if its contain a function object ,

            use the function co_argcount on the function object to get the number
            of parameters 

            As it is a class methode the count include self , by decrementing 
            the argcount by  1 , we ll easily check it 

            '''

            if i == 'process' and inspect.isfunction(attrs[i]) and (attrs[i].__code__.co_argcount - 1 == 3):
                val = True

        if val:
            print("class inherit successfully")
            return type(classname, superclass, attrs)
        else:
            print("Missing function with 3 parameters")
