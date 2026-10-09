# Raw Data README: WoSIS Snapshot (December 2023)

This folder holds the original, unedited WoSIS download. **No file in `data_raw/` is ever modified.** All cleaning happens later, on copies, and cleaned data is saved separately in `data_processed/`.

## Dataset Source
- **Dataset:** Standardised soil profile data for the world (WoSIS snapshot, December 2023)
- **Provider:** ISRIC – World Soil Information (World Data Centre for Soils), Wageningen
- **Direct download link:** https://files.isric.org/public/wosis_snapshot/WoSIS_2023_December.zip
- **Dataset DOI:** https://doi.org/10.17027/isric-wdcsoils-20231130
- **Coverage (per the provider's readme):** 228k profiles from 217k geo-referenced sites in 174 countries, with over 900k soil layers and over 6 million records.

## Download Date
2026-10-02 (format: year-month-day)

## File Names and Format
- **Downloaded file:** `WoSIS_2023_December.zip`
- **Contents of the zip (per the provider's readme):**
  - `wosis_202312_observations.tsv`: catalogue of the measured properties
  - `wosis_202312_sites.tsv`: site locations
  - `wosis_202312_profiles.tsv`: one row per soil profile
  - `wosis_202312_layers.tsv`: soil layers (horizons) per profile
  - one `wosis_202312_xxxx.tsv` file per soil property
  - `wosis_202312.gpkg`: the same data as a GeoPackage (for spatial work later)
  - `Readme_WoSIS_202312_v2b.pdf`: the provider's documentation
- **Format:** TSV (tab-separated values), UTF-8 encoding, double quotation marks around text.
- **Extraction:** the zip was extracted with WinRAR.

## Files Used in This Project
| File | Property | Unit |
|---|---|---|
| `wosis_202312_orgc.tsv` | Organic carbon | g/kg |
| `wosis_202312_phaq.tsv` | pH (in water) | unitless |
| `wosis_202312_clay.tsv` | Clay | g/100g |
| `wosis_202312_sand.tsv` | Sand | g/100g |

All other files in the zip were left unused for now.

## Imported into PostgreSQL
- **Database:** `wosis_project`
- **Tables:** `wosis_orgc`, `wosis_phaq`, `wosis_clay`, `wosis_sand`
- **Method:** tables created with matching column types from the provider's readme, then loaded with the DBeaver Import Data tool (tab delimiter, UTF-8).
- **Row counts after import (whole world):** orgc 526,953; phaq 655,336; clay 652,347; sand 542,463.
- **Row counts for Ghana:** orgc 1,756; phaq 2,044; clay 801; sand 834.

## Citation
The provider asks that the citation always be quoted when the data are used:

> Calisto, L., de Sousa, L.M., Batjes, N.H., 2023. Standardised soil profile data for the world (WoSIS snapshot – December 2023), https://doi.org/10.17027/isric-wdcsoils-20231130

Supplement to:

> Batjes N.H., Calisto, L. and de Sousa L.M., 2023. Providing quality-assessed and standardised soil data to support global mapping and modelling (WoSIS snapshot 2023). Earth System Science Data, https://doi.org/10.5194/essd-2024-14

## Licence

The dataset contains three licences:

| Licence | Rows | Share |
|---------|------|-------|
| CC BY 4.0 | 955 | 54.4% |
| CC BY-NC 3.0 | 722 | 41.1% |
| CC BY 3.0 | 79 | 4.5% |

The 722 rows under CC BY-NC 3.0 (41.1%) cannot be used commercially without permission. All three licences require attribution.
