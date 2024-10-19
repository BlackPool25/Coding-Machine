import requests
import sys


def main():
    user_loc = input("Enter the address: ")
    try:
        weather = requests.get(f"http://api.weatherapi.com/v1/current.json?key=f0a30e9f27e84ad891d61357241910&q={user_loc}&aqi=no")
        weather_json = weather.json()
        print(f"Location: {weather_json["location"]["name"]}")
        print(f"Temperature: {weather_json["current"]["temp_c"]}")
        print(f"Condition: {weather_json["current"]["condition"]["text"]}")
    except KeyError:
        sys.exit("Invalid location.")


if __name__ == "__main__":
    main()