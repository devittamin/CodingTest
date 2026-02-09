# where 절에 집계함수 못 쓴다
# 붙일 때 concat
SELECT CONCAT(MAX(LENGTH),'cm') AS MAX_LENGTH
FROM FISH_INFO;
