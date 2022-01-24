# Notes

_This notes are not a guide to anyone, but me. I did not have time to create comprehensive notes this week; hopefully by next week, I would be able to create comprehensive notes._
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

## Ingesting NY Taxi Data to Postgres
- The `-e` option is used to specify environment variables when running a docker image

- I need to learn more about postgres

- [Dataset Used](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

## Connecting pgAdmin and Postgres
- The port mappimg is
```ssh
-p 8080:80
```
- Host machine listens on port 8080 while pgAdmin listens on port 80

## Dockerising the Ingestion Script

## Running Postgres and pgAdmin with Docker-Compose

## SQL Refresher

## Introduction to Google Cloud Platform
- GCP is a host of cloud computing services offered by Google for compute services, storage services and application development
- The services can be divided into different parts:
-