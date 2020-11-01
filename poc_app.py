import requests
import re
import os
from github import Github
from github.GithubException import BadCredentialsException, UnknownObjectException

from extractors.extractor import dot_notation_get


GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)


def read_data(files, properties):
    if not files or not properties:
        print("Please provide the necessary files or properties to extract the information.")
    while files:
        file = files.pop(0)
        if file.name.endswith(".json"):
            print("=== Information from file {} ===".format(file.name))
            print(dot_notation_get(file.decoded_content, ["id", "objects[0].name", "objects[0].kill_chain_phases"]))
            print("======")


if __name__ == "__main__":
    files = []
    try:
        files = Github(GITHUB_ACCESS_TOKEN).get_repo("mitre/cti").get_contents("enterprise-attack/attack-pattern")
    except (BadCredentialsException, UnknownObjectException):
        print("Something went wrong with the connection to the github repository")

    properties_to_read = ["id", "objects[0].name", "objects[0].kill_chain_phases"]
    read_data(files, properties_to_read)
