1. WITH get_win (client_number, win) AS (SELECT client_number, count(outcome)
                                      FROM event_value
                                               JOIN bid USING (play_id)
                                      WHERE coefficient = value
                                        AND outcome = 'win'
                                      GROUP BY client_number),
     get_lose (client_number, lose) AS (SELECT client_number, count(outcome)
                                        FROM event_value
                                                 JOIN bid USING (play_id)
                                        WHERE coefficient = value
                                          AND outcome = 'lose'
                                        GROUP BY client_number)
SELECT client_number, win as Побед, lose as Поражений
FROM get_win
         JOIN get_lose USING (client_number)
ORDER BY 1;


1.1 SELECT client_number, sum(if(outcome = 'win', 1, 0)) as Побед, sum(if(outcome = 'lose', 1, 0)) as Поражений
FROM event_value
         JOIN bid USING (play_id)
WHERE coefficient = value
GROUP BY client_number
ORDER BY 1;


2. SELECT IF(home_team < away_team, CONCAT_WS('-', home_team, away_team), CONCAT_WS('-', away_team, home_team)) as game,
       COUNT(1)                                                                                              as games_count
FROM event_entity
GROUP BY 1
ORDER BY 2, 1;