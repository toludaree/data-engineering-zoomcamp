# Week 1 Homework

## Question 1: Google Cloud SDK
```ssh
Google Cloud SDK 369.0.0
alpha 2022.01.14
beta 2022.01.14
bq 2.0.72
core 2022.01.14
gsutil 5.6
```

## Question 2: Terraform


## Question 3: Count records
```sql
SELECT
	COUNT(1)
FROM
	yellow_taxi_trips
WHERE
	CAST(tpep_pickup_datetime AS DATE) = '2021-01-15';
```
Answer: 53024

## Question 4: Largest tip for each day
```sql
SELECT
    CAST(tpep_pickup_datetime AS DATE) AS "day",
    SUM(tip_amount) AS "total_tip_amount"
FROM
    yellow_taxi_trips
WHERE
	CAST(tpep_pickup_datetime AS DATE) >= '2021-01-01' AND
	CAST(tpep_pickup_datetime AS DATE) <= '2021-01-31'
GROUP BY
    CAST(tpep_pickup_datetime AS DATE)
ORDER BY total_tip_amount DESC;
```
Answer: 2021-01-21

## Question 5: Most popular destination
```sql
SELECT
	zdo."Zone",
	COUNT(1) AS "count"
FROM
	yellow_taxi_trips t JOIN zones zpu
		ON t."PULocationID" = zpu."LocationID"
	JOIN zones zdo
		ON t."DOLocationID" = zdo."LocationID"
WHERE
	CAST(t."tpep_pickup_datetime" AS DATE) = '2021-01-14' AND
	zpu."Zone" = 'Central Park'
GROUP BY
	zdo."Zone"
ORDER BY "count" DESC
```
Answer: Upper East Side South

## Question 6: Most expensive locations
```sql
SELECT
	CONCAT(zpu."Zone", '/', zdo."Zone") AS "zone_pair",
	AVG(total_amount) as "average_price"
FROM
	yellow_taxi_trips t JOIN zones zpu
		ON t."PULocationID" = zpu."LocationID"
	JOIN zones zdo
		ON t."DOLocationID" = zdo."LocationID"
GROUP BY
	zone_pair
ORDER BY average_price DESC
```
Answer: Alphabet City/Unknown