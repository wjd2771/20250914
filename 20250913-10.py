# 학생 관리 프로그램 - 성적 입력 및 석차 계산

# 학생 정보를 입력받는 함수
def input_student_info():
    students = []
    while True:
        name = input("학생 이름을 입력하세요 (종료하려면 q 입력): ")
        if name.lower() == 'q':
            break
            
        try:
            score = int(input(f"{name}의 점수를 입력하세요 (0-100): "))
            if 0 <= score <= 100:
                # 튜플로 학생 정보 저장 (이름, 점수)
                students.append((name, score))
            else:
                print("점수는 0에서 100 사이여야 합니다.")
        except ValueError:
            print("올바른 점수를 입력해주세요.")
    
    return tuple(students)

# 석차를 계산하는 함수
def calculate_ranks(students):
    # 점수를 기준으로 정렬된 새로운 튜플 리스트 생성
    sorted_students = tuple(sorted(students, key=lambda x: x[1], reverse=True))
    
    # 석차 정보를 포함한 새로운 튜플 리스트 생성
    ranked_students = []
    current_rank = 1
    previous_score = None
    same_rank_count = 0
    
    for i, (name, score) in enumerate(sorted_students):
        if score == previous_score:
            # 동점자는 같은 석차 부여
            rank = current_rank - same_rank_count
        else:
            rank = current_rank
            same_rank_count = 0
        
        ranked_students.append((name, score, rank))
        previous_score = score
        current_rank += 1
        same_rank_count += 1
    
    return tuple(ranked_students)

# 결과를 출력하는 함수
def print_results(ranked_students):
    print("\n== 학생 성적 순위 ==")
    print("순위\t이름\t점수")
    print("----------------")
    for name, score, rank in ranked_students:
        print(f"{rank}등\t{name}\t{score}점")

# 메인 프로그램 실행
def main():
    print("학생 성적 관리 프로그램")
    print("------------------------")
    
    # 학생 정보 입력 받기
    students = input_student_info()
    
    if not students:
        print("입력된 학생 정보가 없습니다.")
        return
        
    # 석차 계산 및 정렬
    ranked_students = calculate_ranks(students)
    
    # 결과 출력
    print_results(ranked_students)

if __name__ == "__main__":
    main()
