FROM python:3.5


RUN git clone https://github.com/snehesht/blog && \
	cd blog && \
	pip install -r Requirements.in && \
	cd app && \
	python3 app.py

EXPOSE 5000


