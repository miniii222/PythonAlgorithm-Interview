# PythonAlgorithm-Interview

### generator
- yield와 next를 이용해서 제너레이터만 생성해두고 저장해놓지 않고, 필요할 때 언제든 숫자를 만들어낼 수 있다.

```
def get_natural_number() :
  n = 0
  while True :
    n += 1
    yield n
    
g = get_natural_number()
for _ in rnage(100):
  print(next(g))
```

### range
- generator처럼 생성 조건만 정해두고 나중에 필요할 때 생성해서 꺼내 쓸 수 있다.
- 메모리 효율 good

```
a = [n for n in range(100000)]
b = range(100000)
```
라고 했을 때, 길이가 같고, 인덱스로 접근 역시 가능하지만, 차지하는 메모리가 b 가 훨씬 적다.

###print format
```
print(f'{idx + 1} : {fruit}')
```

### Dictionary (딕셔너리)
- 대부분의 연산(개수, 키 조회, 키/값 삽입, 키 존재 확인 여부)이 O(1)
#### dafaultdict
```
a = collections.defaultdict(int)
a['C'] += 1
```
a에 존재하지 않는 C라는 key를 불러와도 에러가 나지 않고, default value 0으로 삽입.

```
mydict = collections.defaultdict(list)
```
빈 dict 선언

#### Counter
```
collections.Coutner(a)
```
a라는 dictionary에 값이 몇 개가 들어가 있는지 알려줌

#### OrderedDict
```
collections.OrderedDict({'banana' : 3, 'apple' : 4})
```
대부분 key를 기준으로 정렬이 되는데, 정렬되지 않고 그대로 유지

