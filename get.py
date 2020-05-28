# This example displays how to get all contacts from a HubID and paginate through them using the 'offset' parameter.
# The end result is a python list containing all parsed contacts.

import requests
import json
import urllib

max_results = 500
hapikey = '0ad67088-5064-4540-9de7-2075f371e28e'
count = 5
contact_list = []
property_list = []
get_all_contacts_url = "https://api.hubapi.com/contacts/v1/lists/all/contacts/all?"
parameter_dict = {'hapikey': hapikey, 'count': count}
headers = {}

# Paginate your request using offset
has_more = True
while has_more:
    parameters = urllib.urlencode(parameter_dict)
    get_url = get_all_contacts_url + parameters
    r = requests.get(url=get_url, headers=headers)
    response_dict = json.loads(r.text)
    has_more = response_dict['has-more']
    contact_list.extend(response_dict['contacts'])
    parameter_dict['vidOffset'] = response_dict['vid-offset']
    # Exit pagination, based on whatever value you've set your max results variable to.
    if len(contact_list) >= max_results:
        print('maximum number of results exceeded')
        break
print('loop finished')

list_length = len(contact_list)

print("You've succesfully parsed through {} contact records and added them to a list".format(list_length))
