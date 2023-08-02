def hello() :
    print('Hello from inside a file!')

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]
    

def eat_lunch(lunch_items):
    if not lunch_items:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {lunch_items[0]}")
        for item in lunch_items[1:]:
            print(f"Next I eat {item}")

hello()
pack('arg1', 'arg2', 'arg3')
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])


