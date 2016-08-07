Minimalist Blog Engine
======================
[snehesh.me](https://snehesh.me)


_TL;DR_

Publish a blog post with ` git push `
![](http://i.imgur.com/gtfvdkM.gif)


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
		-e POSTS_GIT_REPO_SECRET="5qs04EbWpxQ2WYFpS6apFqhWDubGqC19" \
		-p 5000:5000 \
		--name be1 snehesh/blogengine:latest
```

Stack
-----
> - Python 3
> - Flask
> - Markdown
> - Github Webhook

5qs04EbWpxQ2WYFpS6apFqhWDubGqC19