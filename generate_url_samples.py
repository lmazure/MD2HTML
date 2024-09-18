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

markdown_template = """# Markdown

## Links
- {url}
- [link]({url})
- [link that also has title text]({url} "This link takes you to somewhere!")
- [reference-style link, see below][{url} reference text]
- [link text itself][], see below.

[arbitrary case-insensitive reference text]: {url}  
[1]: {url}
[link text itself]: {url}

## Image

![image]({url})  
![image with title text]({url} "Title Text")  

![image reference style][logo]  
[logo]: {url} "Title Text"

## Video/audio

![Video]({url})  
![Video with title text]({url})  
![Video with title text with absolute size]({url} "Title Text"){{width=100 height=100px}}  
![Video with title text with relative size]({url} "Title Text"){{width=75%}}

# raw HTML

## Image

<img src="{url}" alt="Description of image">

<img src="{url}" alt="Description" width="300" height="200">

<picture>
  <source srcset="{url}" media="(min-width: 800px)">
  <source srcset="{url}" media="(min-width: 400px)">
  <img src="{url}" alt="Description">
</picture>

<div style="background-image: url('{url}');"></div>

<figure>
  <img src="{url}" alt="Description">
  <figcaption>Caption for the image</figcaption>
</figure>

<iframe src="{url}" width="500" height="400" frameborder="0" scrolling="no"></iframe>

## Audio

<audio src="a{url}" controls>
  Your browser does not support the audio element.
</audio>

<audio controls>
  <source src="{url}" type="audio/mpeg">
  <source src="{url}" type="audio/ogg">
  Your browser does not support the audio element.
</audio>

<embed src="{url}" width="300" height="50" type="audio/mpeg">

<object data="{url}" type="audio/mpeg" width="300" height="50">
  <param name="src" value="{url}">
  <param name="autoplay" value="false">
  <param name="autostart" value="false">
</object>

<button onclick="playAudio()">Play Audio</button>
<script>
function playAudio() {{
  var audio = new Audio('{url}');
  audio.play();
}}
</script>

<iframe src="{url}" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>

## Video

<video src="{url}" controls width="640" height="360">
  Your browser does not support the video tag.
</video>

<video controls width="640" height="360">
  <source src="{url}" type="video/mp4">
  <source src="{url}" type="video/webm">
  Your browser does not support the video tag.
</video>

<iframe width="560" height="315" src="{url}" frameborder="0" allowfullscreen></iframe>

<object data="{url}" width="640" height="360">
  <param name="src" value="{url}">
  <param name="autoplay" value="false">
  <param name="autostart" value="false">
</object>

<embed src="{url}" width="640" height="360" type="video/mp4">

<video id="myVideo" width="640" height="360">
  <source src="{url}" type="video/mp4">
</video>
<script>
var video = document.getElementById("myVideo");
function playPause() {{
  if (video.paused) {{
    video.play();
  }} else {{
    video.pause();
  }}
}}
</script>

<video controls poster="{url}">
  <source src="{url}" type="video/mp4">
  <picture>
    <source srcset="{url}" media="(min-width: 800px)">
    <source srcset="{url}" media="(min-width: 400px)">
    <img src="{url}" alt="Video poster">
  </picture>
</video>
"""

for index, u in enumerate(files, start=100):
    output_filename = f"markdown-samples/{index}.md"
    content = markdown_template.format(url=u)
    
    with open(output_filename, 'w', encoding="utf8") as output_file:
        output_file.write(content)
    
    print(f"{index},\"URL = '{u}'\"")

print("All files have been created.")