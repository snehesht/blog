from app import app
from flask import  url_for, redirect, request, render_template, Markup
import markdown
from loader import DataStore
from config import *
from helper import hash_check

# Initilize Loading files from git repo
DS = DataStore()

"""
When triggered by Github repo webhook, verifies if the request is valid and if it is, the data stored inside the git repo is pulled down and the DataStore is reloaded
"""
@app.route('/_reload', methods=['POST'])
def reload_data():
	if request.headers.get('X-Hub-Signature', None) != None:
		gh_sha1 = request.headers.get('X-Hub-Signature')
		gh_payload = request.data
		secret = GIT_REPO_SECRET
		if hash_check(gh_sha1, gh_payload, secret) == True:
			DS.reload()
		return redirect(url_for('index'))
	else:
		print('Recieved a post request to reload, but not from github')
		return redirect(url_for('index'))



"""
Index view, a.k.a /root
"""
@app.route('/')
def index():
	return render_template('index.html')



"""
	Redirects to Resume.pdf hosted on Dropbox
"""
@app.route('/resume')
def resume():
	# return render_template('resume.html')
	return redirect('https://www.dropbox.com/s/1fm7p9kr8mjbz8m/resume.pdf?dl=0')



"""
	List of completed and going on projects
"""
@app.route('/projects')
def projects_page():
	return render_template('projects.html')



"""
	About myself
"""
@app.route('/about')
def about_page():
	return render_template('about.html')


"""
	Index of all blogposts
"""
@app.route('/blog/')
@app.route('/blog')
def blog_index_page():
	data = DS.get_metadata()
	return render_template('blog.html', content=data)


@app.route('/blog/<url_slug>/')
@app.route('/blog/<url_slug>')
def blog_post(url_slug):
	data = DS.get_data()
	metadata = DS.get_metadata()
	bp = {}
	try:
		for item in metadata:
			# Search for metadata of the blogpost with that url
			if item['url'] == url_slug:
				bp = item
	except Exception as e:
		# No such blogpost
		return redirect(url_for('index_page'))
	finally:
		raw_content = data[bp['file']]
		processed_content = Markup(markdown.markdown(raw_content))
		return render_template('blog_post.html', content=processed_content,metadata=bp)