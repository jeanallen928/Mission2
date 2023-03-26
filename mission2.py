# 문제에 주어진 코드

def solution(answers):
    answer = []
    return answer



# 샘플로 내가 만들어본 입력값

answer = [2,1,3,5,1,2,3,4,4,1,3,4,2,5,5,1,3,4,2,5]

math_test_answers = [
    [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],
    [2,1,2,3,2,4,2,5,2,1,2,3,2,4,2,5,2,1,2,3],
    [3,3,1,1,2,2,4,4,5,5,3,3,1,1,2,2,4,4,5,5]
]



# 진짜 정답과 수포자들의 정답을 비교해서 수포자들의 점수를 계산

answers_by_testers = []

for i, a in enumerate(math_test_answers):
    total_answer = 0
    for ii, b in enumerate(math_test_answers[i]):
        if math_test_answers[i][ii] == answer[ii]:
            total_answer += 1

    answers_by_testers.append(total_answer)



# 결과값을 출력

# case1) 모두 동점인 경우

if answers_by_testers[0]==answers_by_testers[1]==answers_by_testers[2]:

    print(f"모두 {total_answer}문제를 맞혔습니다.")

# case2) 모두 다른 점수를 득점한 경우

else:
    temp = 0
    
    for i, d in enumerate(answers_by_testers):
    
        if temp < answers_by_testers[i]:
            temp = answers_by_testers[i]
            max_math = i+1
    
        else:
            pass
    for i, e in enumerate(math_test_answers):
        print(f"수포자 {i + 1}은/는 {answers_by_testers[i]}문제를 맞혔습니다.")

    print(f"따라서 가장 많은 문제를 맞힌 사람은 수포자 {max_math}입니다.")