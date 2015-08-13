#coding=utf-8
# Old Version
# class WhatFor(object):
#     """docstring for WhatFor"""
#     def __init__(self):
#         super(WhatFor, self).__init__()
#     def it(self,cls):
#         print 'work with %s'%cls
#     it=classmethod(it)
#     def uncommon():
#         print "I am a staticmethod"
#     uncommon=staticmethod(uncommon)


#New Version
print("--------------------------------------------------------")
#使用自带的装饰器@property

class Person(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, first_name, last_name):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name

    #----------------------------------------------------------------------
    @property
    def full_name(self):
        """
        Return the full name
        """
        return "%s %s" % (self.first_name, self.last_name)
    @full_name.setter
    def full_name(self,name):

        if(isinstance(name,str)):
            names=name.split(" ")
            if(len(names)==1):
                self.first_name=names[0]
            if(len(names)==2):
                self.last_name=names[1]


person = Person("Mike","Zhang")
#将方法变为属性
print person.full_name

person.full_name="mingkai Hu"
print person.full_name

print("--------------------------------------------------------")
class WhatFor(object):
    """docstring for WhatFor"""
    @classmethod
    def it(cls):
        print 'work with %s'%cls
    @staticmethod
    def uncommon():
        print "I am a staticmethod"


Object_1=WhatFor()
Object_1.it()
Object_1.uncommon()
print("--------------------------------------------------------")
# 最简单的使用方法
def my_decorator(fn):
    print "I am a ordinary function"
    def wrapper():
        print "I am a funtion returned by the decorator"
        fn()
    return wrapper
def lazy_f():
    print("Zzzzzzz...")

lazy_f=my_decorator(lazy_f)
lazy_f()

@my_decorator
def lazy_f2():
    print "Zzzz..."
lazy_f2()




print("--------------------------------------------------------")

#2. 如何传递参数给装饰器
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):

    print "I make decorators! And I accept arguments:", decorator_arg1, decorator_arg2

    def my_decorator(func):
        # 这里能传递参数的能力，是闭包的特性
        # 更多闭包的内容，参考 http://stackoverflow.com/questions/13857/can-you-explain-closures-as-they-relate-to-python
        print "I am the decorator. Somehow you passed me arguments:", decorator_arg1, decorator_arg2

        # 不要搞混了装饰器参数和函数参数
        def wrapped(function_arg1, function_arg2) :
            print ("I am the wrapper around the decorated function.\n"
                  "I can access all the variables\n"
                  "\t- from the decorator: {0} {1}\n"
                  "\t- from the function call: {2} {3}\n"
                  "Then I can pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,
                          function_arg1, function_arg2))
            return func(function_arg1, function_arg2)

        return wrapped

    return my_decorator

@decorator_maker_with_arguments("Leonard", "Sheldon")
def decorated_function_with_arguments(function_arg1, function_arg2):
    print ("I am the decorated function and only knows about my arguments: {0}"
           " {1}".format(function_arg1, function_arg2))

decorated_function_with_arguments("Rajesh", "Howard")
print("--------------------------------------------------------")
#实例：使用装饰器打印一个函数的执行时间
def benchmark(func):
    import time
    def wrapper(*args,**kwargs):
        t=time.clock()
        res=func(*args,**kwargs)
        print func.__name__,time.clock()-t
        return res
    return wrapper

@benchmark
def f():
    j=0
    for i in range(0,100000):
        i=i**2
        j=j+i
    print j

f()


print("--------------------------------------------------------")
#3. 代理模式
class User(object):
    """docstring for User"""
    def __init__(self, roles):
        super(User, self).__init__()
        self.roles = roles
class Unauthorized(Exception):
    pass

def protect(role):
    def _protect(function):
        def __protect(*args,**kw):
            user=globals().get('user')
            if user is None or role not in user.roles:
                raise Unauthorized("I wont tell you")
            return function(*args,**kw)
        return __protect
    return _protect

tarek=User(('admin','user'))
bill=User(('user',))

class MySecrets(object):
    """docstring for MySecrets"""
    @protect('admin')
    def waffle_recipe(self):
        print "Use tons of butter"

these_are=MySecrets()
user=tarek
these_are.waffle_recipe()

user=bill
these_are.waffle_recipe()
