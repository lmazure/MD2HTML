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
            subprocess.run(['python', 'createIssue.py', token, description, markdown_file, project_path])

# Parse arguments
parser = argparse.ArgumentParser(description='Delete a GitLab issue.')
parser.add_argument('token', type=str, help='GitLab token')
parser.add_argument('csv_index', type=str, help='CSV file containing the index')
parser.add_argument('project_path', type=str, help='GitLab project path')
args = parser.parse_args()

process_csv(args.token, args.project_path, args.csv_index)
