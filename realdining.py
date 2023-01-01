import http.client
import json

#get data from dineoncampus api
conn = http.client.HTTPSConnection("api.dineoncampus.com")
conn.request("GET", "/v1/locations/status?site_id=5acea5d8f3eeb60b08c5a50d&platform=0")

res = conn.getresponse()
data = res.read()

#gets api of everything (status, time records, locations)
results = json.loads(data.decode('utf-8'))

# just need locations, so save the name and menu in a variable
locations = results['locations']

for i in locations:
    if i['name'] == 'Allison Dining Commons':
        allison_name = i['name']
        allison_menu = i['status'].get('message')
    if i['name'] == 'Sargent Dining Commons':
        sargent_name = i['name']
        sargent_menu = i['status'].get('message')
    if i['name'] == 'Elder Dining Commons':
        elder_name = i['name']
        elder_menu = i['status'].get('message')
    if i['name'] == 'Foster Walker Plex West':
        plexw_name = i['name']
        plexw_menu = i['status'].get('message')
    if i['name'] == 'Foster Walker Plex East':
        plexe_name = i['name']
        plexe_menu = i['status'].get('message')

message_str = "%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s" % (allison_name, allison_menu, sargent_name, sargent_menu, elder_name, elder_menu, plexw_name, plexw_menu, plexe_name, plexe_menu)