import os

files = [
    "logo.png",
    "logo.jpg",
    "video.mp4",
    "audio.mp3",
    "foo.md",
    "foo.html",
    "dir/logo.png",
    "dir/logo.jpg",
    "dir/video.mp4",
    "dir/audio.mp3",
    "dir/foo.md",
    "dir/foo.html",
    "./logo",
    "./logo.png",
    "./logo.jpg",
    "./video.mp4",
    "./audio.mp3",
    "./foo.md",
    "./foo.html",
    "../logo",
    "../logo.png",
    "../logo.jpg",
    "../video.mp4",
    "../audio.mp3",
    "../foo.md",
    "../foo.html",
    "http://example.com/dir/logo",
    "http://example.com/dir/logo.png",
    "http://example.com/dir/logo.jpg",
    "http://example.com/dir/video.mp4",
    "http://example.com/dir/audio.mp3",
    "http://example.com/dir/foo.md",
    "http://example.com/dir/foo.html",
    "http://example.com/dir/logo?par=foor&nam=bar",
    "http://example.com/dir/logo.png?par=foor&nam=bar",
    "http://example.com/dir/logo.jpg?par=foor&nam=bar",
    "http://example.com/dir/video.mp4?par=foor&nam=bar",
    "http://example.com/dir/audio.mp3?par=foor&nam=bar",
    "http://example.com/dir/foo.md?par=foor&nam=bar",
    "http://example.com/dir/foo.html?par=foor&nam=bar",
    "http://example.com/dir%2Flogo",
    "http://example.com/dir%2Flogo.png",
    "http://example.com/dir%2Flogo.jpg",
    "http://example.com/dir%2Fvideo.mp4",
    "http://example.com/dir%2Faudio.mp3",
    "http://example.com/dir%2Ffoo.md",
    "http://example.com/dir%2Ffoo.html",
    "http://example.com/dir/logo%",
    "http://example.com/dir/logo.png%",
    "http://example.com/dir/logo.jpg%",
    "http://example.com/dir/video.mp4%",
    "http://example.com/dir/audio.mp3%",
    "http://example.com/dir/foo.md%",
    "http://example.com/dir/foo.html%",
    "/uploads/9f7f9e81d1e0c15ae1856781667166d4/logo.png",
    "/uploads/9f7f9e81d1e0c15ae1856781667166d4/logo.jpg",
    "/uploads/9f7f9e81d1e0c15ae1856781667166d4/video.mp4",
    "/uploads/9f7f9e81d1e0c15ae1856781667166d4/audio.mp3",
    "/uploads/9f7f9e81d1e0c15ae1856781667166d4/foo.md",
    "/uploads/9f7f9e81d1e0c15ae1856781667166d4/foo.html",
    "#toto",
    "1",
    "0",
    "-1",
    "",
    "#",
    "?",
    "%"
]

markdown_template = """# Links
- {url}
- [link]({url})
- [link that also has title text]({url} "This link takes you to somewhere!")
- [reference-style link, see below][{url} reference text]
- [link text itself][], see below.

[arbitrary case-insensitive reference text]: {url}  
[1]: {url}
[link text itself]: {url}

# Image

![image]({url})  
![image with title text]({url} "Title Text")  

![image reference style][logo]  
[logo]: {url} "Title Text"

# Video/audio

![Video]({url})  
![Video with title text]({url})  
![Video with title text with absolute size]({url} "Title Text"){{width=100 height=100px}}  
![Video with title text with relative size]({url} "Title Text"){{width=75%}}

"""

for index, u in enumerate(files, start=100):
    output_filename = f"markdown-samples/{index}.md"
    content = markdown_template.format(url=u)
    
    with open(output_filename, 'w', encoding="utf8") as output_file:
        output_file.write(content)
    
    print(f"{index},\"URL = '{u}'\"")

print("All files have been created.")