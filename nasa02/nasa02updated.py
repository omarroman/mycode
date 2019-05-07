#!/usr/bin/env python3

import requests ## 3rd party URL lookup

## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    startdate = 'start_date=2019-05-07' ## start date for data
    enddate = '&end_date=END_DATE' ## create a mechanism to utilize enddate
    mykey = '&api_key=gCe3LGONN1ThoXY2UINjWpgxVhH2a0lXVeh9IzcX' ## Your API key

    neourl = neourl + startdate + mykey

    neojson = (requests.get(neourl)).json()

    print(neojson)

## call main
main()
