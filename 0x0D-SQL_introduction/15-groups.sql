-- lists the number of records with the same score in the table
-- A query that list the number of records with the same score
SELECT score, count(*) AS number FROM second_table GROUP BY score ORDER BY score;
