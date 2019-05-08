#!/usr/bin/env python3

import requests ## 3rd party URL lookup

## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    startdate = "start_date={}".format(input("Enter Start Date as yyyy-mm-dd ")) ## start date for data
    enddate = '&end_date=END_DATE' ## create a mechanism to utilize enddate
    mykey = '&api_key=gCe3LGONN1ThoXY2UINjWpgxVhH2a0lXVeh9IzcX' ## Your API key

    neourl = neourl + startdate + mykey

    neojson = (requests.get(neourl)).json()

    print(neojson)


def moon_lengths(missdistance):
    m_length = 238900

    print(missdistance/m_length)

## call main
#main()
moon_lengths(1000000)
