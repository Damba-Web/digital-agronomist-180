# Question 8: Show all soil samples with their management practices (crop_type, tillage_type, fertilizer_kg_ha). Include samples that have no management data.
    SELECT *, crop_type, tillage_type, fertilizer_kg_ha
    FROM soil_samples ss
    LEFT JOIN management_practices mp ON mp.sample_id = ss.sample_id;

# Question 9: Show all soil samples with their climate data (annual_rainfall_mm, mean_temperature_c) for each district.
    SELECT *
    FROM soil_samples ss
    JOIN climate_normals cn ON cn.district = ss.district

# Question 10: Create a combined view showing:
    SELECT ss.sample_id, 
    cn.district, 
    land_use, 
    soc_percent, 
    clay_percent, 
    ph, 
    annual_rainfall_mm, 
    mean_temperature_c, 
    tillage_type, 
    residue_retention, 
    irrigation_status
    FROM soil_samples ss 
    JOIN climate_normals cn ON cn.district = ss.district
    JOIN management_practices mp ON mp.sample_id = ss.sample_id;

