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
y = apply_to_one(lambda x: x+4)     # 5  짧은 익명 람다 함수
print(y)                            #

another_double = lambda x: 2 * x
print(another_double(4))

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

# 따옴표 세개로 여러줄 주석 가능
multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""

print (0 / 0)   # ZeroDivisionError: division by zero

# List의 구조 살펴보기
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

# List의 조작
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

j_grade = grades["Joel"] # equals 80  , 키로 value를 호출
print(j_grade)

kates_grade = grades["Kate"]  # except KeyError: print "no grade for Kate!"

# 연산자 in으로 키값있는지 확인
joel_has_grade = "Joel" in grades   # 키 값 in Dict 이 있는지 TRUE, FALSE 반환
kate_has_grade = "Kate" in grades   # Kate는 값이 없다.
print (joel_has_grade)
print (kate_has_grade)

# .get함수는 해당 키를 못찾으면 기본값(0)을 반환해 준다
joels_grade = grades.get("Joel", 0) # equals 80
kates_grade = grades.get("Kate", 0) # equals , 이름이 없으니 대신 0을 반환
no_ones_grade = grades.get("No One") # 기본값으로 None 반환
print (joels_grade )
print (kates_grade )
print (no_ones_grade )

# 키로 벨류 부르기
grades["Tim"] = 99             # replaces the old value
grades["Kate"] = 100           # adds a third entry
num_students = len(grades)      # equals 3
print(grades)                   # 세쌍의 키 벨류가 있어서..

# 정형화된 문자열을 표현할 때
tweet = { "user" : "joelgrus",
          "text" : "Data Science is Awesome",
          "retweet_count" : 100,
          "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

# key,value, item
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

# defaultdict

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

# defaultdict 활용하는 방법
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

# Counter
from collections import Counter # key에 빈도값을 연결하여 히스토그램등에 쓰임
c = Counter([0, 1, 2, 0]) # c is (basically) { 0 : 2, 1 : 1, 2 : 1 }
print(c)

# 이것 한줄로 단어 카운트 해결
word_counts = Counter(document)
print(document)     # This is a first sentence for Python self study
print(word_counts)  #

# print the 10 most common words and their counts
from collections import Counter
print (word, count)
for word, count in word_counts.most_common(10):     # most_common(10)
    pass

# Sets
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
one_is_less_than_two = 1 < 2 # equals True
true_equals_false = True == False # T가 F와 같다면 Ture

x = None        # 파이썬은  null을 None으로 표기
print x == None # prints True, 파이썬스럽지 않다
print x is None # prints True, 파이썬스럽다

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
pairs = [(x, y) for x in range(10) for y in range(10)]
pairs

increasing_pairs = [(x, y) for x in range(10)

