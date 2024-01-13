import duckdb
import pandas as pd
import requests

from prefect import flow, task


@task
def getInfo():
    r = requests.get("https://api.github.com/events")
    return r.json()


@flow
def testFlow():
    info = getInfo()
    print(info)