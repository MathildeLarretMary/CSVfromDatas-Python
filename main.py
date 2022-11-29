import requests
import pandas as pd
# import matplotlib.pyplot as plt

url_api = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"

class Request:
    def __init__(self, url) -> None:
        self.url = url

        while True :
           self.get_data(self.url) 
           break
           
    def get_data(self, url):
        # <Response [200]>
        req = requests.get(url)
        req_json = req.json()
        # print(req_json)
        self.datas_to_csv(req_json)
        self.use_csv('ResultsFile.csv')
        
    def datas_to_csv(self, response):
        datas = response["data"]
        df = pd.DataFrame(datas)
        df.to_csv('ResultsFile.csv', index=False, header=True)
        
    def use_csv(self, file):
        df = pd.read_csv(file)
        df = df.set_index('Year')
        df = df['Population']
        
        # TODO: make a graph -> pandas
        # df = pd.DataFrame(df)
        # # df.hist()
        print(df)



Request(url_api)