import requests
import argparse
import json


def run_graphql_query(token, query):
    headers = {"Authorization": "Bearer " + token}
    request = requests.post("https://gitlab.com/api/graphql", json={'query': query}, headers = headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(f"Query failed to run by returning code of {request.status_code}. {query}")
    
def create_issue(token, project_path, issue_title, issue_description):
    query = """
    mutation {
        createIssue(input: {
            projectPath: "%s",
            title: %s,
            description: %s,
            confidential: false
        }) {
            issue {
                id
                iid
                webUrl
            }
            errors
        }
    }
    """ % (project_path, json.dumps(issue_title, ensure_ascii=False), json.dumps(issue_description, ensure_ascii=False))

    payload = run_graphql_query(token, query)
    if "data" not in payload:
        raise Exception(f"Invalid payload answer: {payload}")
    return payload["data"]["createIssue"]["issue"]["webUrl"]

# Parse arguments
parser = argparse.ArgumentParser(description='Create a GitLab issue from a Markdown file.')
parser.add_argument('token', type=str, help='GitLab token')
parser.add_argument('title', type=str, help='issue title')
parser.add_argument('markdown_file', type=str, help=' Markdown file containing the issue description')
parser.add_argument('project_path', type=str, help='GitLab project path')
args = parser.parse_args()

# Read Markdown file
with open(args.markdown_file, 'r', encoding="utf8") as file:
    description = file.read()

# Create the issue
issue_url = create_issue(args.token, args.project_path, args.title, description)
print(issue_url)
