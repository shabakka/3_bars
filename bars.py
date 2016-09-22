import json
import math

def load_data(filepath):
    with open(filepath, encoding='UTF-8') as file:
        return json.load(file)
    pass


def get_biggest_bar(data):
    maxname = ''
    lst = load_data(data)
    maxelem = lst[0]['Cells']['SeatsCount']
    for element in lst:
        if maxelem < element['Cells']['SeatsCount']:
            maxelem = element['Cells']['SeatsCount']
            maxname = element['Cells']['Name']
    print('Biggest Bar is "' + maxname + '", which seats ' + str(maxelem) + ' people.\n')
    pass


def get_smallest_bar(data):
    minname = ''
    lst = load_data(data)
    minelem = lst[0]['Cells']['SeatsCount']
    for element in lst:
        if minelem > element['Cells']['SeatsCount']:
            minelem = element['Cells']['SeatsCount']
            minname = element['Cells']['Name']
    print('Smallest bar is "' + minname + '", which seats ' + str(minelem) + ' people.')
    pass


def get_closest_bar(data, longitude, latitude):
    closestbar = ''
    checkpair = []
    result = 0.0
    lst = load_data(data)
    checkpair.append(longitude)
    checkpair.append(latitude)
    for element in lst:
        tempcoordpair = element['Cells']['geoData']['coordinates']
        if result < math.sqrt((tempcoordpair[0] - checkpair[0]) ** 2 + (tempcoordpair[1] - checkpair[1]) ** 2):
            result = math.sqrt((tempcoordpair[0] - checkpair[0]) ** 2 + (tempcoordpair[1] - checkpair[1]) ** 2)
            closestbar = 'Closest bar to your location is "' + element['Cells']['Name'] + '".'
    return closestbar
    pass

def maxmin(data):
    lst = load_data(data)
    maxname = ''
    minname = ''
    minelem = lst[0]['Cells']['SeatsCount']
    maxelem = lst[0]['Cells']['SeatsCount']
    for element in lst:
        if maxelem < element['Cells']['SeatsCount']:
            maxelem = element['Cells']['SeatsCount']
            maxname = element['Cells']['Name']
        elif minelem > element['Cells']['SeatsCount']:
            minelem = element['Cells']['SeatsCount']
            minname = element['Cells']['Name']
    print('Biggest Bar is "' + maxname + '", which seats ' + str(
        maxelem) + ' people.\n' + 'Smallest is "' + minname + '", which seats ' + str(minelem) + ' people.')


if __name__ == '__main__':
    path = 'D:/test/Бары.json'
    #print(maxmin(path))
    print(get_biggest_bar(path))
    print(get_smallest_bar(path))
    while 1:
        try:
            longitude = float(input('Enter 1st coordinate:\n'))
            latitude = float(input('Enter 2nd coordinate:\n'))
            print(get_closest_bar(path, longitude, latitude))
            break
        except ValueError:
            print('Coordinate must contain only numbers in format X.X')

    pass
