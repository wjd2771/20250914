if True :
    print('항상 실행되는 문장')
    
print('if와 상관 없는 문장')

score = 85
if score >= 90:
    print('90점 이상입니다')
    
list_1 = [1,2,3,4,5]
if 2 in list_1:
    print('2가 list_1에 있습니다')
    
dict_1 = {'name':'홍길동', 'age':30}
if 'name' in dict_1:
    print('name이 dict_1에 있습니다')  
    
num = 15
if num %2 == 0:   #짝수
    if num %3 == 0:
        print('2와 3의 공배수입니다')   
    else:
        print('2의 배수입니다')

if num %2 == 0 and num %3 == 0:
    print('2와 3의 공배수입니다')
    
    
dong = '101'
ho = '202'
price = '25000'

# '101동 202호의 가격은 25000원 입니다'
dong+'동 '+ho+'호의 가격은 '+price+'원 입니다'
f"{dong}동 {ho}호의 가격은 {price}원 입니다" --->이해못함
print(f"{dong}동 {ho}호의 가격은 {price}원 입니다")
    