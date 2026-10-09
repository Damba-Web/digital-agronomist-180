# Real Dataset Selection Note

## 1. Dataset name
Standardised soil profile data for the world (WoSIS snapshot, December 2023)

## 2. Source organization or authors
- **Organization:** ISRIC – World Soil Information (World Data Centre for Soils), Wageningen
- **Authors:** Calisto, L., de Sousa, L.M. and Batjes, N.H. (2023)

## 3. Download or access method
- The dataset is free to download from the ISRIC file server: https://files.isric.org/public/wosis_snapshot/WoSIS_2023_December.zip
- Dataset DOI: https://doi.org/10.17027/isric-wdcsoils-20231130
- Downloaded on 2026-10-02 and extracted from the zip file.
- The raw files are stored untouched in `data_raw/`. Four property files were imported into PostgreSQL (database `csa_soil_db`). Details are in `data_raw/README_raw_data.md`.

## 4. Variables available
The files used in this project:

| File | Property | Unit |
|---|---|---|
| `wosis_202312_orgc.tsv` | Organic carbon | g/kg |
| `wosis_202312_phaq.tsv` | pH (in water) | unitless |
| `wosis_202312_clay.tsv` | Clay | g/100g |
| `wosis_202312_sand.tsv` | Sand | g/100g |

Each file also holds the profile ID, layer ID, upper and lower depth (cm), the measured value (`value_avg`), country, longitude, latitude, sampling date and licence. The full snapshot contains many more properties (for example bulk density, total nitrogen and cation exchange capacity) that were left unused for now.

## 5. Geographic coverage
- **Full snapshot:** 228k profiles from 174 countries.
- **This project:** Ghana only.
- In the organic carbon table, all 1,756 Ghana rows belong to the WoSIS region "Western Africa".
- Sample locations range from 4.94 to 11.08 degrees north and from 2.97 degrees west to 0.37 degrees east, which is consistent with Ghana's borders.
- The Ghana subset has **318 distinct soil profiles** and 1,756 organic carbon layer measurements, about 5.5 layers per profile.
- Ghana rows in the other tables: pH 2,044; clay 801; sand 834.

## 6. Time coverage
- Sampling years run from **1949 to 2009** (organic carbon table, Ghana).
- 74 of the 1,756 rows (about 4%) have no usable date. The `date` column stores unknown parts as `?` (for example `????-??-??` or `2009-??-??`), so these will be treated as missing values during cleaning.
- The data contain no samples after 2009.

## 7. Why this dataset fits the project
*(Draft: read it, then rewrite it in your own words.)*

I chose this dataset because it meets every selection criterion in my curriculum:
- **Real, not simulated:** it is measured soil data compiled from real surveys.
- **Clear source:** it is published by ISRIC, a recognised soil data centre, with a DOI.
- **Downloadable:** it is free to download.
- **Usable variables:** it has organic carbon, pH, clay and sand, the core variables of soil health work.
- **Citation available:** the provider gives an exact citation.
- **Relevant to soil and climate-smart agriculture:** soil organic carbon is central to soil health and carbon storage.
- **Enough rows:** Ghana has 318 profiles and 1,756 organic carbon layers, with 801 to 2,044 rows for each of the other properties, which is enough for cleaning, statistics and charts.

It also suits a digital agronomy portfolio because it is messy in the way real data are. It comes as many linked files, has missing dates and uneven coverage, and so it lets me show a full workflow: database import, SQL joins, cleaning with documented rules, and analysis in Python.

## 8. Limitations
- The number of measurements per property varies greatly between profiles and depths, so coverage is uneven. Clay and sand have fewer Ghana rows than pH.
- Several layers come from one profile, so rows are not independent samples. There are 318 profiles behind the 1,756 organic carbon rows.
- The samples span 1949 to 2009, so values from different decades are mixed, and nothing is more recent than 2009. Conditions and laboratory methods changed over that time.
- About 4% of rows have an unknown date, recorded with `?` placeholders.
- Clay values are provided only where clay, silt and sand add up to between 90 and 100 percent, and the provider recommends normalising totals to 100 percent before modelling.
- The `value` and `method_options` columns contain complex text strings, so analysis uses `value_avg`, the average of the reported values.
- Data come from many source datasets with different laboratory methods, which adds uncertainty when values are compared.

## 9. Citation or acknowledgement requirement
The provider requires the citation to be quoted whenever the data are used:

> Calisto, L., de Sousa, L.M., Batjes, N.H., 2023. Standardised soil profile data for the world (WoSIS snapshot – December 2023), https://doi.org/10.17027/isric-wdcsoils-20231130

Supplement to:

> Batjes N.H., Calisto, L. and de Sousa L.M., 2023. Providing quality-assessed and standardised soil data to support global mapping and modelling (WoSIS snapshot 2023). Earth System Science Data, https://doi.org/10.5194/essd-2024-14

Each record also carries its own `licence` value set by the original data provider. See `data_raw/README_raw_data.md`.
