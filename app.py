import os
import urllib.request
from collections import defaultdict

from flask import Flask
from flask import render_template
from flask import jsonify
from github import Github
from github.GithubException import BadCredentialsException, UnknownObjectException

from extractors.dot_notation import get_data


GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
app = Flask(__name__)


def get_data_from_files(files, properties_to_read):
    result = defaultdict(dict)
    while files:
        file = files.pop(0)
        if file.name.endswith(".json"):
            raw_url = file.download_url
            data = urllib.request.urlopen(raw_url).read().decode("utf-8")
            result[file.name] = get_data(data, properties_to_read)
    return result


def collect_data(properties_to_read):
    if not properties_to_read:
        print("Please provide the necessary files or properties to extract the information.")
        return
    files = []
    try:
        files = Github(GITHUB_ACCESS_TOKEN).get_repo("mitre/cti").get_contents("enterprise-attack/attack-pattern")
    except (BadCredentialsException, UnknownObjectException):
        print("Something went wrong with the connection to the github repository")

    return get_data_from_files(files, properties_to_read)


@app.route("/")
def index():
    properties_to_read = ["id", "objects[0].name", "objects[0].kill_chain_phases"]
    collected_data = collect_data(properties_to_read)
    return render_template("index.html", data=collected_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
