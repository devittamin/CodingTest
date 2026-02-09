
# mean 아니고 averagae 아니고 avg,, 
# 10cm 이하일 경우에는 LENGTH 가 NULL
# ifnull(~,10) 널이면 10으로 반환 
# round(~,2) 소수점 둘째자리까지 반올림 = 셋째자리에서 반올림
SELECT ROUND(AVG(IFNULL(LENGTH, 10)), 2) AS AVERAGE_LENGTH 
FROM FISH_INFO;
