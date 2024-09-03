a_list = [3, 4, 62, 27, 83, 956, 26, 58, 3, 78, 168, 64, 78]

def print_list(a):
    for i in a:
        print(i)

print_list(a_list)

def scope_test():
    def do_local():
        spam = "local spam"
    
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"
    
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

print('\n함수 연습 문제 1')
def ipCount(x, y):
    result = x ** y
    return result

print(ipCount(int(input()), int(input())))

def numOfDigits(num):
    print(len(str(num )))

numOfDigits(int(input()))