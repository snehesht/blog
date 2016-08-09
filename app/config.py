import os

# Accepted file formats regex
# markdown accepted
# reStructuredText not accepted for now
ACCEPTED_FILE_FORMATS = "^.*\.md$" # .md

# Git Repo Config
# Fetched via environmental variables
if os.environ.get('POSTS_GIT_REPO') != None:
	GIT_REPO_URL = os.environ.get('POSTS_GIT_REPO')
else:
	print('Check your environmental vars - POSTS_GIT_REPO is null ')
	GIT_REPO_URL = "https://github.com/snehesht/blogposts.git"

GIT_REPO_DIR_NAME = GIT_REPO_URL.split('/')[-1].replace('.git','')

if os.environ.get('POSTS_GIT_REPO_SECRET') != None:
	GIT_REPO_SECRET = os.environ.get('POSTS_GIT_REPO_SECRET')
else:
	print('Check your environmental vars - POSTS_GIT_REPO_SECRET is null ')
	GIT_REPO_SECRET = "YOUR SECRET"

# Server Config
PORT=5000
HOST='0.0.0.0'
DEBUG_STATUS=False