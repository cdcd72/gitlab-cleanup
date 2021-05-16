#!/bin/python3
# delete_artifacts.py  

import json
import requests

# adapt accordingly
base_url='https://gitlab.example.com'
project_id='1234'
access_token='12341234'

#
# Get Version Tested with Version 13.11.3
# cf. https://docs.gitlab.com/ee/api/version.html#version-api
#
print(f'GET /version')
x= (requests.get(f"{base_url}/api/v4/version", headers = {"PRIVATE-TOKEN": access_token }))
print(x)
data=json.loads(x.text)
print(f'Using GitLab version {data["version"]}. Tested with 13.11.3')

#
# List project jobs
# cf. https://docs.gitlab.com/ee/api/jobs.html#list-project-jobs
#
request_str=f'projects/{project_id}/jobs'
url=f'{base_url}/api/v4/{request_str}'
print(f'GET /{request_str}')
x= (requests.get(url, headers = {"PRIVATE-TOKEN": access_token }))
print(x)
data=json.loads(x.text)

input('WARNING: This will delete all artifacts. Job logs will remain be available. Press Enter to continue...' )

#
# Delete job artifacts
# cf. https://docs.gitlab.com/ee/api/job_artifacts.html#delete-artifacts
#
for entry in data:
    request_str=f'projects/{project_id}/jobs/{entry["id"]}/artifacts'
    url=f'{base_url}/api/v4/{request_str}'
    print(f'DELETE /{request_str}')
    x = requests.delete(url, headers = {"PRIVATE-TOKEN": access_token })
    print(x)

