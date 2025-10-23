from kaggle.api.kaggle_api_extended import KaggleApi
import os
import zipfile

class DataExtractor:
    def __init__(self, competition_name='digit-recognizer', data_dir='MNIST'):
        self.api = KaggleApi()
        self.api.authenticate()
        self.competition_name = competition_name
        self.data_dir = data_dir

    def download_and_extract(self):
        print(f'Downloading data for competition: {self.competition_name}')
        os.makedirs(self.data_dir, exist_ok=True)
        self.api.competition_download_files(self.competition_name, path=self.data_dir)
        zip_path = os.path.join(self.data_dir, f'{self.competition_name}.zip')
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.data_dir)
            print(f'Extracted files: {zip_ref.namelist()}')
        os.remove(zip_path)
        print(f'Data extracted to {self.data_dir}')


if __name__ == '__main__':
    extractor = DataExtractor()
    extractor.download_and_extract()