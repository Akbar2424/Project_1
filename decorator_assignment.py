def main_key(func):
    def inner(x,y):
        print('This is main function')
        func()
    return inner
@main_key
def calculator():
    print('This is calculator function')

calculator(10,20)
