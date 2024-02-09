# AI 엔지니어인 현식이는 데이터를 분석하는 작업을 진행하고 있습니다.
# 데이터는 ["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"]으로
# 구성되어 있으며 현식이는 이 데이터들 중 조건을 만족하는 데이터만 뽑아서 정렬하려 합니다.
#
# 예를 들어 다음과 같이 데이터가 주어진다면

# 정렬한 데이터들이 담긴 이차원 정수 리스트 data와
# 어떤 정보를 기준으로 데이터를 뽑아낼지를 의미하는 문자열 ext,
# 뽑아낼 정보의 기준값을 나타내는 정수 val_ext,
# 정보를 정렬할 기준이 되는 문자열 sort_by가 주어집니다.

def solution(data, ext, val_ext, sort_by):
    col_order = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    filtered_data = [x for x in data if x[col_order[ext]] < val_ext]
    filtered_data.sort(key=lambda x: x[col_order[sort_by]])


    return filtered_data