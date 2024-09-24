import argparse
import csv
import subprocess
import sys

def get_python_executable():
    # If running in a virtual environment, use its Python
    if (sys.prefix != sys.base_prefix):
        return sys.executable
    # Otherwise, use the system Python
    return 'python'

def run_subprocess(command, error_message):
    if command[0] == 'python':
        command[0] = get_python_executable()
    
    result = subprocess.run(command, capture_output=True, text=True)
    if result.stderr:
        print(f"Error in {error_message}:", result.stderr)
        sys.exit(1)
    return result.stdout.strip()

def process_csv(token, project_path, csv_filename, title_prefix):
    with open(csv_filename, 'r', encoding="utf8") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            index = row['index']
            description = title_prefix + " - " + index + " - " + row['description']
            markdown_file = f"markdown-samples/{index}.md"

            # Create issue
            issue_url = run_subprocess(
                ['python', 'createIssue.py', token, description, markdown_file, project_path],
                'createIssue.py'
            )

            # Generate screenshot of GitLab page of the issue
            run_subprocess(
                ['python', 'generateScreenshot.py', issue_url, f"output/{index}_gitlab.png"],
                'generateScreenshot.py'
            )

            # Get issue description
            run_subprocess(
                ['python', 'getIssueDescription.py', token, issue_url, f"output/{index}_gitlab.html", f"output/{index}_gitlab.md"],
                'getIssueDescription.py'
            )

            ### # Delete issue
            ### run_subprocess(
            ###     ['python', 'deleteIssue.py', token, issue_url],
            ###     'deleteIssue.py'
            ### )

            # Convert markdown to HTML using our Java program
            run_subprocess(
                ['java', '-jar', 'java/target/markdown-to-html-converter-1.0-SNAPSHOT-jar-with-dependencies.jar', markdown_file, f"output/{index}_java.html"],
                'java -jar markdown-to-html-converter'
            )

            print(f"Done with {index}.")

# Parse arguments
parser = argparse.ArgumentParser(description='Delete a GitLab issue.')
parser.add_argument('token', type=str, help='GitLab token')
parser.add_argument('csv_index', type=str, help='CSV file containing the index')
parser.add_argument('project_path', type=str, help='GitLab project path')
parser.add_argument('title_prefix', type=str, help='prefix of issue titles')
args = parser.parse_args()

process_csv(args.token, args.project_path, args.csv_index, args.title_prefix)
