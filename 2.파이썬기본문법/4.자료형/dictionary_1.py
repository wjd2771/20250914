# Dictonary
# key:value 쌍으로 이루어진 자료형 ex) {'name':'홍길동', 'age':20} / name -> key, '홍길동' -> value
# 중복사용시 마지막꺼로 덮어씌움
# key는 중복 불가, value는 중복 가능
# abc = { '이름':'홍길동', '나이':20 }
# #abc['이름'] abc.get( '이름', '없음' ) -> 함수로표현할 때, 없음으로 설정해주면 값이 없을 때 none이 아닌 없음으로 출력
# abc['나이'] = 30 # 수정가능
# abc['취미'] = '축구' # 추가가능

dict_1 = {} # set? dictoionary? -> 빈껍데기 중괄호는 dictionary
print(type(dict_1))
dict_1['name'] = '홍길동'
print(dict_1)
dict_1['age'] = 20 # 추가
print(dict_1)
dict_1['age'] = 200 # 수정
print(dict_1)

