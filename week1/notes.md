## Introduction to Docker
- Docker is a product that delivers software in packages called **containers**. Containers are **isolated** from one another
- Data pipeline is a process/service that gets in data and produces more data. It can be a Python script that gets some CSV file and transforms or processes it and it produces an output e.g a Postgres table
- We can use Docker to create a data pipeine and the container will contain all the dependencies needed to run that pipeline.
- Different containers would never conflict with each other even if they contain the same software
- A docker image is like a snapshot of a container. It has all the instructions needed to set up the environment

### Why should we use Docker?
- **Reproducibility** - We can be certain that a docker image that runs successfully locally would also run successfully in any other environment e.g Google Cloud, AWS
- Doing local experiments
- Very useful for doing Integration tests (CI/CD)
- Running pipelineson the cloud
- For using Spark
- For using Severless

### Using Docker
- After installing, test that Docker is running correctly using:
```bash
docker run hello-world
```
- If we create a pipeline for example:
```python
import pandas
```

```Dockerfile
FROM python:3.9

RUN python
```