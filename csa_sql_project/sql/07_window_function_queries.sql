Question 13: Rank all samples by SOC from highest to lowest. Use ROW_NUMBER() and RANK() to see the difference
    SELECT soc_percent,
    row_number() over(ORDER BY soc_percent),
    rank() OVER (ORDER BY soc_percent)
    FROM soil_samples

Question 14: For each district, rank the samples by SOC from highest to lowest using PARTITION BY
    SELECT district, soc_percent,
    Dense_rank() OVER (PARTITION BY district ORDER BY soc_percent)
    FROM soil_samples;

Question 15: For each district, show:
district
sample_id
soc_percent
The difference between each sample's SOC and the previous sample's SOC in that district (sorted by SOC descending)
    SELECT district, 
    sample_id, 
    soc_percent,
    soc_percent - LAG(soc_percent, 1) OVER (PARTITION BY district ORDER BY soc_percent DESC) AS soc_difference
    FROM soil_samples;