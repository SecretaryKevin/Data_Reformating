import http.client

conn = http.client.HTTPSConnection("zootmc.com")

payload = ""

headers = {'Accept': "application/json"}

conn.request("GET", "/api/ultimate-stats?uuid=6796c785-6804-43b7-a7ba-b096b46553dc", payload, headers)
res = conn.getresponse()
data = res.read()
int_data = data.decode("utf-8")


def uuid_handler(int_string):
    """isolates the uuid from the rests of the string and tidy's its up"""
    split = int_string.split(":")
    uuid = split[-1].removeprefix('"')
    return uuid


def space_remover(list):
    """removes spaces left over in list's"""
    while '' in list:
        list.remove('')
    return list


def dictionary_generator(input_list):
    """Generates the internal dictionary's"""
    dictionary = {}
    temp_list = []
    for item in input_list:
        if ":" in item:
            temp_list = item.split(":")
            if temp_list[1].isdigit() or "." in temp_list[1]:
                dictionary[temp_list[0]] = float(temp_list[1])
            else:
                dictionary[temp_list[0]] = [str(temp_list[1])]
        else:
            dictionary[temp_list[0]].append(item)
    return dictionary


def int_processing(list):
    """Removes '|' & ',' from data"""
    list_rfp = []
    for data in list:
        if "|" in data:
            data = data.replace("|", " ")
        elif "," in data:
            data = data.replace(",", "")
        list_rfp.append(data)
    return list_rfp


def dictionary_generator_handler(jeremy, final_dictionary={}, x=0):
    """controls feeding data to dictionary_generator and adds the generated dictionary's to the final dictionary"""
    keys = ["uuid", "kills", "death", "damage", "accuracy", "world", "movement", "inventory", "interactions"]
    while x < (len(jeremy) - 1):
        if x == 0:
            uuid = uuid_handler(jeremy[0])
            final_dictionary[keys[0]] = uuid
        else:
            temp_data = space_remover(jeremy[x].split(" "))
            temp_data = dictionary_generator(temp_data[1:])
            final_dictionary[keys[x]] = temp_data
        x = x + 1
    return final_dictionary


# converts data from string to list
list_data = list(int_data.split('","'))
list_data = list_data[1:-1]
list_rfp = int_processing(list_data)
print(dictionary_generator_handler(list_rfp))
