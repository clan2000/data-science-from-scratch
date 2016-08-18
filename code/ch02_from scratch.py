def double(x):
    return x * 2

def apply_to_one(f):         # 인자로 들어온 함수 f에 1을 넣는 함수
                                # 의미 없는 라인
    return f(1)

my_double = double              # 함수에 함수를 대입할수 있다
x = apply_to_one(my_double)     # 함수를 인자로 하여 다른 함수에 대입할수 있다.

print(x)

y = apply_to_one(lambda x: x+4)  # 5  짧은 익명 람다 함수

another_double = lambda x: 2 * x

print(y)

another_double = lambda x: 2 * x        # don't do this
def another_double(x): return 2 * x     # do this instead

def my_print(message="my default message"):  # message 인자의 Default 값으로 my default message를 사용
    print (message)

my_print("hello") # prints 'hello'
my_print() # prints 'my default message'

my_print("dododo")

def subtract(a=0, b=0):
    return a - b
print(subtract(10, 5))  # returns 5
print(subtract(0, 5))   # returns -5
print(subtract(b=5))    # same as previous

single_quoted_string = 'data science'
double_quoted_string = "data science"

tab_string = "\t"   # represents the tab character
print(len(tab_string))      # is 1 , 문자길이는 한자
print("C"+tab_string+"C")   # 거리는 4칸이지만

not_tab_string = r"\t" # represents the characters '\' and 't'
len(not_tab_string) # is 2   '\t'
print(not_tab_string)

