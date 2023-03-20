import pandas as pd
import numpy as np
import os
from natsort import natsorted

class SplitAndProcessVideos():

    """ Takes as input a data folder path with full raw data videos, splits them
    into individual videos lasting as long as the stimulus and saves them in the
    split_videos_data folder which will later be put through an analysis pipeline"""

    def __init__(self,folder_path:str,output_folder_path):
        self.folder_path = folder_path
        self.output_folder_path = output_folder_path
        self.movie_data = None
        self.csv_data = None


    @staticmethod
    def folder_input():
        return SplitAndProcessVideos(
            input('Path of folder to process: ')
        )

    def load_data(self):
        folder = os.fsencode(self.folder_path)
        filenames_movies = []
        filenames_csv = []
        for file in natsorted(os.listdir(folder)):
            filename = os.fsdecode(file)
            if filename.endswith('.avi'):
                filenames_movies.append(filename)
            if filename.endswith('.csv'):
                filenames_csv.append(filename)
        print(f'Movie filenames: {filenames_movies}')
        print(f'CSV filenames: {filenames_csv}')

        self.csvdata = [pd.read_csv(os.path.join(self.folder_path, f)) for f in filenames_csv]
        self.movie_data = []

        return self.movie_data, self.csv_data
