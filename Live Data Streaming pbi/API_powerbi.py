import pandas as pd
from datetime import datetime
from datetime import timedelta
import requests
import time
import random

#class for data_generation


def data_generation():
    surr_id = random.randint(1, 3)
    speed = random.randint(20,200)
    date = datetime.today().strftime("%Y-%m-%d")
    time = datetime.now().isoformat()

    return [surr_id, speed, date, time]


if __name__ == '__main__':

    REST_API_URL = 'https://api.powerbi.com/beta/05f72c84-5a2b-4523-9bab-9517d1da28c1/datasets/6c61e40d-90ed-4257-a20d-ba138a6e504e/rows?key=eGoJ00dXiRkZGKnNUO8xnwIvVIlgyglE6PlUTTamQKdbDvn4H4mDU6sGZTkZa6DgDxVPQCK2I7c7Fddcje6xiQ%3D%3D'

    while True:
        data_raw = []
        for i in range(1):
            row = data_generation()
            data_raw.append(row)
            print("Raw data - ", data_raw)

        # set the header record
        HEADER = ["surr_id", "speed", "date", "time"]

        data_df = pd.DataFrame(data_raw, columns=HEADER)
        data_json = bytes(data_df.to_json(orient='records'), encoding='utf-8')
        print("JSON dataset", data_json)

        # Post the data on the Power BI API
        req = requests.post(REST_API_URL, data_json)

        print("Data posted in Power BI API")
        time.sleep(2)