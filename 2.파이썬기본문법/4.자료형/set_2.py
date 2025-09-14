# 리스트 연산자 ( 리스트끼리는 더하기만 / 곱하기는 정수(숫자만)와만 가능)
list_1 = [1,2,3]
list_2 = [4,5,6]
print('list_1 + list_2)', list_1 + list_2) #리스트 연결

list_1.extend(list_2) # (list_1 + list_2) [1, 2, 3, 4, 5, 6]
print('list_1 = ', list_1) #리스트 연결

print('list_1 * 3', list_1 * 3) #리스트 반복

list_1.append(list_2) #-> list_1 =  [1, 2, 3, 4, 5, 6]
print('list_1 = ', list_1)

# 문자열
str_1 = 'Hello'
str_2 = 'World'
print('str_1 + str_2 = ', str_1 + str_2)
print('str_1 * 3 = ', str_1 * 3)


# Set
# 중복허용 안함
set_1 = {1,2,3,4,5,7,8,1,2,3,4,5,6,7}
print('set_1 = ', set_1) #중복제거
# print(set_1[0]) #인덱싱 불가    
# set에서 특정 위치에 단일 값에 접근하려면
print('set_1에서 특정 위치에 단일 값에 접근하려면 = ', list(set_1)[0]) #인덱싱 불가 -> 리스트로 변환 후 인덱싱 가능

# set 사용하는 이유) 중복제거 + 집합연산 (합집합, 교집합, 차집합)
set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8}
# 교집합
print('set_1 & set_2 = ', set_1 & set_2) #교집합
print('set_1.intersection(set_2) = ', set_1.intersection(set_2)) #교집합
# 합집합
print('set_1 | set_2 = ', set_1 | set_2) #합집합
print('set_1.union(set_2) = ', set_1.union(set_2)) #합집합
# 차집합
print('set_1 - set_2 = ', set_1 - set_2) #차집합
print('set_1.difference(set_2) = ', set_1.difference(set_2)) #차집합