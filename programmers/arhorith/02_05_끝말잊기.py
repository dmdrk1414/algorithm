# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = []
    turn = 0
    wordList = [words[0]]
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for idx in range(1, len(words)):
        if words[idx - 1][-1] != words[idx][0]:
            turn = idx
            break
        if words[idx] in wordList:
            turn = idx
            break
        wordList.append(words[idx])
    if turn == 0:
        return [0, 0]
    # 가장 먼저 탈락하는 사람의 번호
    # 그 사람이 자신의 몇 번째 차례에 탈락하는지
    print(turn % n + 1)
    return [turn % n + 1, turn // n + 1]


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
