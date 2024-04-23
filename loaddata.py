import csv
from classification import classification, POST_FROM_LANDLORD

FILENAME = 'Dataset_Raw_From_Facebook/dataset_facebook-groups-scraper_2024-03-02_22-11-37-739_raw_overview.csv'
SIZE = 5

def read_posts_from_file(FileName=FILENAME, Size=SIZE):
    posts = []
    with open(FileName, 'r') as CsvFile:
        reader = csv.reader(CsvFile)
        data = list(reader)
        #We skip the row 0 and 1 since they do not have valuable data
        data_slice = data[2:Size + 2]
        for i in range(SIZE):
            if classification(data_slice[i][1]) == POST_FROM_LANDLORD:
                posts.append(data_slice[i][1])
        return posts

user_query= f"""
Hello everyone! I am looking for some room for the Sp24. Below are some requirements:

- I am a guy, a SJSU international stduent not having SSN/income/credit score yet.
- budget <$1300
- walkable/ridable distance to campus
- single room required, open to shared bathroom
- cooking enabled in the kitchen
- quiet environment preferred
- SJSU student housemates preferred

Please DM me if you are looking for a roommate or have a room available. Thank you!
"""

def generate_all_posts(FileName=FILENAME):
    """This function is used for generate post_*.txt in directory Dataset_For_Classification. Not used in the project"""
    with open(FileName, 'r') as CsvFile:
        reader = csv.reader(CsvFile)
        data = list(reader)
        for i in range(2, len(data)):
            PostName = f'Dataset_For_Classification/post_{i - 1}.txt'
            with open(PostName, 'w') as PostFile:
                PostFile.write(data[i][1])

