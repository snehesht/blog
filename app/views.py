from app import app
from flask import url_for, redirect, request, render_template, Markup, jsonify, make_response, Response
import misaka
from loader import DataStore
from config import *
from helper import hash_check, md2html, gen_sitemap

# Initilize Loading files from git repo
DS = DataStore()

# Pull the new commits and update the DataStore
@app.route('/_reload', methods=['POST'])
def reload_data():
    """
    When triggered by Github repo webhook, verifies if the request is valid
    and if it is, the data stored inside the git repo is pulled down and the
    DataStore is reloaded
    """
    DS.reload()
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


# ToDo
# [ ] Implement SAMARITAN UI on index page
# Index View
@app.route('/')
def index():
    # return render_template('index.html')
    return redirect(url_for('blog_index_page'))


# Redirects to Resume.pdf hosted on Dropbox
@app.route('/resume')
def resume():
    # return render_template('resume.html')
    return redirect(
        'https://www.dropbox.com/s/hrliztig0dzs84n/Resume.pdf?dl=0')


# ****NOT IMPELMENTED YET ****
# Projects Page
# List of completed and going on projects
@app.route('/projects')
def projects_page():
    # return redirect('https://github.com/snehesht')
    data = DS.get_metadata()
    return render_template('projects.html', content=data)


# About Me Page
@app.route('/about')
def about_page():
    return render_template('about.html', content=ABOUT_ME_CONTENT)


# Todo:
#   [ ]  Pagination
#   [ ]  Kudos


# BlogPosts Page - List of all posts
@app.route('/blog/')
@app.route('/blog')
def blog_index_page():
    data = DS.get_metadata()
    return render_template('blog.html', content=data)


# Individual BlogPost View
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

        raw_content = data[bp['file']]
        processed_content = Markup(md2html(raw_content))
        return render_template(
            'post.html', content=processed_content, metadata=bp)
    except Exception as e:
        # No blogpost found with the matching URL
        # redirects to /blog
        print(e)
        return redirect(url_for('blog_index_page'))


# 404 Error
@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('index'))


# Prints all URL endpoints
@app.route('/sitemap.xml')
def sitemap():
    urlmap = gen_sitemap(DS.get_metadata())
    resp = render_template('sitemap.xml',
        sitemap=urlmap)
    return Response(resp, status=200, mimetype='application/xml')
