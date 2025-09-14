# 리스트에 데이터 추가
# 맨 마지막에 추가하는 방법 # 중간에 추가하는 방법

# 리스트변수
scores=[10,20,30]
# 추가:마지막append
scores.append(100)
print(scores)

#추가:중간 .insert / 인덱스 위치에 추가
scores.insert(1,200)
print(scores)

#삭제
#del은 한칸 띄어야함
del scores[0] #달걀한판에서 달걀을 깨버려 실존1개의 달걀 없음
print(scores)
scores.pop(0) #가장마지막에 있는 애를 지우는 다른 방법 - 달걀한판에서 달걀을 하나빼서 내손에 쥐고 있음
print(scores)