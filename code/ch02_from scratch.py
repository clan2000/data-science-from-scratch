# 함수 기초
# <editor-fold desc="함수 기초">
def double(x):
    return x * 2

def apply_to_one(f):         # 인자로 들어온 함수 f에 1을 넣는 함수
                                # 의미 없는 라인
    return f(1)

# 함수에 함수 넣기
my_double = double              # 함수에 함수를 대입할수 있다
x = apply_to_one(my_double)     # 함수를 인자로 하여 다른 함수에 대입할수 있다.
print(x)
# </editor-fold>

# 람다 함수
# <editor-fold desc="짧은 익명 람다 함수">
y = apply_to_one(lambda x: x+4)     # 5  짧은 익명 람다 함수
print(y)                            #

another_double = lambda x: 2 * x
print(another_double(4))

another_double = lambda x: 2 * x        # don't do this
def another_double(x): return 2 * x     # do this instead
# </editor-fold>

# 함수의 Default 값
# <editor-fold desc="message="my default message"">
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
# </editor-fold>

# 따옴표
# <editor-fold desc="따옴표">
single_quoted_string = 'data science'
double_quoted_string = "data science"
# </editor-fold>

# 특수문자 처리
# <editor-fold desc="\사용법 r사용법">
tab_string = "\t"   # represents the tab character
print(len(tab_string))      # is 1 , 문자길이는 한자
print("C"+tab_string+"C")   # 거리는 4칸이지만

not_tab_string = r"\t" # represents the characters '\' and 't'
len(not_tab_string) # is 2   '\t'
print(not_tab_string)
# </editor-fold>

# 따옴표 세개로 여러줄 주석 가능
# <editor-fold desc="주석">
multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""
# </editor-fold>

# division by zero
# <editor-fold desc="division by zero">
print (0 / 0)
# </editor-fold>

# List의 구조 살펴보기
# <editor-fold desc="List의 구조 길이 합계">
integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]      # 이질적 자료 모음

list_of_lists = [ integer_list, heterogeneous_list, [] ]
print(list_of_lists)                    # 이렇게 표시됨 [[1, 2, 3], ['string', 0.1, True], []]
print(len(list_of_lists))               # 결과는 3, 첫번째 껍데기 안의 갯수를 보여줌

list_length = len(integer_list)         # 결과는 3
list_sum = sum(integer_list)            # 결과는 6
# </editor-fold>

# List의 인자 살펴 보기
# <editor-fold desc="List의 인자 지정">
x = range(10) # is the list [0, 1, ..., 9]
print (x)
zero = x[0]
one = x[1]
nine = x[-1]    # equals 9, 'Pythonic' for last element
eight = x[-2]   # equals 8, 'Pythonic' for next-to-last element #
x[0] = -1       # now x is [-1, 1, 2, 3, ..., 9]
print(x)
# </editor-fold>

# List 의 참조
# <editor-fold desc="List의 참조">
first_three = x[:3]
print(first_three)

three_to_end = x[3:]
one_to_four = x[1:5]
last_three = x[-3:]
print(three_to_end)

without_first_and_last = x[1:-1]
print(without_first_and_last)
copy_of_x = x[:]
# </editor-fold>

# List 와 in
# <editor-fold desc="List 와 in">
0 in [1, 2, 3]  # False
# </editor-fold>

# List 의 조작
# <editor-fold desc="List에 추가 ">
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
# </editor-fold>


# 튜플은 그 값을 바꿀수 없다
# <editor-fold desc="튜플은 변경 불가">
my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3

# my_list is now [1, 3] try:
my_tuple[1] = 3 #  except TypeError:  print "cannot modify a tuple"
# </editor-fold>

# 함수가 여러개의 값을 같이 반환
# <editor-fold desc="파이썬 스러운 변수 반환">
def sum_and_product(x, y):
    return (x + y),(x * y)
sp = sum_and_product(2, 3)      # equals (5, 6)
print(sp)                      # 하나의 변수에 두개의 값

s, p = sum_and_product(5, 10)   # s is 15, p is 50, 이렇게 두변수에 동시에 입력도 가능하다
print(s,p)

x, y = 1, 2     # now x is 1, y is 2
x, y = y, x     # 가장 파이썬스러운 변수 값 교환
# </editor-fold>

# Dict를 알아 보자
# <editor-fold desc="key, value 구조를 만들수 있다">
empty_dict = {}         # 가장 파이썬 스럽게 Dict를 만드는 법
empty_dict2 = dict()    # less Pythonic
grades = {  "Joel"  : 80,
            "Tim"   : 95 }    # 이것이 Dict다
print(grades)

j_grade = grades["Joel"] # equals 80  , 키로 value를 호출
print(j_grade)

kates_grade = grades["Kate"]  # except KeyError: print "no grade for Kate!"
# </editor-fold>

# 연산자 in 으로 키값있는지 확인
# <editor-fold desc="in 연산자">
joel_has_grade = "Joel" in grades   # 키 값 in Dict 이 있는지 TRUE, FALSE 반환
kate_has_grade = "Kate" in grades   # Kate는 값이 없다.
print (joel_has_grade)
print (kate_has_grade)
# </editor-fold>

# .get함수는 해당 키를 못찾으면 기본값(0)을 반환해 준다
# <editor-fold desc="get 함수 사용법">
joels_grade = grades.get("Joel", 0) # equals 80
kates_grade = grades.get("Kate", 0) # equals , 이름이 없으니 대신 0을 반환
no_ones_grade = grades.get("No One") # 기본값으로 None 반환
print (joels_grade )
print (kates_grade )
print (no_ones_grade )
# </editor-fold>

# 키로 벨류 부르기
# <editor-fold desc="Key로 호출">
grades["Tim"] = 99             # replaces the old value
grades["Kate"] = 100           # adds a third entry
num_students = len(grades)      # equals 3
print(grades)                   # 세쌍의 키 벨류가 있어서..
# </editor-fold>

# 정형화된 문자열을 표현할 때
# <editor-fold desc="Description">
tweet = { "user" : "joelgrus",
          "text" : "Data Science is Awesome",
          "retweet_count" : 100,
          "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}
# </editor-fold>

# key,value, item 함수 사용법
# <editor-fold desc="Description">
print (tweet)                   # {키:값, 키:값,,,}

tweet_keys = tweet.keys()       # list of keys  키 부분만 출력
print (tweet_keys)


tweet_values = tweet.values()   # list of values 값 부분만 출력
print(tweet_values)

tweet_items = tweet.items()     # item  출력 [(키,값), (키,값..]
print(tweet_items)

print ("user" in tweet_keys)    # tweet_keys는 dict가 아닌 List인데 그래서 in 사용시 느림

print("user" in tweet)          # dict에서 in을 사용했기 때문에 빠름. 파이썬 스럽다

"joelgrus" in tweet_values      # list of (key, value) tuples
# </editor-fold>

# defaultdict
# <editor-fold desc="defaultdict을 쓰지 않고">
# 1. 가장 기초적인 방법
word_counts = {}
for word in document:
    if word in word_counts:         # 해당 단어가 있으먄
        word_counts[word] += 1      # 그 단어 value에 1을 더한다
    else:
        word_counts[word] = 1       # 없으면 1로 value를 지정

# 2. 에러를 활용한 방법
# document = "This is a first sentence for Python self study"
word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1
print(word_counts)

# 좀더 고급스러운 방법
word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

# </editor-fold>



# defaultdict 활용하는 방법

# <editor-fold desc="해당 키값이 없는 경우 만들어 준다">
from collections import defaultdict
word_counts = defaultdict(int)  # int() produces 0 , Defaultdict 형태의 함수로 만든다
for word in document:
    word_counts[word] += 1      # 해당 word가 없으면 0이므로 1로 채운다


# case #1
from collections import defaultdict
dd_list = defaultdict(list)     # 빈 list를 생성
dd_list[2].append(1)            # 세번째 자리에 1을 채운다
dd_list[0].append(9)            # 0째 자리에 9를 채운다
print(dd_list)
len(dd_list)

# case #2
from collections import defaultdict
dd_dict = defaultdict(dict)
dd_dict["Joel"]["City"] = "Seattle"
len(dd_dict)
print(dd_dict)                  # defaultdict(<class 'dict'>, {'Joel': {'City': 'Seattle'}})

# case #3
from collections import defaultdict
dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1               # 이부분은 알수 없다
print(dd_pair)                  # defaultdict(<function <lambda> at 0x105acc510>, {2: [0, 1]})
# </editor-fold>

# Counter
# <editor-fold desc="히스토그램에 쓰임">
from collections import Counter # key에 빈도값을 연결하여 히스토그램등에 쓰임
c = Counter([0, 1, 2, 0]) # c is (basically) { 0 : 2, 1 : 1, 2 : 1 }
print(c)
# </editor-fold>

# 이것 한줄로 단어 카운트 해결
# <editor-fold desc="단어 세기">
document = "This is a first sentence for Python self study"
word_counts = Counter(document)
print(document)     # This is a first sentence for Python self study
print(word_counts)
# </editor-fold>

# print the 10 most common words and their counts
word = "wolf fox bear cat dogs eagle"
from collections import Counter
print (word, count)
for word, count in word_counts.most_common(10):     # most_common(10)
    pass

# Sets: 이것은 파이썬에서 집합을 표현
# <editor-fold desc="집합">
s = set()
s.add(1)
s.add(2)
s.add(2)    # 이미 앞에서 2를 넣었기 때문에 집합개념인 s는 원소 갯수는 변하지 않는다
print(s)


x = len(s)  # 2
print(x)

y = 2 in s
print(y)    # TRUE

z = 3 in s
print(z)    # FALSE
# </editor-fold>

# List보다 Set에서 in으로 원소를 찾는 것이 훨씬 빠르다
stopwords_list = ["a","an","at"] + hundreds_of_other_words + ["yet", "you"]
"zip" in stopwords_list # False, but have to check every element

stopwords_set = set(stopwords_list)
"zip" in stopwords_set  # very fast to check

# set과 list의 차이점 set은 중복 제거용으로 쓸 수 있다
item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)              # 6
item_set = set(item_list)               # 집함이므로 원소는 3개
num_distinct_items = len(item_set)      # 3
distinct_item_list = list(item_set)     # 중복된 원소가 제거되어 [1,2,3]만 남는다

# 흐름 제어
if 1 > 2 :
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use else (if you want to)"
print(message) # when all else fails use else (if you want to)

# if else는 한줄로도 표현 가능
parity = "even" if x % 2 == 0 else "odd "
print(parity)

# 파이썬도 while이 있지만
x = 0
while x < 10:
    print (x,"is less than 10")
    x += 1

# 대부분은 for in 을 쓴다
for x in range(10):  # 10칸을 만들지만 0~9 이다. 즉 10은 만들지 않는다
    print (x, "is less than 10")

# 복잡한 로직이 필요한 경우 continue 나 break를 사용할수 있다
for x in range(10):
    if x == 3:
        continue    # 여기서 점프하여 for 시작으로 돌아 간다
    if x == 5:
        break       # 루프를 멈추므로 6부터는 보이지 않는다
    print(x)        # This will print 0, 1, 2, and 4.

# 불리언 연산자
# <editor-fold desc="is 연산자">
one_is_less_than_two = 1 < 2 # equals True
true_equals_false = True == False # T가 F와 같다면 Ture

x = None        # 파이썬은  null을 None으로 표기
print x == None # prints True, 파이썬스럽지 않다
print x is None # prints True, 파이썬스럽다
# </editor-fold>

# 아래 값은 모두 False다
False
None
[]          # (an empty list), list는 1차원
{}          # (an empty dict), dict은 key-value
""
set()
0
0.0

# True와 False
# 첫문자가 비어 있지않으면 그 문자를 출력
s = "some_function_that_returns_a_string()"
if s:
    first_char = s[0]
else:
    first_char = ""
print(first_char)


# 첫번째 값이 참이면 두번째인 s[0]을 첫번째가 거짓이면 첫번째를 돌려준다
s =""
first_char = s and s[0]
print(first_char)       # 거짓이므로 첫번째 값인 ""을 돌려줌

x = 37
safe_x = x or 1     # 37 or 1 = 37
print(safe_x)

print(all([True, 1, { 3 }]))        # T 모두 참이냐 ?
print(all([True, 1, {}]))           # F, {}는 비어 있어서 거짓
print(any([True, 1, {}]))           # T 하나라도 참이냐?
print(all([]))                      # 이것이 왜 참임?
print(any([]))                      # F


''' Part 2 Not So Basic'''

x = [4,1,2,3]
y = sorted(x)           # is [1,2,3,4], x is unchanged
print(y)
x.sort()                # # now x is [1,2,3,4] .sort()로 순서를 바꾼다

# sort the list by absolute value from largest to smallest
# []는 리스트 {}는 Dict
# sort(리스트, key = abs, reverse = True)
x = sorted([-4,1,-2,3], key=abs, reverse=True) # is [-4,3,-2,1]
print(x)

# 가장 많이 나온 문자부터 표시
word_counts = Counter(document)
print(word_counts)
word_counts.items()

# 왜 안되는지 알수 없음 ㅠㅠ
wcc = sorted(word_counts.items(),               # (워드,카운트) 형태로 뽑아냄
            key = lambda (word, count): count,  # 카운트만 남기고 벗겨냄
            reverse = True)

# List Comprehensions : List 로 변환
even_numbers = [x for x in range(5) if x % 2 == 0]  # [0, 2, 4] #
print(even_numbers)

squares = [x * x for x in range(5)]                 # [0, 1, 4, 9, 16]
print(squares)

even_squares = [x * x for x in even_numbers]        # [0, 4, 16]
print(even_squares)

# dict로 변환
square_dict = { x : x * x for x in range(5) }       # { 0:0, 1:1, 2:4, 3:9, 4:16 }

# set으로 변환
square_set = { x * x for x in [1, -1] }             # { 1 }  제곱한 것은 동일하게 1 이므로

# 불필요한 값은 _로 표시
zeroes = [0 for _ in even_numbers] # even_numbers 와 동일한 길이
print(zeroes)

# (0,0) 부터 (9,9)까지
# <editor-fold desc="range 쓰는 법">
pairs = [(x, y) for x in range(10) for y in range(10)]
pairs

increasing_pairs = [(x, y)
                    for x in range(10)
                    for y in range(x + 1, 10)]  # Y 는 x보다 1 크게 시작
increasing_pairs
# </editor-fold>

# Generators and Iterators
# <editor-fold desc="무슨 뜻인지 명확하지 않음">
def lazy_range(n):
    """a lazy version of range"""
    i = 0
    while i < n:
        yield i
        i += 1

for i in lazy_range(10):
    do_something_with(i)

def natural_numbers():
    """returns 1, 2, 3, ..."""
    n = 1
    while True:
        yield n
        n += 1
        print(n)

lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)
print(lazy_evens_below_20)

# </editor-fold>

# 난수의 생성
# <editor-fold desc="난수 기본 및 영역 설정">
import random
four_uniform_randoms = [random.random() for _ in range(4)]
print(four_uniform_randoms)       # 난수 4개의 List를 보여줌

random.seed(10)             # seed 를 고정
print (random.random())     # 0.57140259469

random.seed(10)             # seed 를 고정
print (random.random())     # 0.57140259469 again

random.seed(11)             # seed 를 변경
print (random.random())     # 0.4523795535098186

print(random.randrange(10))        # 정수로 영역 지정, 끝점은 제외 range(10) = [0, 1, ..., 9]
print(random.randrange(3, 6))      # 정수로 영역 지정, 끝점은 제외 range(3, 6) = [3, 4, 5]
# </editor-fold>

# 난수의 순서 바꾸기
# <editor-fold desc="radom.shuffle 사용법">
up_to_ten = range(10)
print(up_to_ten)

l_utt = list(up_to_ten)
# In python3 range is a generator object - it does not return a list.
# Convert it to a list before shuffling.
print(l_utt)

random.shuffle(l_utt)
print (l_utt)    # shuffle은 리스트의 순서를 임의로 바꾸어 준다.
# </editor-fold>

# choice함수 쓰기와 list로 변환
# <editor-fold desc="random.sample">
my_best_friend = random.choice(["Alice", "Bob", "Charlie"]) # "Bob" for me
print(my_best_friend)

lottery_numbers = range(60)
print((lottery_numbers))

l_n = list(lottery_numbers)             # 먼저 리스트로 바꾸고
print(l_n)

winning_numbers = random.sample(l_n, 6) # [16, 36, 10, 6, 25, 9]
print(winning_numbers)
# </editor-fold>

# 무엇인가 반복을 할때 for _ in range (n)  사용
# <editor-fold desc="">
four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print(four_with_replacement)
# </editor-fold>

# 정규 표현식
# <editor-fold desc="re.match search split sub">
import re

print ([
    not re.match("a", "cat"),                   # 시작에 없으므로 F --> T
    re.search("a", "cat"),                      # cat 중에 a 존재
    not re.search("c", "dog"),                  # dog 중에 ㅊ 없음
    3 == len(re.split("[ab]", "carbs")),        # c,r,s,가 생성되어 길이가 3
    "R-D-" == re.sub("[0-9]", "-", "R2D2")      # 숫자를 -로 대체
])
# </editor-fold>

# 객체 지향 프로그래밍
# <editor-fold desc="class __init__ __repr__ ">
# by convention, we give classes PascalCase names
class Set:
        # these are the member functions
        # 첫번째 인자는 관례적으로  "self"
        # that refers to the particular Set object being used

    def __init__(self, values = None):
        # This is the constructor.
        # Set을 만들때 아래 와 같이 초기화 된다
        # 이렇게 사용할수 있다
        # s1 = Set()                 empty set
        # s2 = Set([1,2,2,3])        초기값이 주어진 셋
        self.dict = {}                  # 이 set의 모든 instance는 자체적으로 dict을 유지
                                        # 아 dict을 통해 항목의 존재여부를 파악
        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        # 프롬프트에서 이 함수를 입려거나 str()로 보내주면 set 객체를 문자열로 표현해 줌
        return "Set: " + str(self.dict.keys())

        # value를 받아서 Set dict 객체에 해당 value를 추가
    def add(self, value):
        self.dict[value] = True

        # value를 받아서 해당 Set Dict 객체에 있으며 True를 반환
    def contains(self, value):
        return value in self.dict

        # value를 받아서 해당 Set Dict에서 value를 삭제
    def remove(self, value):
            del self.dict[value]


ss = Set([1,2,3])        # s를 객체로 표현
ss.add(4)
print(ss)

print (ss.contains(4))

ss.remove(3)
print (ss.contains(3))
# </editor-fold>

# 함수형 도구

# <editor-fold desc="하나의 함수를 만들고 그것 일부를 끝어다 쓸수는 있지만">
def exp(base, power):
    return base ** power

def two_to_the(power):              # 2 - base - 의 power 승
    return exp(2, power)
# </editor-fold>

# <editor-fold desc="partial 함수 사용으로 더 손쉽게 쓸 수 있다">
from functools import partial
two_to_the = partial(exp, 2)        # is now a function of one variable
print (two_to_the(3))               # 8, 2의 exp 승

square_of = partial(exp, power=2)   # partial은 함수 인자를 지정하는 새로운 함수를 만든다
print (square_of(3))                  # 9
# </editor-fold>

# <editor-fold desc="map함수로 하나의 함수에 인자를 개별적으로 넣을 수도 있고">
def double(x):
    return 2 * x

xs = [1, 2, 3, 4]
twice_xs1 = [double(x) for x in xs]         # [2, 4, 6, 8]
twice_xs2 = list(map(double, xs))           # list xs의 각 요소에 대해 double 을 실행
                                            # 파이썬 3에서는 map의 결과를 list로 변환 해야 한다
twice_xs3 = double (xs)                     # List * 2 = List + List

print(twice_xs1)
print(twice_xs2)
print(twice_xs3)
# </editor-fold>

# <editor-fold desc="partial 함수로 어떤 함수를 다른 함수인의 인자에게 map하는 함수를 만들수도 있다">
list_doubler = partial(map, double)         # partial 은 map 함수 안에 double을 넣은 새로운 함수를 만든다
twice_xs = list_doubler(xs)                 # again [2, 4, 6, 8]
print(list(twice_xs))                       # list형으로 변환해 주어야 한다
# </editor-fold>

# <editor-fold desc="인자가 여러개인 함수에도 map 적용이 가능">
def multiply(x, y):
    return x * y

products = list(map(multiply, [1, 2], [4, 5]))  # [1 * 4, 2 * 5] = [4, 10]
print(products)                                 # [x,x,x],[y,y,y]

products = list(map(multiply, [1, 2] ))  #  이 것은 에러
print(products)

# </editor-fold>

# <editor-fold desc="for in if 사용법">
def is_even(x):                             # 짝수이면 0
    return x % 2 == 0

x_evens = [x for x in xs if is_even(x)]     # {1,2,3,4] 중 짝수인 것만 넘김  [2,4]
print(list(x_evens))
# </editor-fold>

# <editor-fold desc="filter로 다른 함수를 사용하기와 partial로 필터와 다른 함수 결합하기">
x_evens = filter(is_even, xs)               # xs에 대해 is_even을 필터로 사용
print(list(x_evens))

list_evener = partial(filter, is_even)      # us_even을 filter로 사용하는 함수를 partial로 만듦
x_evens = list_evener(xs)
# </editor-fold>

# <editor-fold desc="reduce는 list의 모든 항목을 합쳐주면서 하나의 값으로 만들어 준다">
from functools import partial
from functools import reduce                # 파이썬 3에서는 import 필요

xs = [1,2,3,4]
x_product = reduce (multiply, xs)             # = 1 * 2 * 3 * 4 = 24
print(x_product)

list_product = partial (reduce, multiply)    # *function* that reduces a list

x_product = list_product(xs)                # again = 24
print(x_product)
# </editor-fold>


# enumerate

# <editor-fold desc="파이썬 스럽지 않은 방법">
documents ="This is a second sentence for python self study"
for i in range(len(documents)):
    document = documents[i]
    print(i, document )

# also not Pythonic
i=0
for document in documents:
    print(i, document)
    i += 1
# </editor-fold>
# <editor-fold desc="enumerate는 인덱스, 항목을 tuple로 생성해 준다">
for i, document in enumerate(documents):    # enumerate는 인덱스, 항목을 tuple로 생성해 준다
    print(i, document)

for i in range(len(documents)):             # 안댁스만 필요한 경우, 파이썬 스럽지 않다
    print(i)

for i, _ in enumerate(documents):           # enumerate로 문자 갯수만 뽑는다
    print(i)
# </editor-fold>

# zip, argument unpacking
# <editor-fold desc="복수 list의 인자간 결합 또는 해체">
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zz = zip(list1, list2)          # is [('a', 1), ('b', 2), ('c', 3)]
print(list(zz))                 # list로 바꾸어서 출력

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)  # *인자를 해체할때 사용한다

def add(a, b):
    return a + b
add(1, 2)                       # 3
add([1, 2])                     # 인자가 1개이므로 에러
add(*[1, 2])                    # 풀어서 2개이므로 3
# </editor-fold>


# args와 kwargs

# <editor-fold desc="doubler함수는 다른 함수를 인자로 받아서 그 결과값을 2배로 해주는 고차 함수">
def doubler(f):
    def g(x):
        return 2 * f(x)
    return g

def f1(x):
    return x+1

g = doubler(f1)

print (g(3))        # 8 (== ( 3 + 1) * 2)
print (g(-1))         # 0 (== (-1 + 1) * 2)
# </editor-fold>

# <editor-fold desc="doubler는 복수 인자의 함수에는 적용할 수 없다">
def f2(x, y):
    return x+y

g = doubler(f2)
print (g(1, 2)) # 이 방식은 2개 이상의 인자를 넘길때에는 쓸수 없다
# </editor-fold>

# <editor-fold desc="여러 개의 인자를 받아서 tuple과 dict로 나누어 사용할수 있다">
def magic(*args, **kwargs):
    print ("unnamed args:", args)           # 이름없은 인자 tuple
    print ("keyword args:", kwargs)         # 이름있는 dict

magic(1, 2, key="word", key2="word2")
    # prints
    #  unnamed args: (1, 2)
    #  keyword args: {'key2': 'word2', 'key': 'word'}
# </editor-fold>

# <editor-fold desc="list와 dick을 해체하여 숫자 부분만 덧셈하는 것도 가능">
def other_way_magic(x, y, z):
    return x+y+z

x_y_list = [1, 2]
z_dict = {"z":3}
print (other_way_magic(*x_y_list, **z_dict)) # 6
# </editor-fold>

# <editor-fold desc="d_c함수는 kk함수를 인자로 받 그 결과를 2배로 해준다  kk는 tuple, dict를 인자로 받는다 ">
def f2(x, y):
    return x+y

def doubler_correct(kk):        # kk함수가 무엇을 인자로 받던 상관없다
    def g(*args, **kwargs):     # 어떤 인자들이던 g로 넘어오면 , pass them through to kk
        return 2 * kk(*args, **kwargs)
    return g

g = doubler_correct(f2)         # g는 f2의 결과 값을 2배로
print (g(1, 2))                 # 6,  g의 인자가 2개여도 무관
# </editor-fold>

