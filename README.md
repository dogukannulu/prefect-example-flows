# Instructions

## Tricks:
- We can use logging for better observability for our flows:
```
from prefect import  get_run_logger

logger = get_run_logger()
logger.info('something to log')
```

- We have two options for deployments:

If we have multiple flows, we can define them in a single Python script. We can use the following commands so that we create multiple deployments for them:

```
first_deployment = first_flow.to_deployment(name="first_deployment", cron = '* * * * *')
second_deployment = second_flow.to_deployment(name="second_deployment", cron = '* * * * *')
serve(first_deployment, second_deployment)
```

Instead of using these, we can use:

```
prefect deployment build <entrypoint>
```


## Steps:

### GitHub Connection:

1. Go to __Blocks__ section and add a new block.
Choose __GitHub__
![Alt text](img/image.png)

2. Populate the parameters as below.
![Alt text](img/image-1.png)
Give a desired name to the block
Repository link will be the link we use for `git clone` command
We can use a classic Access token created within __Settings -> Developer Settings -> Personal Access Tokens__

3. After creating the block, don't forget the below commands in the flow script:

```
from prefect.filesystems import GitHub

github_block = GitHub.load("prefect-github")
```

4. While creating the deployment, we will run the command so that Prefect will get the files from our GitHub repository:
`prefect deployment build flows/example-flow.py:testFlow -n example-flow -sb github/prefect-github/flows --apply`

Doing this will help us define the storage block.
![Alt text](img/image-2.png)


5. After doing all these, we have to start the agent.