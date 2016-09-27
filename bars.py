import json
import math


def load_data(filepath):
    with open(filepath, encoding='UTF-8') as loadeddata:
        return json.load(loadeddata)


def get_biggest_bar(data):
    maxname = ''
    loadeddata = load_data(data)
    maxelem = loadeddata[0]['Cells']['SeatsCount']
    for element in loadeddata:
        if maxelem < element['Cells']['SeatsCount']:
            maxelem = element['Cells']['SeatsCount']
            maxname = element['Cells']['Name']
    return maxname


def get_smallest_bar(data):
    minname = ''
    loadeddata = load_data(data)
    minelem = loadeddata[0]['Cells']['SeatsCount']
    for element in loadeddata:
        if minelem > element['Cells']['SeatsCount']:
            minelem = element['Cells']['SeatsCount']
            minname = element['Cells']['Name']
    return minname


def get_closest_bar(data, longitude, latitude):
    closestbar = ''
    distance = 0.0
    loadeddata = load_data(data)
    for bar in loadeddata:
        bar_longtitude = bar['Cells']['geoData']['coordinates'][0]
        bar_latitude = bar['Cells']['geoData']['coordinates'][1]
        if distance < math.sqrt((bar_longtitude - longitude) ** 2 + (bar_latitude - latitude) ** 2):
            distance = math.sqrt((bar_longtitude - longitude) ** 2 + (bar_latitude - latitude) ** 2)
            closestbar = bar['Cells']['Name']
    return closestbar


if __name__ == '__main__':
    while 1:
        try:
            path_to_file = input('Введите путь до скаченого файла Бары.json: ')
            print('Самый вместительный бар: ' + get_biggest_bar(path_to_file))
            print('Самый маленький бар: ' + get_smallest_bar(path_to_file))
            break
        except IOError:
            print('Введите корректный путь до файла.')
    while 1:
        try:
            longitude = float(input('Введите долготу:\n'))
            latitude = float(input('Введите широту:\n'))
            print(get_closest_bar(path_to_file, longitude, latitude))
            break
        except ValueError:
            print('Введите координату в корректном формате. Пример: х.ххххххххххххххх')
