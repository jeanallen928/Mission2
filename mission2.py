# 문제에 주어진 코드

def solution(answers):
    answer = []
    return answer



# 샘플로 내가 만들어본 입력값

answers = [2,1,2,5,1,2,3,4,4,1,3,4,2,5,5,1,3,4,2,5]

answers_of_supos = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]



# 정답과 수포자들이 찍은 답을 비교해서 수포자들의 점수를 계산

points_of_supos = []

for ii in range(len(answers_of_supos)):
    total_right_answers = 0
    for i, an in enumerate(answers):
        if answers_of_supos[ii][i%len(answers_of_supos[ii])] == answers[i]:
            total_right_answers += 1
    points_of_supos.append(total_right_answers)



# 결과값을 출력

# case1) 모두 동점인 경우

if len(set(points_of_supos)) == 1:

    print(f"모두 {total_right_answers}문제를 맞혔습니다.")

# case2) 모두 다른 점수를 득점한 경우

if len(set(points_of_supos)) == len(points_of_supos):
    
    for i, e in enumerate(answers_of_supos):
        print(f"수포자 {i + 1}은/는 {points_of_supos[i]}문제를 맞혔습니다.")

    tester_index = points_of_supos.index(max(points_of_supos))
    print(f"따라서 가장 많은 문제를 맞힌 사람은 수포자 {tester_index + 1}입니다.")