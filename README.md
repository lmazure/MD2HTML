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

## markdown-to-html-converter-1.0-SNAPSHOT-jar-with-dependencies.jar
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
[INFO]
[INFO] --- resources:3.3.1:resources (default-resources) @ markdown-to-html-converter ---
[INFO] skip non existing resourceDirectory F:\Documents\repos\MD2HTML\java\src\main\resources
[INFO]
[INFO] --- compiler:3.8.1:compile (default-compile) @ markdown-to-html-converter ---
[INFO] Changes detected - recompiling the module!
[INFO] Compiling 1 source file to F:\Documents\repos\MD2HTML\java\target\classes
[INFO] 
[INFO] --- resources:3.3.1:testResources (default-testResources) @ markdown-to-html-converter ---
[INFO] skip non existing resourceDirectory F:\Documents\repos\MD2HTML\java\src\test\resources    
[INFO] 
[INFO] --- compiler:3.8.1:testCompile (default-testCompile) @ markdown-to-html-converter ---     
[INFO] No sources to compile
[INFO] 
[INFO] --- surefire:3.2.2:test (default-test) @ markdown-to-html-converter ---
[INFO] No tests to run.
[INFO] 
[INFO] --- jar:3.3.0:jar (default-jar) @ markdown-to-html-converter ---
[INFO] Building jar: F:\Documents\repos\MD2HTML\java\target\markdown-to-html-converter-1.0-SNAPSHOT.jar
[INFO] 
[INFO] --- assembly:3.3.0:single (make-assembly) @ markdown-to-html-converter ---
[INFO] Building jar: F:\Documents\repos\MD2HTML\java\target\markdown-to-html-converter-1.0-SNAPSHOT-jar-with-dependencies.jar
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  4.941 s
[INFO] Finished at: 2024-09-12T18:57:46+02:00
[INFO] ------------------------------------------------------------------------
$ java -jar target/markdown-to-html-converter-1.0-SNAPSHOT-jar-with-dependencies.jar ../markdown-samples/004.md ../output/004.html
Conversion completed successfully.
```

