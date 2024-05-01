import json
import csv

FILENAME = 'Dataset_Raw_From_Facebook/dataset_facebook-groups-scraper_2024-03-02_22-11-37-739_raw.json'

def read_posts_from_file(FileName=FILENAME):
    with open(FileName, 'r') as jsonFile:
        data = json.load(jsonFile)
        return [post['text'] for post in data]        

def generate_all_posts(FileName=FILENAME):
    """This function is used for generate post_*.txt in directory Dataset_Classification. Not used in the project"""
    with open(FileName, 'r') as CsvFile:
        reader = csv.reader(CsvFile)
        data = list(reader)
        for i in range(2, len(data)):
            PostName = f'Dataset_Classification/post_{i - 1}.txt'
            with open(PostName, 'w') as PostFile:
                PostFile.write(data[i][1])