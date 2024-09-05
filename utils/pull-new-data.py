from bs4 import BeautifulSoup
import requests
import os 

class PullData :
    
    def init(self, season = "2024/2025") : 
        self.url = "https://www.football-data.co.uk"
        self.belgium = "/belgiumm.php"
        self.season = f"Season {season}"
        self.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": f"{self.url}{self.belgium}",
}

    def pull_data(self) : 
        response = requests.get(f"{self.url}{self.belgium}", headers=self.headers)
        if response.status_code == 200 : 
            soup = BeautifulSoup(response.text, "html.parser")
            last_season = soup.find("i", string = self.season) 
            
            if last_season : 
                csv_url = last_season.find_next("a")["href"]
                print(csv_url)
                csv_response = requests.get(f"{self.url}/{csv_url}")
                print(csv_response)
                
                if csv_response.status_code == 200 : 
                    with open("data/csv/test.csv", "w+" ) as f : 
                        f.write(csv_response.text)
                        if os.stat("data/csv/B1.csv").st_size < os.stat("data/csv/test.csv").st_size : 
                            os.remove("data/csv/B1.csv")
                            os.rename("data/csv/test.csv", "data/csv/B1.csv")
                    print("done!")
                else:
                    print("Error writing file")
            else : 
                print(f"Didn't found the 'i' tag with the {self.season} text")
        else :
            print("Error")