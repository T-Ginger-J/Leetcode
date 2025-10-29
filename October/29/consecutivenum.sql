SELECT DISTINCT Num AS ConsecutiveNums
FROM (
  SELECT Num,
         LAG(Num) OVER (ORDER BY Id) AS prev_num,
         LEAD(Num) OVER (ORDER BY Id) AS next_num
  FROM Logs
) t
WHERE Num = prev_num AND Num = next_num;
