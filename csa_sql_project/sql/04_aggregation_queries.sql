# Question 5: Calculate the average SOC, average pH, and average clay for the entire dataset.

SELECT AVG(soc_percent) AS avg_soc, 
    AVG(ph) AS avg_ph,
    AVG(clay_percent) AS avg_clay
    FROM soil_samples;

# Question 6: Show the average SOC by land use (Cropland, Forest, Fallow, Pasture
SELECT land_use, 
AVG(soc_percent) AS soc_avg
FROM soil_samples
GROUP BY land_use;

# Question 7: Show the average SOC by district, sorted from highest to lowest.
SELECT district, 
AVG(soc_percent) AS soc_avg
FROM soil_samples
GROUP BY district
ORDER BY soc_avg DESC;