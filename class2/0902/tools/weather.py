import requests

urlPathApi="https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization=CWA-7A8E25AF-A8D6-4AD8-A221-9E11DAD10812&format=JSON"
def get_weather():
    print("get weather")
    county = input('輸入要查詢的縣市: ')
    response=requests.get(urlPathApi)
    allData=response.json()
    locations=allData['records']['Station']
    weatherList=[]
    for item in locations:
        itemDic = {}
        if item['GeoInfo']['CountyName']== county:
            itemDic['縣市']=item['GeoInfo']['CountyName']
            itemDic['區域']=item['GeoInfo']['TownName']
            itemDic['時間']=item['ObsTime']['DateTime']
            itemDic['溫度']=item['WeatherElement']['AirTemperature']
            weatherList.append(itemDic)
    # mylist=[10,20,30,40]
    # try:
    #     mylist[5]
    # except IndexError as e:
    #     print(e)
    # except Exception as e:
    #     print(e)
    # except:
    #     print("mylist error")
    # finally:
    #     print("catch error")
    # if response.status_code == 200:
    #     print("success")
    # else:
    #     print("false")
    #     return None
    # return "Data"
    return weatherList
