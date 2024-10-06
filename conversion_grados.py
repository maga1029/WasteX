import pandas


def grados_fun():
    cc = [18.664, 19.417, -95.612, -96.897]
    dist_lat = round(cc[1]-cc[0], 2)
    dist_lon = round(cc[2]-cc[3], 2)

    df = pandas.read_excel("Longitudes_Tabla.xlsx")
    list_aux = df.to_numpy()
    split_list = []

    for _ in list_aux:
        split_row = [str(__).split("\' \'") for __ in _]
        split_list.append(split_row)

    for _ in range(len(split_list)):
        coordinate = list_aux[_][1][:-3]
        parts = coordinate.split('°')
        degrees = int(parts[0])
        minutes_seconds = parts[1].split('\'')
        minutes = int(minutes_seconds[0])
        seconds = float(minutes_seconds[1].split('"')[0])
        split_list[_][1] = round(degrees+(minutes/60)+(seconds/3600), 2)
        coordinate = list_aux[_][2][:-3]
        parts = coordinate.split('°')
        degrees = int(parts[0])
        minutes_seconds = parts[1].split('\'')
        minutes = int(minutes_seconds[0])
        seconds = float(minutes_seconds[1].split('"')[0])
        split_list[_][2] = round(degrees+(minutes/60)+(seconds/3600), 2)
        dist_lat_total = round((cc[1]-split_list[_][1])/dist_lat, 2)
        dist_lon_total = round((cc[2]+split_list[_][2])/dist_lon, 2)
        split_list[_].append(dist_lat_total)
        split_list[_].append(dist_lon_total)
    print(split_list)
    return split_list


if __name__ == "__main__":
    grados_fun()
