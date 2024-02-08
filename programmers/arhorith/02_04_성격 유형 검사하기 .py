# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    person_dic = {
        "R": 0,
        "T": 1,
        "C": 2,
        "F": 3,
        "J": 4,
        "M": 5,
        "A": 6,
        "N": 7
    }
    
    score_person = [0] * 8
    persons = ["R", "T", "C", "F", "J", "M", "A", "N"]
    score_dic = {
        1: 3,
        2: 2,
        3: 1,
        4: 0,
        5: 1,
        6: 2,
        7: 3
    }
    for i, sur in enumerate(survey):
        first, second = sur.rstrip()
        first_index = person_dic[first]
        second_index = person_dic[second]
        choice = choices[i]
        if choice < 4:
            score_person[first_index] += score_dic[choice]
        if choice > 4:
            score_person[second_index] += score_dic[choice]

    print(score_person)

    for i in range(0, 4 * 2, 2):
        first_score = score_person[i]
        second_score = score_person[i + 1]
        if first_score >= second_score:
            answer += persons[i]
        else:
            answer += persons[i + 1]

    return answer
