import hashlib
import hmac
import datetime
import misaka
from app import app
from loader import DataStore
from config import SITE_URL , SITEMAP_BLACKLIST

# Generate sitemap.xml
def gen_sitemap(blog_metadata):
    ''' Generate sitemap.xml file '''
    today = datetime.datetime.now().date().isoformat()
    sitemap_urllist = []

    # compile a list of all static urls like /about, /blog, / etc.
    # and append them to the sitemap_urllist.
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static' and "GET" in rule.methods and len(
                rule.arguments) == 0 and rule.rule not in SITEMAP_BLACKLIST:
            tmp_dic = {}
            tmp_dic['url'] = SITE_URL + rule.rule
            # Ignoring the lastmod for constant URL's
            #tmp_dic['lastmod'] = today
            tmp_dic['priority'] = 0.3
            tmp_dic['changefreq'] = "daily"
            sitemap_urllist.append(tmp_dic)

    for bp in blog_metadata:
        tmp_dic = {}
        tmp_dic['url'] = SITE_URL +"/blog/" + bp['url']
        tmp_dic['lastmod'] = bp['date']
        tmp_dic['priority'] = 0.5
        tmp_dic['changefreq'] = "weekly"
        sitemap_urllist.append(tmp_dic)

    return sitemap_urllist


# Convert markdown --> html
def md2html(markdown_content):
    ''' Convert markdown to html using misaka '''
    html_content = misaka.html(
        markdown_content,
        extensions=misaka.EXT_NO_INTRA_EMPHASIS | misaka.EXT_FENCED_CODE |
        misaka.EXT_AUTOLINK | misaka.EXT_TABLES | misaka.EXT_STRIKETHROUGH |
        misaka.EXT_QUOTE | misaka.EXT_UNDERLINE | misaka.EXT_HIGHLIGHT,
        render_flags=misaka.HTML_USE_XHTML | misaka.HTML_HARD_WRAP)
    return html_content


# Verify Github Webhook hash
def hash_check(gh_sha1, gh_payload, secret):
    ''' Verify Github webhook payload and hash '''
    calc_hmac_sha1 = hmac.new(secret.encode(), gh_payload, hashlib.sha1)
    if gh_sha1.split('=')[1] == calc_hmac_sha1.hexdigest():
        return True
    else:
        return False
