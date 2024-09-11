# Markdown → HTML conversion

## createIssue.py
Create an issue whose description is defined by a Markdown file
```sh
$ python createIssue.py $GITLAB_TOKEN "blabla" testfile.md lmazure_TestGroup/20240911
https://gitlab.com/lmazure_TestGroup/20240911/-/issues/10
```
## getIssueDescription.py
Retrieve the Markdown and HTML description of an issue (given its URL) and write them in two files
```sh
$ python getIssueDescription.py $GITLAB_TOKEN https://gitlab.com/lmazure_TestGroup/20240911/-/issues/10 desc.html desc.md
$ cat desc.md
My test.
$ cat desc.html
<p data-sourcepos="1:1-1:8" dir="auto">My test.</p>
```
