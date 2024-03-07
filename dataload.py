import csv
from classification import is_leasing_post

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
            if is_leasing_post(data_slice[i][1]):
                posts.append(data_slice[i][1])
        return posts
