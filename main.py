def time_convert(t):
    year, month, day = map(int, t.split('.'))
    return year * 12 * 28 + month * 28 + day


def solution(today, terms, privacies):
    term_dict = dict()
    todayTotal = time_convert(today)
    answer = []

    for term in terms:
        nameType, period = term.split()
        term_dict[nameType] = int(period) * 28
        print(term_dict)

    for idx, privacy in enumerate(privacies):
        privaciesPriod, nameType = privacy.split()
        privacieTotalDay = time_convert(privaciesPriod) + term_dict[nameType]
        if privacieTotalDay <= todayTotal:
            answer.append(idx + 1)
    return answer


today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
answer = solution(today=today, terms=terms, privacies=privacies)

print(answer)
