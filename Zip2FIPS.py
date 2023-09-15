import pandas as pd
import inspect
from uszipcode import SearchEngine

# Load the CSV file into a DataFrame
csv_file = '/Users/thomasss/Desktop/canvaslot/dirtyData/shortened9to5digitZipOrders.csv'
data = pd.read_csv(csv_file, na_filter=False)
# Initialize the SearchEngine
search = SearchEngine()

# Lists to store extracted information
latitudes = []
longitudes = []
counties = []
states = []

# Iterate through each row in the DataFrame
for index, row in data.iterrows():
    zipcode = row['address_zip']
    if zipcode =='NULL':
        #result = search.by_zipcode(zipcode)
        latitudes.append(None)
        longitudes.append(None)
        counties.append(None)
        states.append(None) 
    else:
        try:
                result = search.by_zipcode(zipcode)
                lat = result.lat
                long = result.lng
                county = result.county
                state = result.state
                latitudes.append(lat)
                longitudes.append(long)
                counties.append(county)
                states.append(state)
        except AttributeError:
                latitudes.append(None)
                longitudes.append(None)
                counties.append(None)
                states.append(None)
       
# Add new columns to the DataFrame
data['latitudes'] = latitudes
data['longitudes'] = longitudes
data['counties'] = counties
data['states'] = states

output_csv = 'cleaned9digitOrdersWithStatesCounties.csv'
#data.to_csv(output_csv, index=False)
print(data)
print('added states and counties and lats/longs 💯💯')