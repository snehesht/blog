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

Usage
-----
	docker pull snehesht/blogengine:latest
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
