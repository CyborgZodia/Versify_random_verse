import json
import requests
import datetime


def get_daily_verse():
    try:
        dv = open("daily_verse.json","r")
        current_date = json.load(dv)
        cdate = datetime.datetime.now()
        cdate = str(cdate.date())

        if current_date["cdate"] != cdate: 
            response_API = requests.get("https://beta.ourmanna.com/api/v1/get/?format=json&order=daily")
            data = response_API.text
            parse_json = json.loads(data)
            json_dct = {}
            text = parse_json['verse']['details']['text']
            reference = parse_json['verse']['details']['reference']
            json_dct["cdate"] = cdate
            json_dct["text"] = text
            json_dct["reference"] = reference
            with open('daily_verse.json', 'w') as daily_verse:
                json.dump(json_dct, daily_verse, ensure_ascii=False)
            with open("daily_verse.json") as json_file:
                file = json.load(json_file)
            return file
        else:
            print("this function did not execute because it is the same day")
    except:
        return '', 200 


print(get_daily_verse())

