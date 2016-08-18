
# 함수 기초
def double(x):
    return x * 2

def apply_to_one(f):         # 인자로 들어온 함수 f에 1을 넣는 함수
                                # 의미 없는 라인
    return f(1)

# 함수에 함수 넣기
my_double = double              # 함수에 함수를 대입할수 있다
x = apply_to_one(my_double)     # 함수를 인자로 하여 다른 함수에 대입할수 있다.
print(x)

# 람다 함수
y = apply_to_one(lambda x: x+4)  # 5  짧은 익명 람다 함수
another_double = lambda x: 2 * x
print(y)

another_double = lambda x: 2 * x        # don't do this
def another_double(x): return 2 * x     # do this instead

# 함수의 Default 값
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

# 따옴표
single_quoted_string = 'data science'
double_quoted_string = "data science"

# 특수문자 처리
tab_string = "\t"   # represents the tab character
print(len(tab_string))      # is 1 , 문자길이는 한자
print("C"+tab_string+"C")   # 거리는 4칸이지만

not_tab_string = r"\t" # represents the characters '\' and 't'
len(not_tab_string) # is 2   '\t'
print(not_tab_string)

multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""
# 따옴표 세개로 여러줄 주석 가능

print (0 / 0)   # ZeroDivisionError: division by zero

# Lsit의 구조 살펴보기
integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]      # 이질적 자료 모음

list_of_lists = [ integer_list, heterogeneous_list, [] ]
print(list_of_lists)                    # 이렇게 표시됨 [[1, 2, 3], ['string', 0.1, True], []]
print(len(list_of_lists))               # 결과는 3, 첫번째 껍데기 안의 갯수를 보여줌

list_length = len(integer_list)         # 결과는 3
list_sum = sum(integer_list)            # 결과는 6

# List의 인자 살펴 보기
x = range(10) # is the list [0, 1, ..., 9]
print (x)
zero = x[0]
one = x[1]
nine = x[-1]    # equals 9, 'Pythonic' for last element
eight = x[-2]   # equals 8, 'Pythonic' for next-to-last element #
x[0] = -1       # now x is [-1, 1, 2, 3, ..., 9]
print(x)

# List의 참조
first_three = x[:3]
print(first_three)


three_to_end = x[3:]
one_to_four = x[1:5]
last_three = x[-3:]
print(three_to_end)

without_first_and_last = x[1:-1]
print(without_first_and_last)
copy_of_x = x[:]


0 in [1, 2, 3]
# True # False
# [-1, 1, 2]
# [3, 4, ..., 9] # [1, 2, 3, 4] # [7, 8, 9]
# [1, 2, ..., 8] # [-1, 1, 2, ..., 9]

x = [1, 2, 3]
x.extend([4, 5, 6])
print(x)

x = [1, 2, 3]
y = x + [4, 5, 6]
print(y)

x = [1, 2, 3]
x.append(0)
print(x)

y = x[-1]
print(y)

z = len(x)
print(z)


# 튜플은 그 값을 바꿀수 없다
my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3

# my_list is now [1, 3] try:
my_tuple[1] = 3 #  except TypeError: print "cannot modify a tuple"

# 함수가 여러개의 값을 같이 반환
def sum_and_product(x, y):
    return (x + y),(x * y)
sp = sum_and_product(2, 3)      # equals (5, 6)
print(sp)                      # 하나의 변수에 두개의 값

s, p = sum_and_product(5, 10)   # s is 15, p is 50, 이렇게 두변수에 동시에 입력도 가능하다
print(s,p)

x, y = 1, 2     # now x is 1, y is 2
x, y = y, x     # 가장 파이썬스러운 변수 값 교환

# Dict를 알아 보자
# key, value 구조를 만들수 있다

empty_dict = {}         # 가장 파이썬 스럽게 Dict를 만드는 법
empty_dict2 = dict()    # less Pythonic
grades = {  "Joel"  : 80,
            "Tim"   : 95 }    # 이것이 Dict다
print(grades)

 # dictionary litera
