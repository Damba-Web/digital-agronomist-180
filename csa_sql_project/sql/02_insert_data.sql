-- ============================================
-- INSERT SOIL SAMPLES
-- ============================================

INSERT INTO soil_samples (
    sample_id, district, community, latitude, longitude, 
    land_use, soc_percent, clay_percent, sand_percent, ph, sampling_year
) VALUES
-- Ejura District
(1, 'Ejura', 'Agogo', 7.123456, -1.234567, 'Cropland', 1.25, 25.00, 60.00, 6.20, 2023),
(2, 'Ejura', 'Agogo', 7.134567, -1.245678, 'Cropland', 0.85, 30.00, 55.00, 5.80, 2023),
(3, 'Ejura', 'Nkwanta', 7.145678, -1.256789, 'Fallow', 1.80, 22.00, 65.00, 6.50, 2023),
(4, 'Ejura', 'Nkwanta', 7.156789, -1.267890, 'Pasture', 2.10, 20.00, 68.00, 6.80, 2023),
(5, 'Ejura', 'Kasei', 7.167890, -1.278901, 'Cropland', 0.95, 28.00, 58.00, 5.50, 2023),
-- Nsawam District
(6, 'Nsawam', 'Adoagyiri', 5.789012, -0.456789, 'Forest', 3.10, 35.00, 45.00, 5.80, 2022),
(7, 'Nsawam', 'Adoagyiri', 5.798123, -0.467890, 'Forest', 2.80, 38.00, 42.00, 5.50, 2022),
(8, 'Nsawam', 'Koforidua', 5.807234, -0.478901, 'Cropland', 1.40, 32.00, 50.00, 6.10, 2022),
(9, 'Nsawam', 'Koforidua', 5.816345, -0.489012, 'Cropland', 1.10, 30.00, 55.00, 6.30, 2022),
-- Tamale District
(10, 'Tamale', 'Gumani', 9.345678, -0.987654, 'Cropland', 0.85, 15.00, 75.00, 7.50, 2024),
(11, 'Tamale', 'Gumani', 9.356789, -0.998765, 'Fallow', 1.20, 18.00, 72.00, 6.80, 2024),
(12, 'Tamale', 'Vitting', 9.367890, -1.009876, 'Cropland', 0.65, 20.00, 70.00, 7.20, 2024),
-- Kumasi District
(13, 'Kumasi', 'Kentinkrono', 6.654321, -1.654321, 'Pasture', 1.80, 30.00, 50.00, 6.70, 2023),
(14, 'Kumasi', 'Kentinkrono', 6.665432, -1.665432, 'Cropland', 1.50, 28.00, 52.00, 5.90, 2023),
(15, 'Kumasi', 'Asokwa', 6.676543, -1.676543, 'Forest', 2.50, 40.00, 40.00, 5.20, 2023),
(16, 'Kumasi', 'Asokwa', 6.687654, -1.687654, 'Fallow', 1.90, 32.00, 48.00, 6.50, 2023),
-- Akatsi District
(17, 'Akatsi', 'Ave-Dakpa', 6.111222, 0.888999, 'Cropland', 2.05, 40.00, 40.00, 5.50, 2025),
(18, 'Akatsi', 'Ave-Dakpa', 6.122333, 0.889000, 'Cropland', 1.80, 42.00, 38.00, 5.30, 2025),
(19, 'Akatsi', 'Dzodze', 6.133444, 0.890001, 'Fallow', 2.20, 38.00, 42.00, 5.80, 2025),
(20, 'Akatsi', 'Dzodze', 6.144555, 0.891002, 'Pasture', 2.50, 35.00, 45.00, 6.00, 2025);

-- ============================================
-- INSERT CLIMATE NORMALS
-- ============================================

INSERT INTO climate_normals (
    climate_id, district, annual_rainfall_mm, mean_temperature_c, 
    dry_season_length_days, rainy_season_start, rainy_season_end
) VALUES
(1, 'Ejura', 1400.00, 26.50, 90, 'April', 'October'),
(2, 'Nsawam', 1200.00, 27.00, 100, 'April', 'October'),
(3, 'Tamale', 1100.00, 28.50, 120, 'May', 'September'),
(4, 'Kumasi', 1600.00, 25.80, 70, 'March', 'November'),
(5, 'Akatsi', 800.00, 29.00, 150, 'April', 'October');

-- ============================================
-- INSERT MANAGEMENT PRACTICES
-- ============================================

INSERT INTO management_practices (
    management_id, sample_id, crop_type, tillage_type, 
    fertilizer_kg_ha, residue_retention, irrigation_status, notes
) VALUES
-- Ejura samples
(1, 1, 'Maize', 'Reduced', 60.00, 'Some retained', 'Rainfed', ''),
(2, 2, 'Maize', 'Conventional', 80.00, 'All removed', 'Rainfed', ''),
(3, 3, NULL, NULL, NULL, NULL, NULL, 'Fallow field - no management'),
(4, 4, NULL, NULL, NULL, NULL, NULL, 'Pasture - no tillage'),
(5, 5, 'Cassava', 'Reduced', 40.00, 'Some retained', 'Rainfed', ''),
-- Nsawam samples
(6, 6, NULL, NULL, NULL, NULL, NULL, 'Forest - natural'),
(7, 7, NULL, NULL, NULL, NULL, NULL, 'Forest - natural'),
(8, 8, 'Rice', 'No-till', 50.00, 'Fully retained', 'Irrigated', ''),
(9, 9, 'Maize', 'Reduced', 70.00, 'Some retained', 'Rainfed', ''),
-- Tamale samples
(10, 10, 'Sorghum', 'Conventional', 30.00, 'All removed', 'Rainfed', ''),
(11, 11, NULL, NULL, NULL, NULL, NULL, 'Fallow field - no management'),
(12, 12, 'Cowpea', 'No-till', 20.00, 'Fully retained', 'Rainfed', ''),
-- Kumasi samples
(13, 13, NULL, NULL, NULL, NULL, NULL, 'Pasture - no tillage'),
(14, 14, 'Maize', 'Reduced', 80.00, 'Some retained', 'Rainfed', ''),
(15, 15, NULL, NULL, NULL, NULL, NULL, 'Forest - natural'),
(16, 16, NULL, NULL, NULL, NULL, NULL, 'Fallow - no management'),
-- Akatsi samples
(17, 17, 'Maize', 'Conventional', 100.00, 'All removed', 'Supplemental', ''),
(18, 18, 'Cassava', 'Reduced', 60.00, 'Some retained', 'Rainfed', ''),
(19, 19, NULL, NULL, NULL, NULL, NULL, 'Fallow - no management'),
(20, 20, NULL, NULL, NULL, NULL, NULL, 'Pasture - no tillage');