# Data Lake (GCS)
## What is a Data Lake?
A data lake is a centralised storage repository for storing big data from many sources in its raw or native format. Data stored in a data lake can be structured, semi-structured, or unstructured. A data lake solution generaly has to be secure, scalable and inexpensive

![datalake-diagram](../images/datalake-diagram.png)

## Data Lake vs. Data Warehouse
|                  |Data Lake                             |Data Warehouse                    |
|------------------|------------------------------------  |----------------------------------|
|**Data Structure**|Generally contains unstructured, raw data|Generally contains structured, processed data|
|**Target Users**  |Data Analysts/Scientists              |Business Analysts                 |
|**Use Cases**     |Stream Processing, Machine Learning, Real-Time Analytics|Batch Processing, BI Reporting|
|**Storage size**  |Huge amount of data, usually petabytes|Relatively Small|          
|**Purpose of Storage**|Not yet defined|Defined and already in use|

## How did it start?
* James Dixon, the then chief technology officer at Pentaho coined the term in 2011. ([source](https://en.wikipedia.org/wiki/Data_lake))
* It started due to companies realising more about the value of data and how the traditional Data Warehouse structure hindered the ability to store and access data quickly as developing schemas and relationships takes time.
* Also, it was discovered that data might not seem useful when the project starts but later in the project lifecycle.
* Once cannot always define the structure of data, hence a Data Warehouse might not be possible.
* Increase in Data Scientists and increase in Research and Development on Data Products also brought about its popularity.
* Another driver of Data Lake solutions was the need for cheap storage of Big Data.

## ETL vs ELT
* **ETL** represents **E**xtract, **T**ransform and **L**oad while **ELT** represents **E**xtract, **L**oad and **T**ransform. These two concepts might seem very similar but it is a good example of what differentiates a Data Lake from a Data Warehouse.
* ETL is a Data Warehouse solution. It's idea is *schema-on-write*: schema and relationships have to be defined before the data is written.
* ELT is a Data Lake soluition. IT's own idea is *schema-on-read*: data is written first, then the schema is determined on the read.

## Gotchas (Challenges) of Data Lake
* Using a Data Lake starts with a good intention, but it can soon turn into a **Data Swamp**
* This is due to lack of organisation, versioning, incompatible schemas for same data.
* It also can occur when there is no metadata associated with the data in the Data Lake
* When _joins_ become impossible, Data Lakes become useless.
* When a Data Lake converts into a Data Swamp, it becomes hard to be useful by Data Scientists and Analysts.

## Cloud Providers For Data Lakes
* **G**oogle **C**loud **P**latform: Cloud Storage
* **A**mazon **W**eb **S**ervices: S3
* AZURE: Azure Blob

## For More Info:
* [Wikipedia](https://en.wikipedia.org/wiki/Data_lake)
* [2011 Aricle on Data Lake](https://www.forbes.com/sites/ciocentral/2011/07/21/big-data-requires-a-big-new-architecture/?sh=39f64fdc1157)
* [Data Lake vs Data Warehouse](https://www.talend.com/resources/data-lake-vs-data-warehouse/)
* [Turning Your Data Lake Into a Data Swamp](https://www.integrate.io/blog/turning-your-data-lake-into-a-data-swamp/)

# Introduction to Workflow Orchestration
We made a kind of pipleline last week, [ingest_data.py](https://github.com/Isaac-Tolu/data-engineering-zoomcamp/blob/main/week1/2_docker_sql/dockerfiles/ingest_data.py). This script downloaded a csv file, did some processing and ingested it to Postgres. It got data as input, and produced data as output

![wrong-pipeline](../images/week1-pipeline.png)

This is a good example of how we should _not_ write data pipelines. The reason is because we're doing two different operations in one script. If something happened during the ingesting process (e.g. connection error to Postgres), running the script again means re-downloading the csv file. Different operations should be splitted into multiple files

![correct-pipeline](../images/good-pipeline.png)

The data pipeline is parameterized. The different jobs have parameters and the pipeline as a whole also has a parameter (URL). The parameter of the pipeline can even be time e.g. running the whole pipeline on 2022-01-31.

![parameterized-pipeline](../images/pipeline2.png)

This week, we're doing a much more interesting and complex architecture:
* Download the CSV file,
* Convert it to a parquet file. A parquet file is much more efficient than a CSV file, as it uses a columnar storage format
* Upload the parquet file to Google Cloud Storage
* Upload to BigQuery from GCS

The final result would be a table in BigQuery

![week2-pipeline](../images/pipeline4.png)

A data pipeline is often called a data workflow. It is also sometimes referred to as **DAG** (**D**irected **A**cyclic **G**raph):
* Directed because it has a direction, 
* Acyclic because it does not work in cycles i.e. as a loop, 
* Graph because the boxes are the nodes and arrows define dependencies.

We use orchestration tools to manage this workflow. A traditional way can be through the use of python scripts and the [MAKE](https://www.gnu.org/software/make/) utility to define dependencies.This is usually used for smaller workflows.

There are standard tools created specifically for managing data workflows. Some of them are:
* [Luigi](https://luigi.readthedocs.io/en/stable/)
* [Apache Airflow](https://airflow.apache.org/)
* [Prefect](https://www.prefect.io/)
* [Argo](https://argoproj.github.io/)

Apache Airflow is the most popular tool used, and that is what we'll be focusing on in this course.