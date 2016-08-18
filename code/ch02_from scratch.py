def double(x):
    return x * 2

def apply_to_one(f):            # 인자로 들어온 함수 f에 1을 넣는 함수
    return f(1)

my_double = double              # 함수에 함수를 대입할수 있다
x = apply_to_one(my_double)     # 함수를 인자로 하여 다른 함수에 대입할수 있다.

print (x)


