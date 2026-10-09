-- ============================================
-- CREATE DATABASE
-- ============================================

CREATE DATABASE csa_soil_project;

\c csa_soil_project;

-- ============================================
-- TABLE 1: SOIL SAMPLES
-- ============================================

CREATE TABLE soil_samples (
    sample_id INTEGER PRIMARY KEY,
    district TEXT NOT NULL,
    community TEXT,
    latitude NUMERIC(9,6),
    longitude NUMERIC(9,6),
    land_use TEXT,
    soc_percent NUMERIC(5,2),
    clay_percent NUMERIC(5,2),
    sand_percent NUMERIC(5,2),
    ph NUMERIC(4,2),
    sampling_year INTEGER,
    CONSTRAINT check_soc_non_negative CHECK (soc_percent >= 0),
    CONSTRAINT check_ph_range CHECK (ph BETWEEN 3.0 AND 10.0),
    CONSTRAINT check_clay_range CHECK (clay_percent BETWEEN 0 AND 100),
    CONSTRAINT check_sand_range CHECK (sand_percent BETWEEN 0 AND 100)
);

-- ============================================
-- TABLE 2: CLIMATE NORMALS
-- ============================================

CREATE TABLE climate_normals (
    climate_id INTEGER PRIMARY KEY,
    district TEXT NOT NULL UNIQUE,
    annual_rainfall_mm NUMERIC(7,2),
    mean_temperature_c NUMERIC(4,2),
    dry_season_length_days INTEGER,
    rainy_season_start TEXT,  -- Month name or 'YYYY-MM'
    rainy_season_end TEXT
);

-- ============================================
-- TABLE 3: MANAGEMENT PRACTICES
-- ============================================

CREATE TABLE management_practices (
    management_id INTEGER PRIMARY KEY,
    sample_id INTEGER REFERENCES soil_samples(sample_id),
    crop_type TEXT,
    tillage_type TEXT CHECK (tillage_type IN ('Conventional', 'Reduced', 'No-till')),
    fertilizer_kg_ha NUMERIC(7,2),
    residue_retention TEXT CHECK (residue_retention IN ('All removed', 'Some retained', 'Fully retained')),
    irrigation_status TEXT CHECK (irrigation_status IN ('Rainfed', 'Irrigated', 'Supplemental')),
    notes TEXT
);