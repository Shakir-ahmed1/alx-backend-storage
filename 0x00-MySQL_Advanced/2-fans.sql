-- group by country
SELECT origin, SUM(nb_fans) AS nb_fans
FROM bands
GROUP BY origin
ORDER BY nb_fans DESC;

