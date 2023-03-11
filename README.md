# River Thames Tidal Variation

Time series analysis of historical sea level records for every gauge along River Thames, 1911-1995.

Steps:
- Wrote function to import and load 13 datasets, one for each tidal gauge
- Defined interquartile range function
- Performed manipulation to create datetime columns
- Filtered dataframes for high tide and low tide, based on water level data
- Calculated ratio for days with highest tide and days with lowest tide
- Wrote function to generate boxplots showing water level distribution for each tidal gauge

Sources:
- [The British National Oceanography Centre](https://www.bodc.ac.uk/data/published_data_library/catalogue/10.5285/b66afb2c-cd53-7de9-e053-6c86abc0d251)
- [Digitising historical sea level records in the Thames Estuary](https://doi.org/10.1038/s41597-022-01223-7)


