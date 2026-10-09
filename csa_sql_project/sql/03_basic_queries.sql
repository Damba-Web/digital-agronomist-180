# Question 1: Show all soil samples from Ejura district
SELECT * 
FROM soil_samples 
WHERE district = 'Ejura';

# Question 2: Show all samples with low SOC (below 1.0%) and acidic pH (below 5.5)
SELECT * 
FROM soil_samples 
WHERE soc_percent < 1.0 AND ph < 5.5

# Question 3: Show all Cropland samples sorted by SOC from highest to lowest
SELECT * 
FROM soil_samples
WHERE land_use = 'Cropland'
ORDER BY soc_percent DESC;

# Question 4:  Find all samples where clay is between 25% and 40% and sand is below 60%
SELECT * 
FROM soil_samples
WHERE clay_percent BETWEEN 25 AND 40 AND sand_percent < 60;

