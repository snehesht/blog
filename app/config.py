import os

SITE_URL = "https://snehesh.me"

# Accepted file formats regex
# markdown accepted
# reStructuredText not accepted for now
ACCEPTED_FILE_FORMATS = "^.*\.md$" # .md

# Sitemap Blacklist URL's
SITEMAP_BLACKLIST=['/blog/', '/sitemap.xml']

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
DEBUG_STATUS=True

# Welcome Message
WELCOME_MESSAGE="Hello there, I'm Snehesh and I love Python and OSS"

# About Me
# HTML
ABOUT_ME_CONTENT="""
<p>
I'm Snehesh Thalapaneni, a full stack developer living in New York City. While I was doing my undergrad in Electronics, I developed keen interest in computers and I started to teach my self C and then Python. After my bachelors I moved to US and got my master's degree in Computer Engineering. Fast forward, I'm living in New York and working as a generalistic software developer.
</p>

<p>
My interests align with product development, system architecture, IoT, general machine learning, infosec and online privacy. I spend most of my free time turning my ideas into side projects. Apart from the technical aspects of software development, I'm interested in product management, User Interfaces and Robotics.
</p>

<p>
One of most interesting projects I worked on is for my bachelor's thesis, Along with Deepak Muppiri I built a road scanner to map irregularities on indian roads such as speed breakers, path holes, dangerous curves etc. using an array of sensors and then map the data onto Google Maps with ~ 1 meter resolution. Thus the data can be integrated into the navigation software to alert drivers about possible dangers up ahead and this data can also be used by the Govt. to prioritize fixing the roads.
</p>

<p>
Check out my github profile for my side projects, and feel free to use then in anyway you see fit. If you wish to connect, drop an email at <a href="mailto:mail@snehesh.me">mail@snehesh.me</a>
</p>
"""


