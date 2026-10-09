WITH scored_fields AS (
    SELECT 
        s.sample_id,
        s.district,
        s.land_use,
        s.soc_percent,
        s.clay_percent,
        s.ph,
        m.tillage_type,
        m.residue_retention,
        
        (CASE WHEN s.soc_percent < 1.0 THEN 3 ELSE 0 END +
         CASE WHEN s.clay_percent > 25 THEN 2 ELSE 0 END +
         CASE WHEN s.ph BETWEEN 6.0 AND 7.5 THEN 1 ELSE 0 END +
         CASE WHEN m.tillage_type IN ('No-till', 'Reduced') THEN 2 ELSE 0 END +
         CASE WHEN m.residue_retention IN ('Fully retained', 'Some retained') THEN 2 ELSE 0 END +
         CASE WHEN s.land_use IN ('Cropland', 'Pasture') THEN 1 ELSE 0 END
        ) AS carbon_score
    FROM soil_samples s
    LEFT JOIN management_practices m ON s.sample_id = m.sample_id
)
SELECT 
    *,
    CASE 
        WHEN carbon_score >= 8 THEN 'High Opportunity'
        WHEN carbon_score BETWEEN 5 AND 7 THEN 'Moderate Opportunity'
        ELSE 'Low Opportunity'
    END AS opportunity_class
FROM scored_fields
ORDER BY carbon_score DESC;