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


## Application Steps:
