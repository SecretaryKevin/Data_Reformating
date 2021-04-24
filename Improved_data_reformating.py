import http.client
import re

conn = http.client.HTTPSConnection("zootmc.com")

payload = ""

headers = {'Accept': "application/json"}

conn.request("GET", "/api/ultimate-stats?uuid=6796c785-6804-43b7-a7ba-b096b46553dc", payload, headers)
res = conn.getresponse()
data = res.read()
int_data = data.decode("utf-8")


def uuid_handler(int_uuid):
    int_uuid = int_uuid.split(":")
    int_uuid = int_uuid[-1]
    return int_uuid.replace('"', "")


def key_stealer(list, temp_keys=["uuid"]):
    uuid = list[0]
    list.pop(0)
    uuid = uuid_handler(uuid)
    for items in list:
        temp = items.find(":")
        temp_keys.append(items[:temp - 1])
    return temp_keys, uuid


def internal_dictionary_generator(input_string, directory={}, temp_list={}):
    input_list = input_string.split(":")
    print(input_list)
    directory = "test"
    return directory


def external_dictionary_generator(rtp_list, keys, uuid, directory={}, x=0):
    while x < (len(rtp_list)):
        if x == 0:
            directory[keys[0]] = uuid
        else:
            temp_data = rtp_list[x]
            location_num = temp_data.find('":"')
            temp_data = internal_dictionary_generator(temp_data[(location_num + 4):])
            directory[keys[x]] = temp_data
        x = x + 1
    return directory






int_data = int_data.replace("|", " ")
int_data = int_data.replace(",", "")
int_list = int_data.split('""')
int_list = int_list[1:]
global keys
keys, uuid = key_stealer(int_list)
final_dictionary = external_dictionary_generator(int_list, keys, uuid)
print(final_dictionary)

