import requests

urlPathApi="https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization=CWA-7A8E25AF-A8D6-4AD8-A221-9E11DAD10812&format=JSON"
def get_weather():
    print("get weather")
    response=requests.get(urlPathApi)
    data=response.json()
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
    return data
