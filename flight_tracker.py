import requests as rq

params = {

    "access_key": "ENTER API KEY HERE"

}

try:

    flight_data = rq.get("http://api.aviationstack.com/v1/flights", params).json()

    json = flight_data["data"]

    for route in json:

        date = route["flight_date"]

        status = route["flight_status"]

        ari = route["arrival"]["airport"]

        dep = route["departure"]["airport"]

        flight = route["airline"]["name"]

        iata = route["flight"]["iata"]

        print(f"Flight: {flight} {iata}")
        
        print(f"Flight Date: {date}")

        print(f"Flight Status: {status}")

        print(f"Flight Arrival: {ari}")

        print(f"Flight Departure: {dep}")

        print("")





except:

    print("Error: Could not fetch data. Please check your internet connetion and try again.")

