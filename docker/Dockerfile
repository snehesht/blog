FROM python:3.5

ENV POSTS_GIT_REPO "https://github.com/snehesht/blogposts"
ENV POSTS_GIT_REPO_SECRET "THIS IS A SECRET"

RUN mkdir -p /www && \
	cd www && \
	git clone https://github.com/snehesht/blog && \
	cd blog && \
	git checkout "v2.0" && \
	pip install -r Requirements.in && \
	cd app && \
	git clone $POSTS_GIT_REPO

ADD https://raw.githubusercontent.com/snehesht/blog/master/docker/start_server.sh /www
CMD ["chmod","+x","/www/start_server.sh"]

EXPOSE 5000

CMD ["sh","/www/start_server.sh"]