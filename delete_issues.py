import json
import requests
from config import *

api_url = f"{base_url}/api/v4"

#
# Get Version
# cf. https://docs.gitlab.com/ee/api/version.html#version-api
#
url = f"{api_url}/version"
print(f"GET {url}")
response = requests.get(url, headers={"PRIVATE-TOKEN": access_token})
print(response)
data = json.loads(response.text)
print(f'Using GitLab version {data["version"]}.')

#
# List project jobs
# cf. https://docs.gitlab.com/ee/api/jobs.html#list-project-jobs
#
url = f"{api_url}/projects/{project_id}/issues?labels={label}"
print(f"GET {url}")
response = requests.get(url, headers={"PRIVATE-TOKEN": access_token})
print(response)
data = json.loads(response.text)

input(
    f"WARNING: This will delete all issues tagged {label}. Job logs will remain be available. Press Enter to continue..."
)

#
# Delete issues with label
# cf. https://docs.gitlab.com/ee/api/issues.html#delete-an-issue
#
for entry in data:
    url = f"{api_url}/projects/{project_id}/issues/{entry['iid']}"
    print(f"DELETE {url}")
    response = requests.delete(url, headers={"PRIVATE-TOKEN": access_token})
    print(response)
