import pandas as pd
from datetime import datetime
from datetime import timedelta
import requests
import time
import random

##class for data_generation


def data_generation():
    surr_id = random.randint(1, 3)
    speed = random.randint(20,200)
    date = datetime.today().strftime("%Y-%m-%d")
    time = datetime.now().isoformat()

    return [surr_id, speed, date, time]


if __name__ == '__main__':

        data_raw = []
        for i in range(1):
            row = data_generation()
            data_raw.append(row)
            print("Raw data - ",data_raw)

        ##set the header record
        HEADER = ["surr_id", "speed", "date", "time"]

        data_df = pd.DataFrame(data_raw, columns=HEADER)
        data_json = bytes(data_df.to_json(orient='records'), encoding='utf-8')
        print("JSON dataset -- ", data_json)