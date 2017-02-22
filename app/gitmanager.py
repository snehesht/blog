import subprocess
import os
from config import *

# Update the GIT database repo
def git_update():
    current_dir = os.getcwd().split('/')[-1]
    try:
        if check_repo_exist():
            # Checks if the directory is GIT_REPO_DIR_NAME or not, if not changes to that dir
                # This is to avoid recursive chdir calls
            if current_dir != GIT_REPO_DIR_NAME:
                print("Changing directory")
                os.chdir(GIT_REPO_DIR_NAME)
            proc = subprocess.run(['git','pull'])
            # Sleeps for 10 secs, waits till the pull is completed
            # time.sleep(10)
        else:
            print('Some problem with the repo, repo doesnt exist')
    except Exception as e:
        raise e
    finally:
        os.chdir("../")


def get_current_dir():
    tmp = os.getcwd().split('/')
    return tmp[-1]


# GIT DATA repo doesn't exist, pull the repo
def git_clone():
    try:
        os.chdir(GIT_REPO_DIR_NAME)
        proc = subprocess.run(['git','clone',GIT_REPO_URL])
    except Exception as e:
        raise e
    finally:
        return 0


# Check if git data repo exist
def check_repo_exist():
    try:
        repo_exists = False
        # List dir
        for item in os.listdir():
            # print(item)
            if item == GIT_REPO_DIR_NAME:
                repo_exists = True
        current_dir = os.getcwd().split('/')[-1]
        # If curr directory is GIT_REPO_DIR_NAME
        if current_dir == GIT_REPO_DIR_NAME:
            repo_exists = True
        if repo_exists == False:
            proc = subprocess.run(['git','clone',GIT_REPO_URL])
    except Exception as e:
        raise
    finally:
        return True
