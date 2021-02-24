import http.client

conn = http.client.HTTPSConnection("zootmc.com")

payload = ""

headers = {'Accept': "application/json"}

conn.request("GET", "/api/ultimate-stats?uuid=6796c785-6804-43b7-a7ba-b096b46553dc", payload, headers)
res = conn.getresponse()
data = res.read()
int_data = data.decode("utf-8")


def space_remover(list):
    """removes spaces left over in list's"""
    while '' in list:
        list.remove('')
    return list


def dictionary_generator(input_list, dictionary={}):
    temp_list = []
    for data in input_list:
        if ":" in data:
            temp_list = data.split(":")
            if temp_list[1].isnumeric():
                dictionary[temp_list[0]] = temp_list[1]
            else:
                dictionary[temp_list[0]] = [temp_list[1]]
        else:
            dictionary[temp_list[0]].append(data)
    return dictionary


# converts data from string to list
list_data = list(int_data.split('","'))
list_data = list_data[1:]
list_data = list_data[:-1]

# Removes "|" from data
list_rfp = []
for data in list_data:
    if "|" in data:
        data = data.replace("|", " ")
    if "," in data:
        data = data.replace(",", "")
    list_rfp.append(data)

print(list_rfp)
kills = list_rfp[1].split(" ")
kills = space_remover(kills)
kills = dictionary_generator(kills[1:])

print(kills)
