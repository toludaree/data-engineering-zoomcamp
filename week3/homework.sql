-- Creating FHV external table from GCS path
CREATE OR REPLACE EXTERNAL TABLE `composed-facet-339115.trips_data_all.external_fhv_tripdata`
    OPTIONS(
        format= "parquet",
        uris = [
        "gs://dtc_data_lake_composed-facet-339115/raw/fhv_tripdata/2019/*"
        ]
    );

-- Question 1: What is the count for fhv vehicles data for year 2019
SELECT COUNT(*) as no_of_trips
    FROM composed-facet-339115.trips_data_all.external_fhv_tripdata;

-- Question 2: How many distinct dispatching_base_num we have in fhv for 2019
SELECT COUNT(DISTINCT(dispatching_base_num)) AS no_of_distinct_dbm
    FROM composed-facet-339115.trips_data_all.external_fhv_tripdata;

-- Creating a partitioned-clustered table
CREATE OR REPLACE TABLE composed-facet-339115.trips_data_all.fhv_tripdata_partitoned_clustered
    PARTITION BY DATE(pickup_datetime)
    CLUSTER BY dispatching_base_num AS
        SELECT * FROM composed-facet-339115.trips_data_all.external_fhv_tripdata;

-- Question 4: What is the count, estimated and actual data processed for query which counts trip between 2019/01/01 and 2019/03/31 for dispatching_base_num B00987, B02060, B02279
SELECT COUNT(*) AS count_specific
    FROM composed-facet-339115.trips_data_all.fhv_tripdata_partitoned_clustered
    WHERE DATE(pickup_datetime) BETWEEN '2019-01-01' AND '2019-03-31'
        AND dispatching_base_num='B00987' OR dispatching_base_num='B02060' OR dispatching_base_num='B02279'

-- Correct solution to Question 4. I should have partitioned by dropoff_datetime instead
SELECT COUNT(*) AS count_specific
    FROM composed-facet-339115.trips_data_all.fhv_tripdata_partitoned_clustered
    WHERE DATE(dropoff_datetime) BETWEEN '2019-01-01' AND '2019-03-31'
        AND dispatching_base_num IN ('B00987', 'B02279', 'B02060')