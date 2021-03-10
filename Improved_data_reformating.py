import http.client

conn = http.client.HTTPSConnection("zootmc.com")

payload = ""

headers = {'Accept': "application/json"}

conn.request("GET", "/api/ultimate-stats?uuid=6796c785-6804-43b7-a7ba-b096b46553dc", payload, headers)
res = conn.getresponse()
data = res.read()
int_data = data.decode("utf-8")


def initial_processing(int_string, processed_list=[]):
    temp_list = list(int_string.split('","'))
    temp_list = temp_list[1:-1]
    for string in temp_list:
        string.replace("|", "")
        string.replace(",", "")
        processed_list.append(string)
    return processed_list


def uuid_handler(string_uuid):
    """removes the junk around the uuid and returns the cleaned uuid """
    uuid = string_uuid.split(":")[-1].replace('"', "")
    return uuid


def space_remover(spaced_list):
    """removes the extra spaces in the list passes back"""
    while '' in spaced_list:
        spaced_list.remove("")
    return spaced_list


def dictionary_generator(input_list, dictionary={}):
    """creates the inner dictionary using the supplied data from the handler"""
    for item in input_list:
        if ':' in item:
            temp = item.split(":")
            if temp[1].isdigit() or "." in temp[1]:
                dictionary[temp[0]] = float(temp[1])
            else:
                dictionary[temp[0]] = str(temp[1])
        else:
            dictionary[temp[0]].append(item)
    return dictionary


def dictionary_generator_handler(processed_list, final_dictionary={}, x=0):
    keys = ["uuid", "kills", "death", "damage", "accuracy", "world", "movement", "inventory", "interactions"]
    """keys = key_generator(processed_list)"""
    while x < len(keys):
        if x == 0:
            final_dictionary[keys[0]] = uuid_handler(processed_list[0])
        else:
            final_dictionary[keys[x]] = space_remover(processed_list[x].split(" ")[1:])
        x + 1
    return final_dictionary


test = initial_processing(int_data)

print(dictionary_generator_handler(test))