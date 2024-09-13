import argparse
import csv
import subprocess

def process_csv(token, project_path, csv_filename):
    with open(csv_filename, 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            index = row['index']
            description = row['description']
            markdown_file = f"markdown-samples/{index}.md"
            result = subprocess.run(['python', 'createIssue.py', token, description, markdown_file, project_path], capture_output=True, text=True)
            if result.stderr:
                print("Error in createIssue.py:", result.stderr)
                exit(1)
            issue_url = result.stdout
            result = subprocess.run(['python', 'getIssueDescription.py', token, issue_url, f"output/gitlab_{index}.html", f"output/gitlab_{index}.md"], capture_output=True, text=True)
            if result.stderr:
                print("Error in getIssueDescription.py:", result.stderr)
                exit(1)
            result = subprocess.run(['python', 'deleteIssue.py', token, issue_url], capture_output=True, text=True)
            if result.stderr:
                print("Error in deleteIssue.py:", result.stderr)
                exit(1)
            result = subprocess.run(['java', '-jar', 'java/target/markdown-to-html-converter-1.0-SNAPSHOT-jar-with-dependencies.jar', markdown_file, f"output/java_{index}.html"], capture_output=True, text=True)
            if result.stderr:
                print("Error in java -jar java/target/markdown-to-html-converter-1.0-SNAPSHOT-jar-with-dependencies.jar:", result.stderr)
                exit(1)
            print(f"Done with {index}.")

# Parse arguments
parser = argparse.ArgumentParser(description='Delete a GitLab issue.')
parser.add_argument('token', type=str, help='GitLab token')
parser.add_argument('csv_index', type=str, help='CSV file containing the index')
parser.add_argument('project_path', type=str, help='GitLab project path')
args = parser.parse_args()

process_csv(args.token, args.project_path, args.csv_index)
