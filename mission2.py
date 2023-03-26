# 문제에 주어진 코드

def solution(answers):
    answer = []
    return answer



# 샘플로 내가 만들어본 입력값

<<<<<<< HEAD
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
=======
answers = [2,1,2,5,1,2,3,4,4,1,3,4,2,5,5,1,3,4,2,5] #[4,5,6]
# answers = [2,1,3,5,1,2,3,4,4,1,3,4,2,5,5,1,3,4,2,5] #[5,5,5]
# answers = [4,4,4,5,4,5,5,1,1,4,4,4,4,5,4,4,5,5,1,4] #[0,0,0]
# answers = [2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1] #[0,4,8]
# answers = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5] #[20,3,2]
# answers = [2,1,3,5,1,2,2,4,4,1,3,4,2,5,5,1,3,4,2,5] #[6,6,5]
# answers = [2,1,3,5,1,2,4,4,4,1,3,4,2,5,5,1,3,4,2,5] #[5,5,6]
>>>>>>> answers_10000



# 정답과 수포자들이 찍은 답을 비교해서 수포자들의 점수를 계산

answer_pattern_of_supos = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]

points_of_supos = []

for ii in range(len(answer_pattern_of_supos)):
    total_right_answers = 0
    for i, an in enumerate(answers):
        if answer_pattern_of_supos[ii][i%len(answer_pattern_of_supos[ii])] == answers[i]:
            total_right_answers += 1
    points_of_supos.append(total_right_answers)

max_point = max(points_of_supos)

max_point = max(answers_by_testers)



# 결과값을 출력

# case1) 모두 동점인 경우
<<<<<<< HEAD

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
=======
if len(set(points_of_supos)) == 1:
    if points_of_supos[0] == 0:
        print("모든 사람이 모든 문제를 틀렸습니다.")
    else:
        print(f"모든 사람이 {total_right_answers}문제씩을 맞혔습니다.")

# case2) 모두 다른 점수를 득점한 경우

elif len(set(points_of_supos)) == len(points_of_supos):
    
    for i, e in enumerate(points_of_supos):
        if points_of_supos[i] == len(answers):
            print(f"수포자 {i + 1}은/는 모든 문제를 맞혔습니다.")
        elif points_of_supos[i] == 0:
            print(f"수포자 {i + 1}은/는 모든 문제를 틀렸습니다.")
        else:
            print(f"수포자 {i + 1}은/는 {points_of_supos[i]}문제를 맞혔습니다.")

    supo_index = points_of_supos.index(max(points_of_supos))
    print(f"따라서 가장 많은 문제를 맞힌 사람은 수포자 {supo_index + 1}입니다.")
>>>>>>> answers_10000

# case3) 동점자가 있는 경우

else:
<<<<<<< HEAD
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
=======
    if points_of_supos.count(max_point) > 1:
        for i, e in enumerate(points_of_supos):
            if points_of_supos[i]==len(answers):
                print(f"수포자 {i + 1}은/는 모든 문제를 맞혔습니다.")
            elif points_of_supos[i]==0:
                print(f"수포자 {i + 1}은/는 모든 문제를 틀렸습니다.")
            else:
                print(f"수포자 {i + 1}은/는 {points_of_supos[i]}문제를 맞혔습니다.")
        
        maxs = []
        
        for ind, iii in enumerate(points_of_supos):
            if iii == max(points_of_supos):
                maxs.append(ind)
        
        tester_index = points_of_supos.index(max(points_of_supos))
        print(f"따라서 가장 많은 문제를 맞힌 사람은 수포자 {maxs[0] + 1}와/과 수포자 {maxs[1] + 1}입니다.")
        
    else:
        for i, e in enumerate(points_of_supos):
            if points_of_supos[i]==len(answers):
                print(f"수포자 {i + 1}은/는 모든 문제를 맞혔습니다.")
            elif points_of_supos[i]==0:
                print(f"수포자 {i + 1}은/는 모든 문제를 틀렸습니다.")
            else:
                print(f"수포자 {i + 1}은/는 {points_of_supos[i]}문제를 맞혔습니다.")

        tester_index = points_of_supos.index(max(points_of_supos))
>>>>>>> answers_10000
        print(f"따라서 가장 많은 문제를 맞힌 사람은 수포자 {tester_index + 1}입니다.")