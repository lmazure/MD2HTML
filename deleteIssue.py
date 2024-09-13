import requests
import argparse
from urllib.parse import urlparse

def delete_issue(token, project_path, issue_iid):
    headers = {"Authorization": "Bearer " + token}  
    api_url = f"https://gitlab.com/api/v4/projects/{project_path.replace('/', '%2F')}/issues/{issue_iid}"
    request = requests.delete(api_url, headers=headers)
    if request.status_code == 204:
        return
    else:
        raise Exception(f"Query failed to run by returning code of {request.status_code}. {api_url}")

# Parse arguments
parser = argparse.ArgumentParser(description='Delete a GitLab issue.')
parser.add_argument('token', type=str, help='GitLab token')
parser.add_argument('issue_url', type=str, help='issue URL')
args = parser.parse_args()

parsed_url = urlparse(args.issue_url)
path_parts = parsed_url.path.split('/')
issue_iid = path_parts[-1]
project_path = '/'.join(path_parts[1:-3])
delete_issue(args.token, project_path, issue_iid)
