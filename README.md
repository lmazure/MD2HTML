# GitLab Flavored Markdown → HTML conversion

The purpose of this project is to analyse the best solution to convert a GitLab issue description from GitLab Flavored Markdown into HTML:

- Do we use the HTML provided by GitLab?
- Do we do the GLFM → HTML transformation ourselves? (with the technical constraint that we must use Java)
  If so, by using which library?

## Install the prerequisites
```sh
$ python -m venv .venv

$ source .venv/Scripts/activate
(.venv)
$ pip install -r requirements.txt
$ pip install -r requirements.txt
Collecting selenium (from -r requirements.txt (line 1))
  Using cached selenium-4.24.0-py3-none-any.whl.metadata (7.1 kB)
Collecting urllib3<3,>=1.26 (from urllib3[socks]<3,>=1.26->selenium->-r requirements.txt (line 1))
  Downloading urllib3-2.2.3-py3-none-any.whl.metadata (6.5 kB)
Collecting trio~=0.17 (from selenium->-r requirements.txt (line 1))
  Using cached trio-0.26.2-py3-none-any.whl.metadata (8.6 kB)
Collecting trio-websocket~=0.9 (from selenium->-r requirements.txt (line 1))
  Using cached trio_websocket-0.11.1-py3-none-any.whl.metadata (4.7 kB)
Collecting certifi>=2021.10.8 (from selenium->-r requirements.txt (line 1))
  Downloading certifi-2024.8.30-py3-none-any.whl.metadata (2.2 kB)
Collecting typing_extensions~=4.9 (from selenium->-r requirements.txt (line 1))
  Using cached typing_extensions-4.12.2-py3-none-any.whl.metadata (3.0 kB)
Collecting websocket-client~=1.8 (from selenium->-r requirements.txt (line 1))
  Using cached websocket_client-1.8.0-py3-none-any.whl.metadata (8.0 kB)
Collecting attrs>=23.2.0 (from trio~=0.17->selenium->-r requirements.txt (line 1))
  Using cached attrs-24.2.0-py3-none-any.whl.metadata (11 kB)
Collecting sortedcontainers (from trio~=0.17->selenium->-r requirements.txt (line 1))
  Using cached sortedcontainers-2.4.0-py2.py3-none-any.whl.metadata (10 kB)
Collecting idna (from trio~=0.17->selenium->-r requirements.txt (line 1))
  Downloading idna-3.10-py3-none-any.whl.metadata (10 kB)
Collecting outcome (from trio~=0.17->selenium->-r requirements.txt (line 1))
  Using cached outcome-1.3.0.post0-py2.py3-none-any.whl.metadata (2.6 kB)
Collecting sniffio>=1.3.0 (from trio~=0.17->selenium->-r requirements.txt (line 1))
  Using cached sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
Collecting cffi>=1.14 (from trio~=0.17->selenium->-r requirements.txt (line 1))
  Using cached cffi-1.17.1-cp312-cp312-win_amd64.whl.metadata (1.6 kB)
Collecting wsproto>=0.14 (from trio-websocket~=0.9->selenium->-r requirements.txt (line 1))
  Using cached wsproto-1.2.0-py3-none-any.whl.metadata (5.6 kB)
Collecting pysocks!=1.5.7,<2.0,>=1.5.6 (from urllib3[socks]<3,>=1.26->selenium->-r requirements.txt (line 1))
  Using cached PySocks-1.7.1-py3-none-any.whl.metadata (13 kB)
Collecting pycparser (from cffi>=1.14->trio~=0.17->selenium->-r requirements.txt (line 1))
  Using cached pycparser-2.22-py3-none-any.whl.metadata (943 bytes)
Collecting h11<1,>=0.9.0 (from wsproto>=0.14->trio-websocket~=0.9->selenium->-r requirements.txt (line 1))
  Using cached h11-0.14.0-py3-none-any.whl.metadata (8.2 kB)
Using cached selenium-4.24.0-py3-none-any.whl (9.6 MB)
Downloading certifi-2024.8.30-py3-none-any.whl (167 kB)
Using cached trio-0.26.2-py3-none-any.whl (475 kB)
Using cached trio_websocket-0.11.1-py3-none-any.whl (17 kB)
Using cached typing_extensions-4.12.2-py3-none-any.whl (37 kB)
Downloading urllib3-2.2.3-py3-none-any.whl (126 kB)
Using cached websocket_client-1.8.0-py3-none-any.whl (58 kB)
Using cached attrs-24.2.0-py3-none-any.whl (63 kB)
Using cached cffi-1.17.1-cp312-cp312-win_amd64.whl (181 kB)
Using cached PySocks-1.7.1-py3-none-any.whl (16 kB)
Using cached sniffio-1.3.1-py3-none-any.whl (10 kB)
Using cached wsproto-1.2.0-py3-none-any.whl (24 kB)
Downloading idna-3.10-py3-none-any.whl (70 kB)
Using cached outcome-1.3.0.post0-py2.py3-none-any.whl (10 kB)
Using cached sortedcontainers-2.4.0-py2.py3-none-any.whl (29 kB)
Using cached h11-0.14.0-py3-none-any.whl (58 kB)
Using cached pycparser-2.22-py3-none-any.whl (117 kB)
Installing collected packages: sortedcontainers, websocket-client, urllib3, typing_extensions, sniffio, pysocks, pycparser, idna, h11, certifi, attrs, wsproto, outcome, cffi, trio, trio-websocket, selenium
Successfully installed attrs certifi cffi h11 idna outcome pycparser pysocks selenium sniffio sortedcontainers trio trio-websocket typing_extensions urllib3 websocket-client wsproto
(.venv)
```

Download geckodriver that matches your Firefox version from https://github.com/mozilla/geckodriver/releases.

## Description of the scripts and the programs

### createIssue.py
Create an issue whose description is defined by a Markdown file
```sh
$ python createIssue.py $GITLAB_TOKEN "my title" desc.md lmazure_TestGroup/20240911
https://gitlab.com/lmazure_TestGroup/20240911/-/issues/10
```

### getIssueDescription.py
Retrieve the Markdown and HTML description of an issue (given its URL) and write them in two files
```sh
$ python getIssueDescription.py $GITLAB_TOKEN https://gitlab.com/lmazure_TestGroup/20240911/-/issues/10 desc.html desc.md
$ cat desc.md
My test.
$ cat desc.html
<p data-sourcepos="1:1-1:8" dir="auto">My test.</p>
```

### deleteIssue.py
Delete an issue (given its URL)
```sh
$ python deleteIssue.py $GITLAB_TOKEN https://gitlab.com/lmazure_TestGroup/20240911/-/issues/3

```

### markdown-to-html-converter-1.0-SNAPSHOT-jar-with-dependencies.jar
Convert a Markdown file into a HTML file using Java.
```sh
$ cd java

$ mvn package
[INFO] Scanning for projects...
[INFO] 
[INFO] ---------------< com.example:markdown-to-html-converter >---------------
[INFO] Building markdown-to-html-converter 1.0-SNAPSHOT
[INFO]   from pom.xml
[INFO] --------------------------------[ jar ]---------------------------------
Downloading from central: https://repo.maven.apache.org/maven2/org/commonmark/commonmark/0.22.0/commonmark-0.22.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/commonmark/commonmark/0.22.0/commonmark-0.22.0.pom (2.2 kB at 3.6 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/commonmark/commonmark-parent/0.22.0/commonmark-parent-0.22.0.pom
Downloaded from central: https://repo.maven.apache.org/maven2/org/commonmark/commonmark-parent/0.22.0/commonmark-parent-0.22.0.pom (12 kB at 106 kB/s)
Downloading from central: https://repo.maven.apache.org/maven2/org/commonmark/commonmark/0.22.0/commonmark-0.22.0.jar
Downloaded from central: https://repo.maven.apache.org/maven2/org/commonmark/commonmark/0.22.0/commonmark-0.22.0.jar (194 kB at 1.0 MB/s)
[INFO] 
[INFO] --- resources:3.3.1:resources (default-resources) @ markdown-to-html-converter ---
[INFO] skip non existing resourceDirectory F:\Documents\repos\MD2HTML\java\src\main\resources
[INFO]
[INFO] --- compiler:3.13.0:compile (default-compile) @ markdown-to-html-converter ---
[INFO] Recompiling the module because of changed dependency.
[INFO] Compiling 1 source file with javac [debug target 22] to target\classes
[INFO] 
[INFO] --- resources:3.3.1:testResources (default-testResources) @ markdown-to-html-converter ---
[INFO] skip non existing resourceDirectory F:\Documents\repos\MD2HTML\java\src\test\resources
[INFO]
[INFO] --- compiler:3.13.0:testCompile (default-testCompile) @ markdown-to-html-converter ---
[INFO] No sources to compile
[INFO]
[INFO] --- surefire:3.2.2:test (default-test) @ markdown-to-html-converter ---
[INFO] No tests to run.
[INFO]
[INFO] --- jar:3.3.0:jar (default-jar) @ markdown-to-html-converter ---
[INFO] Building jar: F:\Documents\repos\MD2HTML\java\target\markdown-to-html-converter-1.0-SNAPSHOT.jar
[INFO] 
[INFO] --- assembly:3.7.1:single (make-assembly) @ markdown-to-html-converter ---
[INFO] Building jar: F:\Documents\repos\MD2HTML\java\target\markdown-to-html-converter-1.0-SNAPSHOT-jar-with-dependencies.jar
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  7.095 s
[INFO] Finished at: 2024-09-12T19:07:43+02:00
[INFO] ------------------------------------------------------------------------
$ java -jar target/markdown-to-html-converter-1.0-SNAPSHOT-jar-with-dependencies.jar ../markdown-samples/004.md ../output/004.html
Conversion completed successfully.
```

### markdown-to-html-converter-1.0-SNAPSHOT-jar-with-dependencies.jar
Loop on all Markdown samples and get HTML from GitLab and from Java transformation.
```sh
$ python loop.py $GITLAB_TOKEN markdown-samples/list.csv lmazure_TestGroup/20240911
Done with 001.
Done with 002.
Done with 003.
Done with 004.
Done with 005.
```

## Test cases
- 000→005 are basic smoke tests
- 801→853 are (a quick 'n dirty extract) from https://docs.gitlab.com/ee/user/markdown.html
- 901→910 are from https://gitlab.com/gitlab-org/gitlab/-/blob/master/glfm_specification/input/gitlab_flavored_markdown/glfm_official_specification.md
