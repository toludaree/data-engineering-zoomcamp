# Data Warehouse and BigQuery
- OLAP vs OLTP
- What is a Data Warehouse
- BigQuery
    - Cost
    - 

OLTP - Online Transaction Processing
OLAP - Online Analytical Processing

I'm thinking of OLTP interms of backend databases, used to perform normal CRUD operations which help business operations

While for OLAP, it is designed for storing data intended for analytical operations.. discovering insights

[More on OLTP vs OLAP](https://www.stitchdata.com/resources/oltp-vs-olap/#:~:text=OLTP%20and%20OLAP%3A%20The%20two,historical%20data%20from%20OLTP%20systems.)

A data warehouse is an OLAP solution

BigQuery is a data warehouse solution. 

It's [severless](https://en.wikipedia.org/wiki/Serverless_computing)

BigQuery has the ability to create an External Table on GCS and query from there.. This is different from a native table that is actually stored on BigQuery

## Partitioning in BigQuery

## Clustering in BigQuery

# Partitoning and Clustering

# BigQuery Best Practices
Our focus is mainly on cost reduction and improving query performance