import duckdb
import pandas as pd
import requests
from datetime import datetime
from prefect import flow, task
from prefect.filesystems import GitHub

github_block = GitHub.load("prefect-github")


@task
def time():
    return datetime.utcnow().isoformat()


@flow
def testFlow2():
    info = time()
    print(info)

if __name__ == '__main__':
    testFlow2()