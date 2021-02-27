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


def dictionary_generator(input_list):
    dictionary = {}
    temp_list = []
    for data in input_list:
        if ":" in data:
            temp_list = data.split(":")
            if temp_list[1].isdigit() or "." in temp_list[1]:
                dictionary[temp_list[0]] = float(temp_list[1])
            else:
                dictionary[temp_list[0]] = [str(temp_list[1])]
        else:
            dictionary[temp_list[0]].append(data)
    return dictionary


# converts data from string to list
list_data = list(int_data.split('","'))
list_data = list_data[1:]
list_data = list_data[:-1]


def int_processing(list):
    # Removes "|" & ","from data
    list_rfp = []
    for data in list:
        if "|" in data:
            data = data.replace("|", " ")
        if "," in data:
            data = data.replace(",", "")
        list_rfp.append(data)
    return list_rfp


list_rfp = int_processing(list_data)
print(list_rfp)

kills = list_rfp[1].split(" ")
kills = space_remover(kills)
kills = dictionary_generator(kills[1:])

death = list_rfp[2].split(" ")
death = space_remover(death)
death = dictionary_generator(death[1:])

damage = list_rfp[3].split(" ")
damage = space_remover(damage)
damage = dictionary_generator(damage[1:])

Accuracy = list_rfp[4].split(" ")
Accuracy = space_remover(Accuracy)
Accuracy = dictionary_generator(Accuracy[1:])

world = list_rfp[5].split(" ")
world = space_remover(world)
world = dictionary_generator(world[1:])

movement = list_rfp[6].split(" ")
movement = space_remover(movement)
movement = dictionary_generator(movement[1:])

inventory = list_rfp[7].split(" ")
inventory = space_remover(inventory)
inventory = dictionary_generator(inventory[1:])

ineractions = list_rfp[8].split(" ")
ineractions = space_remover(ineractions)
ineractions = dictionary_generator(ineractions[1:])

print(kills)
print(death)
print(damage)
print(Accuracy)
print(world)
print(movement)
print(inventory)
print(ineractions)
