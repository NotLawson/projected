import json as j
client_information=open("client_information.json", r)
j.load(client_information)
print(client_information)