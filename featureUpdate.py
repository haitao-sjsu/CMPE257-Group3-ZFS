import json
import pandas as pd
from featureExtraction import extract_accomodation_details

df = pd.read_excel('Dataset_For_Recommendation/OFFICIAL_Labeling_dataset_facebook-groups-scraper_raw_SVM_PREDICTIONS.xlsx')

# featureNames= ['rent','location','fromDate','toDate','bedrooms','bathrooms','amenities']
# for feature in featureNames:
#     df[feature] = ""



for index, row in df.iloc[800:1000].iterrows():
    print('=============================================================================================================================')
    response = ""
    print(row['Supply(Selling)_or_Demand(Buying)'] != 'Unknown')
    print(index)
    if(pd.notna(row['text']) and row['Supply(Selling)_or_Demand(Buying)'] != 'Unknown') :
        response = extract_accomodation_details(row['text'])
    
        if(pd.notna(response)):
            response = json.loads(response)
        print(response)

    
        if 'rent' in response:
            df.at[index, 'rent'] = response['rent']
        else:
            df.at[index, 'rent'] = None

        if 'location' in response:
            df.at[index, 'location'] = response['location']
        else:
            df.at[index, 'location'] = None

        if 'fromDate' in response:
            df.at[index, 'fromDate'] = response['fromDate']
        else:
            df.at[index, 'fromDate'] = None

        if 'toDate' in response:
            df.at[index, 'toDate'] = response['toDate']
        else:
            df.at[index, 'toDate'] = None

        if 'bedrooms' in response:
            df.at[index, 'bedrooms'] = response['bedrooms']
        else:
            df.at[index, 'bedrooms'] = None

        if 'bathrooms' in response:
            df.at[index, 'bathrooms'] = response['bathrooms']
        else:
            df.at[index, 'bathrooms'] = None

        if 'amenities' in response:
            df.at[index, 'amenities'] = ', '.join(response['amenities'])
        else:
            df.at[index, 'amenities'] = None


df.to_excel('Dataset_For_Recommendation/OFFICIAL_Labeling_dataset_facebook-groups-scraper_raw_SVM_PREDICTIONS.xlsx', index=False)