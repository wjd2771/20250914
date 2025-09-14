# SET의 기본사용법
# 중복을 허용하지 않음
# 순서가 없음(인덱싱, 슬라이싱 불가) 순서를 보장하지 않음
# 집합연산 가능(합집합, 교집합, 차집합)
# 서로다른 자료형끼리 전환 가능( 리스트 <-> 튜플 )

# 1. SET 생성 및 중복 제거 예제
numbers = {1, 2, 2, 3, 3, 4, 5, 5}
print("중복이 제거된 SET:", numbers)  # 출력: {1, 2, 3, 4, 5}

# 2. 순서가 없음을 보여주는 예제
fruits = {'apple', 'banana', 'orange'}
print("\n원본 SET:", fruits)
# 여러번 실행하면 출력 순서가 매번 다를 수 있음

# 3. 집합 연산 예제
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

# 합집합 (Union)
union_set = set_A | set_B  # set_A.union(set_B) 도 가능
print("\n합집합:", union_set)

# 교집합 (Intersection)
intersection_set = set_A & set_B  # set_A.intersection(set_B) 도 가능
print("교집합:", intersection_set)

# 차집합 (Difference)
difference_set = set_A - set_B  # set_A.difference(set_B) 도 가능
print("차집합 (A-B):", difference_set)

# 4. 자료형 변환 예제
# 리스트를 SET으로 변환
my_list = [1, 2, 2, 3, 3, 4]
list_to_set = set(my_list)
print("\n리스트를 SET으로 변환:", list_to_set)

# SET을 리스트로 변환
set_to_list = list(list_to_set)
print("SET을 리스트로 변환:", set_to_list)


# 5. SET의 기본 메서드 사용 예제
fruits = {'apple', 'banana', 'orange'}
print("\n원본 SET:", fruits)

# 요소 추가
fruits.add('grape')
print("요소 추가 후:", fruits)

# 요소 제거
fruits.remove('apple')  # 없는 요소를 remove하면 KeyError 발생
print("요소 제거 후:", fruits)


