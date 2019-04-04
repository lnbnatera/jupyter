#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json

with open("package2.json", "r") as f_in:
    data = json.load(f_in)


# In[2]:


print(json.dumps(data, indent=4))


# In[3]:


if data['Instance'][0]['Component']['PRN'] > data['Instance'][1]['Component']['PRN']:
    new = 0
    old = 1
else:
    new = 1
    old = 0


# In[4]:


combined_dict = {}

for i1, v1 in enumerate(data['Instance'][new]['Package']):
    if v1:
        #print("%s - %s" % (v1['Name'], v1['Version']))
        combined_dict[v1['Name']] = {'old_version': v1['Version'] }
        data['Instance'][new]['Package'][i1] = {}
    for i2, v2 in enumerate(data['Instance'][old]['Package']):
        if v2 and v1['Name'] == v2['Name']:
            #print("  %s - %s" % (v2['Name'], v2['Version']))
            combined_dict[v2['Name']]['new_version'] = v2['Version']
            data['Instance'][old]['Package'][i2] = {}
    if 'new_version' not in combined_dict[v1['Name']]:
        combined_dict[v1['Name']]['new_version'] = None
        combined_dict[v1['Name']]['status'] = "REMOVED"
    elif combined_dict[v1['Name']]['new_version'] != combined_dict[v1['Name']]['old_version']:
        combined_dict[v1['Name']]['status'] = "UPDATED"
    elif combined_dict[v1['Name']]['new_version'] == combined_dict[v1['Name']]['old_version']:
        combined_dict[v1['Name']]['status'] = "UNCHANGED"
    
for i1, v1 in enumerate(data['Instance'][old]['Package']):
    if v1:
        #print("  %s - %s" % (v1['Name'], v1['Version']))
        combined_dict[v1['Name']] = {'old_version': None}
        combined_dict[v1['Name']]['new_version'] = v1['Version']
        combined_dict[v1['Name']]['status'] = "NEW"

    
print(json.dumps(combined_dict, indent=4))

