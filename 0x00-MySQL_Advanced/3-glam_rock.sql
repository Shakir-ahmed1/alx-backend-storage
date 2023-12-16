-- displays bands with style of Galm rock and their lifespan
SELECT band_name,
       IF(split IS NULL, 2020 - formed , split - formed) AS lifespan
FROM metal_bands
WHERE style REGEXP "Glam rock"
ORDER BY lifespan DESC
