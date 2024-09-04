from tools import weather
if __name__ == "__main__":
    print("Hi python~")
    data=weather.get_weather()
    if data is not None:
        print(f"資料是: {data}")