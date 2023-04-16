# River Thames Tidal Variation

Time series analysis of historical sea level records for every gauge along River Thames, 1911-1995. Using machine learning, an isolation forest model was used to identify anomalies in the water level data. Results were plotted using Bokeh.


Methods:
- Wrote function to import and load 13 datasets, one for each tidal gauge
- Performed manipulation, cleaning, and merging to prepare datasets for analysis
- Defined interquartile range function and used it to calculate summary statistics
- Calculated ratios based on high tide and low tide statistics
- Wrote for loops to generate line plots displaying monthly average water levels (with confidence intervals) across all years for each gauge location 
- Wrote for loops to generate boxplots and inspect water level distributions for each gauge location
- Fit an isolation forest model to identify anomalies in the water level data and plotted the results using Bokeh

<p><img style="float: right ; margin: 5px 20px 5px 10px; width: 55%" src="https://github.com/MyreLab/thames-tidal-variation/blob/main/thames-tidal-anomalies.png?raw=true"></p>

Data sources:
- [The British National Oceanography Centre](https://www.bodc.ac.uk/data/published_data_library/catalogue/10.5285/b66afb2c-cd53-7de9-e053-6c86abc0d251)
- [Digitising historical sea level records in the Thames Estuary](https://doi.org/10.1038/s41597-022-01223-7)


