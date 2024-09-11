import requests
import argparse
from urllib.parse import urlparse, parse_qs

def run_graphql_query(token, query):
    headers = {"Authorization": "Bearer " + token}
    request = requests.post("https://gitlab.com/api/graphql", json={'query': query}, headers = headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(f"Query failed to run by returning code of {request.status_code}. {query}")
    
def get_issue(token, project_path, issue_iid):
    query = """
    {
    project(fullPath: "%s") {
        issues(iid: "%s") {
        edges {
            cursor
            node {
              description
              descriptionHtml
            }
          }
        }
      }
    }
    """ % (project_path, issue_iid)

    payload = run_graphql_query(token, query)
    return payload["data"]["project"]["issues"]["edges"][0]["node"]

# Parse arguments
parser = argparse.ArgumentParser(description='Retrieve the description of a GitLab issue.')
parser.add_argument('token', type=str, help='GitLab token')
parser.add_argument('issue_url', type=str, help='issue URL')
parser.add_argument('html_file', type=str, help='name of the file (to be created) into which to write the HTML description')
parser.add_argument('markdown_file', type=str, help='name of the file (to be created) into which to write the Markdown description')
args = parser.parse_args()

parsed_url = urlparse(args.issue_url)
path_parts = parsed_url.path.split('/')
issue_iid = path_parts[-1]
project_path = '/'.join(path_parts[1:-3])
descriptions = get_issue(args.token, project_path, issue_iid)

try:
    with open(args.markdown_file, 'x') as file:
        file.write(descriptions["description"])
except FileExistsError:
    print(f"Error: {args.markdown_file} already exists. Refusing to overwrite.")
    exit(1)

try:
    with open(args.html_file, 'x') as file:
        file.write(descriptions["descriptionHtml"])
except FileExistsError:
    print(f"Error: {args.html_file} already exists. Refusing to overwrite.")
    exit(1)
