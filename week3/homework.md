# Week 3 Homework

## Question 1: What is the count for fhv vehicles data for year 2019
42084899

## Question 2: How many distinct dispatching_base_num we have in fhv for 2019
792

## Question 3: Best strategy to optimise if query always filter by dropoff_datetime and order by dispatching_base_num
Partition by dropoff_datetime and cluster by dispatching_base_num

## Question 4: What is the count, estimated and actual data processed for query which counts trip between 2019/01/01 and 2019/03/31 for dispatching_base_num B00987, B02060, B02279
Count: 26558, Estimated data processed: 400 MB, Actual data processed: 155 MB

## Question 5: What will be the best partitioning or clustering strategy when filtering on dispatching_base_num and SR_Flag
Cluster by dispatching_base_num and SR_Flag

## Question 6: What improvements can be seen by partitioning and clustering for data size less than 1 GB
- No improvements
- Can be worse due to metadata

## Question 7: In which format does BigQuery save data
Columnar

> [SQL Reference file](https://github.com/Isaac-Tolu/data-engineering-zoomcamp/blob/main/week3/homework.sql)