# GitLab Cleanup

## Utilities

### `delete_artifacts.py`

If you feel, that old artifacts are taking up to much space but you don't want to delete them manually.

Just adapt the header of `delete_artifacts`

```python
# adapt accordingly
base_url='https://gitlab.example.com'
project_id='1234'
access_token='12341234'
```

and run the script. It will first output the GitLab version you are using (Currently tested with 13.11.3). And verify the id and token you just provided.

```
gitlab_cleanup$ ./delete_artifacts.py 
GET /version
<Response [200]>
Using GitLab version 13.11.3. Tested with 13.11.3
GET /projects/6733/jobs
<Response [200]>
WARNING: This will delete all artifacts. Job logs will remain be available. Press Enter to continue...
```
Confirm with enter after the warning.

The program will then output the respectve jobs and return the response code. 

#### Response codes

`<Response [204]>` file deleted successfully
