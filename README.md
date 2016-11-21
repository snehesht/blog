Minimalist Blog Engine [snehesh.me](https://snehesh.me)
======================
Discuss on [Hacker News](https://news.ycombinator.com/item?id=12244475)

_TL;DR_

Publish a blog post with ` git push `

![](http://i.imgur.com/JKMdO42.gif)

My motivation to build this blog engine was based on 3 factors.
- Write on any device ( i.e Mobile, Laptop) using CLI or text editor
- Never worry about database backups and keep track of all changes I made on an article
- Make publishing simple without touching the server

This project uses git to track all changes made on an article, as all the writing is done in markdown format, I can write posts on multiple devices ( CLI (Termux) on Android, VIM or Sublime on Arch ) switching back and forth. Finally I can publish those writings by adding metadata to the metadata.json file. In other words the posts are visible on blog only when they are enabled in `metadata.json`.


![](https://i.imgur.com/SenXIET.png)



ToDo
----
- Multiprocess support for DataStore()
- Support for .rst format
- Social Buttons ( HN, Twitter )
- Filtered views based on Tags 


Usage
-----
	docker pull snehesh/blogengine:latest
```
	Environmental Variables
		POSTS_GIT_REPO
		POSTS_GIT_REPO_SECRET
```

```
		docker run -d \
		-e POSTS_GIT_REPO="https://github.com/snehesht/BLOGPOSTS_REPO" \
		-e POSTS_GIT_REPO_SECRET="SECRET HERE" \
		-p 5000:5000 \
		--name be1 snehesh/blogengine:latest
```

Stack
-----
> - Python 3
> - Flask
> - Markdown
> - Github Webhook

License
-------

The MIT License (MIT)

Copyright (c) 2016 Snehesh Thalapaneni

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
