from datetime import datetime

def func():
    return (11,'asfas','155545')



def func1(a,b=10,*args,**kwargs):
    print(a, b, args,kwargs)


def func2(content=b"", *args, **kwargs):
    print(content,args,kwargs)


def func3():
    if isinstance("str",str):
        print("yes")
    else:
        print("no")

def func4():
    a = 1
    b = 2
    print(a.__ge__(b))
    print(a > b)


def func5():
    account_dict = {'a':1,'b':2,'c':3}
    print(account_dict.get('e'))

def main():
    # func1(1)
    # func1(1,2)
    # func1(1,2,3)
    # func1(1,2,3,4)
    # func1(1,b=2)
    # func1(b=2,a=10)
    # func1(1,2,k=1,e=2)
    # func2("hello world",1)
    # tuple = func()
    # print(type(tuple),tuple[0])
    # func4()
    func5()
if __name__ == '__main__':
    main()