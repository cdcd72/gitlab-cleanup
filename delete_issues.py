#!/bin/python3
# delete_artifacts.py  

import json
import requests
from config import *

#
# Get Version Tested with Version 13.12.4
# cf. https://docs.gitlab.com/ee/api/version.html#version-api
#
print(f'GET /version')
x= (requests.get(f"{base_url}/api/v4/version", headers = {"PRIVATE-TOKEN": access_token }))
print(x)
data=json.loads(x.text)
print(f'Using GitLab version {data["version"]}. Tested with 13.12.4')

#
# List project jobs
# cf. https://docs.gitlab.com/ee/api/jobs.html#list-project-jobs
#
request_str=f'projects/{project_id}/issues?labels={tag}'
url=f'{base_url}/api/v4/{request_str}'
print(f'GET /{request_str}')
x= (requests.get(url, headers = {"PRIVATE-TOKEN": access_token }))
print(x)
data=json.loads(x.text)

input(f'WARNING: This will delete all issues tagged {tag}. Job logs will remain be available. Press Enter to continue...' )

#
# Delete issues
# cf. https://docs.gitlab.com/ee/api/issues.html#delete-an-issue
#
for entry in data:
    request_str=f'projects/{project_id}/issues/{entry["iid"]}'
    url=f'{base_url}/api/v4/{request_str}'
    print(f'DELETE /{request_str}')
    x = requests.delete(url, headers = {"PRIVATE-TOKEN": access_token })
    print(x)

