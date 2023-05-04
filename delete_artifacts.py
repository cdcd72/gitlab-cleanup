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
url = f"{api_url}/projects/{project_id}/jobs"
print(f"GET {url}")
response = requests.get(url, headers={"PRIVATE-TOKEN": access_token})
print(response)
data = json.loads(response.text)

input(
    "WARNING: This will delete all artifacts. Job logs will remain be available. Press Enter to continue..."
)

#
# Delete artifacts per job
# cf. https://docs.gitlab.com/ee/api/job_artifacts.html#delete-artifacts
#
for entry in data:
    url = f"{api_url}/projects/{project_id}/jobs/{entry['id']}/artifacts"
    print(f"DELETE {url}")
    response = requests.delete(url, headers={"PRIVATE-TOKEN": access_token})
    print(response)
