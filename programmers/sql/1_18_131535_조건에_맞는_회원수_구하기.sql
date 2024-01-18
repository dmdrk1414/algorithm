-- https://school.programmers.co.kr/learn/courses/30/lessons/131535
-- 2021년에 가입한 회원 중 나이가 20세 이상 29세 이하인 회원은 USER_ID 가 1, 3, 5 인 회원들 이므로, 다음과 같이 결과가 나와야 합니다.

SELECT COUNT(USER_ID) AS USERS
FROM USER_INFO
WHERE LEFT(JOINED,4) = 2021 AND AGE BETWEEN 20 AND 29;

SELECT COUNT(USER_ID) AS USERS
FROM USER_INFO
WHERE SUBSTRING(JOINED, 1, 4) = '2021'
  AND AGE >= 20 AND AGE <= 29

SELECT COUNT(USER_ID) AS USERS
FROM USER_INFO
WHERE DATE_FORMAT(JOINED, '%Y') = '2021'
  AND AGE >= 20 AND AGE <= 29