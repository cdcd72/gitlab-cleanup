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

and run the script. Confirm with enter after the warning.
