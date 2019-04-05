import json

old_file = <old_filename>
new_file = <new_filename>

package_list = []

with open("%s.txt" % old_file, 'r') as fp:
    for mystr in fp.readlines():
        package, version = mystr.strip().split(" ")
        package_list.append({'Name': package, 'Old_version': version})

with open("%s.txt" % new_file, 'r') as fp:
    for mystr in fp.readlines():
        package, version = mystr.strip().split(" ")
        package_not_found = True
        for i, kv in enumerate(package_list):
            if package_list[i]['Name'] == package:
                package_not_found = False
                package_list[i]['New_version'] = version
                if package_list[i]['New_version'] == package_list[i]['Old_version']:
                    package_list[i]['Status'] = "UNCHANGED"
                elif package_list[i]['New_version'] != package_list[i]['Old_version']:
                    package_list[i]['Status'] = "UPDATED"
        if package_not_found:
            package_list.append({'Name': package, 'New_version': version})
            package_list[len(package_list)-1]['Old_version'] = None
            package_list[len(package_list)-1]['Status'] = "NEW"

for i, kv in enumerate(package_list):
    if 'New_version' not in package_list[i]:
        package_list[i]['New_version'] = None
        package_list[i]['Status'] = "REMOVED"

package_list = sorted(package_list, key=lambda k: k['Name'])

print(json.dumps(package_list, indent=4))
