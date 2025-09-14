# delete
a=[10,20,30,20]
#del은 한칸 띄어야함
del 0

# delete
#1.빈리스트 생성
#2. append를 이용해서 데이터를 추가
#3. pop을 이용해서 데이터를 삭제
#4. 또다른 리스트를 준비해서 3번에서 삭제한 인덱서, 데이터 저장
#5. 저장된 리스트에 역순으로 데이터를 뽑아서 insert를 이용해서 복원

data = []
# num = input('숫자 입력 : ')
# num - int(num)
# data.appened(num)


data.append(int(input('숫자 입력 : '))) #10
data.append(int(input('숫자 입력 : '))) #30
data.append(int(input('숫자 입력 : '))) #20
print('data= ',data) #print [10,30,20]
#삭제
removed_list = []
removed_data.pop(1) #data[10,20]
removed_list.append([1,removed_data]) #[[1,30]]

removed_data.pop(0) #data[20]
removed_list.append([0,removed_data]) #[[1,30][0,10]]

removed_data.pop(0) #data[2]
removed_list.append([0,removed_data]) #[[1,30][0,10][0,20]]

#복원순서 [20]-> [10,20] ->[10,30,20]
#삭제순서 [10,30,20] -> [10,20] -> [20] ->[]