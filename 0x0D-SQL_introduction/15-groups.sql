-- Lists all the records with the same score in the second_table of hbtn_0c_0 in MySQL server
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
