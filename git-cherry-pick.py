import requests
import getpass
import sys
import subprocess

repo_name = sys.argv[1]
pull_request_no = sys.argv[2].split(",")

git_use_name = raw_input("Enter your git username?\n")
git_password = getpass.getpass("Enter your git password?\n")
git_commits = []


def extract_commit_hash(pr_no):
    # TODO: remove org name
    r = requests.get('https://api.github.com/repos/xxx/{}/pulls/{}/commits'.format(repo_name, pr_no),
                     auth=(git_use_name, git_password))
    git_response = r.json()
    print "---------------------PR#{}--------------------".format(pr_no)
    for each_commit in git_response:
        # extract commit hash
        print each_commit['sha']
        git_commits.append(each_commit['sha'])

if len(pull_request_no) == 1:
    extract_commit_hash(pull_request_no[0])
else:
    pull_request_no.sort()  # sort PR number by asc
    for each_pull_request_no in pull_request_no:
        extract_commit_hash(each_pull_request_no)

print git_commits
# TODO: include cherry-pick code
subprocess.call(["git", "cherry-pick"] + git_commits)
