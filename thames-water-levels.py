
import pandas as pd                
from scipy.stats import iqr

# Define IQR function
def IQR(column): 
    q25, q75 = column.quantile([0.25, 0.75])
    return q75-q25

# Function to calculate tidal stats for every dataset

def tidal_stats(data):
    try:
        # set root_url to github path with data
        root_url = 'https://github.com/MyreLab/thames-tidal-variation/raw/main/datasets/' 

        # Load datasets
        df = pd.read_csv(root_url+data) 

        # Take only the first three columns
        df = df.iloc[:, :3]

        # Rename columns
        df.columns = ['datetime', 'water_level', 'is_high_tide']

        # Convert to datetime
        df['datetime'] = pd.to_datetime(df['datetime'])

        # Convert to float
        df['water_level'] = df.water_level.astype(float)

        # Create extra month and year columns
        df['month'] = df['datetime'].dt.month
        df['year'] = df['datetime'].dt.year

        # Filter df for high and low tide
        tide_high = df.query('is_high_tide==1')['water_level']
        tide_low = df.query('is_high_tide==0')['water_level']

        # Create summary statistics
        high_statistics = tide_high.agg(['mean', 'median', IQR])
        low_statistics = tide_low.agg(['mean', 'median', IQR])

        # Calculate ratio of high tide days
        all_high_days = df.query('is_high_tide==1').groupby('year').count()['water_level']

        high_days = df.query(f'(water_level>{tide_high.quantile(.75)}) & (is_high_tide==1)').groupby('year').count()['water_level']

        high_ratio = (high_days/all_high_days).reset_index()

        # Calculate ratio of low tide days
        all_low_days = df.query('is_high_tide==0').groupby('year').count()['water_level']

        low_days = df.query(f'(water_level<{tide_low.quantile(.25)}) & (is_high_tide==0)').groupby('year').count()['water_level']

        low_ratio = (low_days/all_low_days).reset_index()

        dictionary = {
            'high_statistics': high_statistics,
            'low_statistics': low_statistics,
            'high_ratio': high_ratio,
            'low_ratio':low_ratio}
        
    except:
        dictionary = 0

    return dictionary

# run tidal_stats function for all tidal gauges:

filenames = [
    '10-11_London_Bridge.txt',
    '12_All_Hallows_Pier.txt',
    '13_Temple_Pier.txt',
    '14_Strand_on_Green.txt',
    '15_Richmond.txt',
    '1_Walton_on_Naze.txt',
    '2_Margate.txt',
    '3_Shivering_Sand.txt',
    '4_Southend.txt',
    '5_Coryton.txt',
    '6_Tilbury.txt',
    '7-8_Silvertown.txt',
    '9_Cherry_Garden_Pier.txt',  
]

# create list to store the resulting tidal stats:

results_dict = {}

for dataset in filenames:
    results_dict[dataset.replace('.txt',"")] = tidal_stats(dataset)


results_dict['13_Temple_Pier']['high_ratio']