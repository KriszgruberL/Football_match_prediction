from datetime import datetime
from bs4 import BeautifulSoup
import requests
import os 
import pandas as pd

class PullData :
    def __init__(self, season = "2024/2025") : 
        self.url = "https://www.football-data.co.uk"
        self.belgium = "/belgiumm.php"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Referer": f"{self.url}{self.belgium}",
    }
        
    def transform_season(self, season):
        # Split the string on "/"
        parts = season.split("/")
        # Extract the last two digits of each part and join them with an underscore
        return f"{parts[0][-2:]}_{parts[1][-2:]}"
        
    def save_csv_if_new(self,csv_response, file_path) :
        """Helper function to save the CSV file if it's new or larger."""
        if not os.path.exists(file_path) or os.stat(file_path).st_size < len(csv_response.text.encode('utf-8')):
            if not os.path.exists(file_path) : 
                print(f"File created at {file_path}.")
            elif os.stat(file_path).st_size < len(csv_response.text.encode('utf-8')) : 
                print(f"File updated at {file_path}.")
                
            with open(file_path, "w+") as f:
                f.write(csv_response.text)
        else:
            print("There is no new data.")

    def pull_one_data(self, season):
        response = requests.get(f"{self.url}{self.belgium}", headers=self.headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            last_season = soup.find("i", string=f"Season {season}")

            if last_season:
                csv_url = last_season.find_next("a")["href"]
                print(f"Found CSV URL: {csv_url}")
                csv_response = requests.get(f"{self.url}/{csv_url}")

                if csv_response.status_code == 200:
                    if not os.path.exists("data/csv"):
                        os.makedirs("data/csv")
                    csv_path = f"data/csv/{self.transform_season(season)}_B1.csv"
                    self.save_csv_if_new(csv_response, csv_path)
                    print("done!")
                else:
                    print("Error fetching CSV file.")
            else:
                print(f"Couldn't find the 'i' tag with the {self.season} text.")
        else:
            print("Error fetching the main page.")

            
    def pull_datas(self, seasons):
        current_year = datetime.now().year
        for season in seasons:
            start_year = int(season.split('/')[0])
            
            if season == f"{current_year}/{current_year + 1}":  # Always scrape the current season
                print(f"{file_name} is for the current season. Scraping data.")
                self.pull_one_data(season)  # Scrape for the current season
            elif start_year <= current_year:
                file_name = self.transform_season(season) + "_B1.csv"
                file_path = os.path.join("data/csv/", file_name)
                
                if not os.path.exists(file_path):
                    print(f"{file_name} does not exist. Scraping data for {season}.")
                    self.pull_one_data(season)  # Your scraping function here
                else:
                    print(f"{file_name} exists. Skipping scraping.")
            
if __name__ == "__main__" : 
    pull = PullData()
    seasons = ["2010/2011", "2011/2012", "2012/2013", "2013/2014", "2014/2015", "2015/2016", "2016/2017", "2017/2018", "2018/2019", "2019/2020", "2020/2021", "2021/2022", "2022/2023", "2023/2024", "2024/2025"]
    pull.pull_datas(seasons)