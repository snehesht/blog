import os
import re
import json
from config import *
from gitmanager import *
import time
import arrow

# Global Config
DATA_DIR = GIT_REPO_DIR_NAME
POSTS_DATA_DIR = DATA_DIR + "/public"
PROJECTS_DATA_DIR = DATA_DIR + "/projects"
FILE_DOT_MD_REGEX = ACCEPTED_FILE_FORMATS
"""
        Class to access data
"""
class DataStore(object):
    """docstring for DataStore"""
    def __init__(self):
        super(DataStore, self).__init__()
        self.data = {}
        self.metadata = {}
        check_repo_exist()
        self.load_files()
        self.load_metadata()
    """
    Load files from data_dir with markdown format and return a map with key as filename and value as contents
    """
    def load_files(self):
        print("loading files ...")
        data = {}
        files_in_dir = os.listdir(POSTS_DATA_DIR)
        for f in files_in_dir:
            # safegaurd to load only *.md files
            if re.match(FILE_DOT_MD_REGEX,f) is not None:
                # Read each file and save it's content in a dict with key as filename and value as content
                with open(POSTS_DATA_DIR+"/"+f) as fp:
                    key = f.replace(".md","")
                    value = fp.read()
                    data[key] = value
        self.data = data

    # Meta data for the posts
    # Rule, the filename must match the key in metadata
    def load_metadata(self):
        with open(DATA_DIR+"/"+"metadata.json","r") as fp:
            parsed_data = json.load(fp)
        parsed_metadata = [];
        for el in parsed_data:
            el['human_time'] = arrow.get(el['date']).humanize()
            el['year'] = arrow.get(el['date']).year
            parsed_metadata.append(el)
        self.metadata = parsed_metadata


   #Function to access data, this is usually called
    def get_data(self):
        return self.data


    #Function to fetch metadata
    def get_metadata(self):
        return self.metadata


    #Reload data from DATA_DIR, usually called when changes are made
    def reload_data(self):
        self.load_files()
        self.load_metadata()

    #Reload data
    def reload(self):
        try:
            git_update()
        except Exception as e:
            print("Reload failed")
        finally:
            self.reload_data()
