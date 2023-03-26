# 문제에 주어진 코드

def solution(answers):
    answer = []
    return answer



# 샘플로 내가 만들어본 입력값

# answer = [2,1,2,5,1,2,3,4,4,1,3,4,2,5,5,1,3,4,2,5] #[4,5,6]
# answer = [2,1,3,5,1,2,3,4,4,1,3,4,2,5,5,1,3,4,2,5] #[5,5,5]
# answer = [4,4,4,5,4,5,5,1,1,4,4,4,4,5,4,4,5,5,1,4] #[0,0,0]
# answer = [2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1] #[0,4,8]
# answer = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5] #[20,3,2]
answer = [2,1,3,5,1,2,2,4,4,1,3,4,2,5,5,1,3,4,2,5] #[6,6,5]
# answer = [2,1,3,5,1,2,4,4,4,1,3,4,2,5,5,1,3,4,2,5] #[5,5,6]

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

max_point = max(answers_by_testers)



# 결과값을 출력

# case1) 모두 동점인 경우

if len(set(answers_by_testers)) == 1:
    if answers_by_testers[0] ==0:
        print("모든 사람이 모든 문제를 틀렸습니다.")
    else:
        print(f"모든 사람이 {total_answer}문제씩을 맞혔습니다.")

# case2) 모두 다른 점수를 득점한 경우

elif len(set(answers_by_testers)) == len(answers_by_testers):
    
    for i, e in enumerate(math_test_answers):
        if answers_by_testers[i]==len(answer):
            print(f"수포자 {i + 1}은/는 모든 문제를 맞혔습니다.")
        elif answers_by_testers[i]==0:
            print(f"수포자 {i + 1}은/는 모든 문제를 틀렸습니다.")
        else:
            print(f"수포자 {i + 1}은/는 {answers_by_testers[i]}문제를 맞혔습니다.")

    tester_index = answers_by_testers.index(max(answers_by_testers))
    print(f"따라서 가장 많은 문제를 맞힌 사람은 수포자 {tester_index + 1}입니다.")

# case3) 동점자가 있는 경우

else:
    if answers_by_testers.count(max_point) > 1:
        for i, e in enumerate(math_test_answers):
            if answers_by_testers[i]==len(answer):
                print(f"수포자 {i + 1}은/는 모든 문제를 맞혔습니다.")
            elif answers_by_testers[i]==0:
                print(f"수포자 {i + 1}은/는 모든 문제를 틀렸습니다.")
            else:
                print(f"수포자 {i + 1}은/는 {answers_by_testers[i]}문제를 맞혔습니다.")
        
        maxs = []
        
        for ind, iii in enumerate(answers_by_testers):
            if iii == max(answers_by_testers):
                maxs.append(ind)
        
        tester_index = answers_by_testers.index(max(answers_by_testers))
        print(f"따라서 가장 많은 문제를 맞힌 사람은 수포자 {maxs[0] + 1}와/과 수포자 {maxs[1] + 1}입니다.")
        
    else:
        for i, e in enumerate(math_test_answers):
            if answers_by_testers[i]==len(answer):
                print(f"수포자 {i + 1}은/는 모든 문제를 맞혔습니다.")
            elif answers_by_testers[i]==0:
                print(f"수포자 {i + 1}은/는 모든 문제를 틀렸습니다.")
            else:
                print(f"수포자 {i + 1}은/는 {answers_by_testers[i]}문제를 맞혔습니다.")

        tester_index = answers_by_testers.index(max(answers_by_testers))
        print(f"따라서 가장 많은 문제를 맞힌 사람은 수포자 {tester_index + 1}입니다.")