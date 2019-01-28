#!/usr/bin/python3

"""Weather app project.
"""

import re
import sys
import html
import argparse
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

ACCU_URL = ("https://www.accuweather.com/uk/ua/dniprodzerzhynsk/322726/"
            "weather-forecast/322726")
RP5_URL = ("http://rp5.ua/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%"
           "D0%9A%D0%B0%D0%BC'%D1%8F%D0%BD%D1%81%D1%8C%D0%BA%D0%BE%D0%B"
           "C%D1%83_(%D0%94%D0%BD%D1%96%D0%BF%D1%80%D0%BE%D0%B4%D0%B7%D"
           "0%B5%D1%80%D0%B6%D0%B8%D0%BD%D1%81%D1%8C%D0%BA%D1%83)")
SINOPTIK_URL = ("https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%"
                "D0%B0-%D0%BA%D0%B0%D0%BC'%D1%8F%D0%BD%D1%81%D1%8C%D0%B"
                "A%D0%B5-303007130")

ACCU_TAGS = ('<span class="large-temp">', '<span class="cond">')
RP5_TAGS = ('<span class="t_0" style="display: block;">', 'F</span>,')
SINOPTIK_TAGS = ('<p class="today-temp">',
                 '<div class="description"> <!--noindex-->')

def get_request_headers():
    """
    """

    return {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;)'}


def get_page_source(url):
    """
    """

    request = Request(url, headers=get_request_headers())
    page_source = urlopen(request).read()
    return page_source.decode('utf-8')


def get_weather_info(page_content):
    """
    """

    city_page = BeautifulSoup(page_content, 'html.parser')
    current_day = city_page.find('div', attrs={'id': 'bd1c'})
    
    weather_info = {}
    if current_day:
        condition = current_day.find('div', class_='wDescription clearfix')
        if condition:
            weather_info['cond'] = condition.text
        temp_info = current_day.find('tr', class_='temperature')
        temp = temp_info.find('td', class_='cur')
        if temp:
            weather_info['temp'] = temp.text
        feel_temp_info = current_day.find('tr', class_='temperatureSens')
        feel_temp = feel_temp_info.find('td', class_='cur')
        if feel_temp:
            weather_info['feel_temp'] = feel_temp.text
        wind_info = current_day.find_all('td', class_='cur')
        for wi in wind_info:
            wind = wi.find('div', class_='wind')
            if wind:
                #import pdb; pdb.set_trace()
                weather_info['wind'] = wind.text
    return weather_info


def produce_output(info):
    """
    """

    print('Accu Weather: \n')

    for key, value in info.items():
        print(f'{key}: {html.unescape(value)}')
    

def main(argv):
    """ Main entry point.
    """

    KNOWN_COMMANDS = {'accu': 'AccuWeather', 'rp5': 'RP5',
                      'sinoptik': 'sinoptik'}

    parser = argparse.ArgumentParser()
    parser.add_argument('command', help='Choose service name: accu, rp5',
                         nargs=1)
    params = parser.parse_args(argv)

    weather_sites = {"AccuWeather": (ACCU_URL, ACCU_TAGS),
                     "RP5": (RP5_URL, RP5_TAGS),
                     "sinoptik": (SINOPTIK_URL, SINOPTIK_TAGS)}

    if params.command:
        command = params.command[0]
        if command in KNOWN_COMMANDS:
            weather_sites = {
                KNOWN_COMMANDS[command]: weather_sites[KNOWN_COMMANDS[command]]
            }
        else:
            print("Unknown command provided!")
            sys.exit(1)

    for name in weather_sites:
        url, tags = weather_sites[name]
        content = get_page_source(url)
        produce_output(get_weather_info(content))


if __name__ == '__main__':
    main(sys.argv[1:])