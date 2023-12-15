-- galm rock
SELECT band_name, 
       IF(splitted = 1, 2022 - CAST(SUBSTRING_INDEX(founded, '-', 1) AS SIGNED), 
                      2022 - CAST(founded AS SIGNED)) AS lifespan
FROM bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
