# Question 11: Find all fields where the SOC is below the average SOC of the entire dataset. Show the sample_id, district, soc_percent, and the difference from the average.
    WITH
    soil_organic_avg AS 
    (SELECT AVG(soc_percent) AS avg_soc
    FROM soil_samples)
    SELECT sample_id, district, soc_percent, (soc_percent - (SELECT *FROM soil_organic_avg)) AS soc_diff
    FROM soil_samples
    WHERE soc_percent < (SELECT *FROM soil_organic_avg);

# Question 12; For each district, calculate the average SOC and the number of samples. Then find districts where the average SOC is below the overall average.
WITH 
soc_avg_count AS 
	(SELECT district, Count(*) AS sample_count,
	AVG(soc_percent) AS avg_soc
	FROM soil_samples
	GROUP BY district),
average_soc AS 
	(SELECT AVG(soc_percent) FROM soil_samples)
SELECT district, avg_soc, sample_count
FROM soc_avg_count sac
WHERE avg_soc < (SELECT * FROM average_soc);