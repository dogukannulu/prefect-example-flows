import duckdb
import pandas as pd
import requests

from prefect import flow, task
from prefect.filesystems import GitHub

github_block = GitHub.load("prefect-github")


@task
def getInfo():
    r = requests.get("https://api.github.com/events")
    return r.json()


@flow
def testFlow():
    info = getInfo()
    print(info)

if __name__ == "__main__":
    testFlow()