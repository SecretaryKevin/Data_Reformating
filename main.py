import http.client

conn = http.client.HTTPSConnection("zootmc.com")

payload = ""

headers = {'Accept': "application/json"}

conn.request("GET", "/api/ultimate-stats?uuid=6796c785-6804-43b7-a7ba-b096b46553dc", payload, headers)
res = conn.getresponse()
data = res.read()

int_data = data.decode("utf-8")

list_data = list(int_data.split('","'))
list_data = list_data[1:]
print(list_data)



