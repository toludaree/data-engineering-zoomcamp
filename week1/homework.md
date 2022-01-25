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
```ssh
var.project
  Your GCP Project ID

  Enter a value: composed-facet-339115


Terraform used the selected providers to generate the following execution
plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.dataset will be created
  + resource "google_bigquery_dataset" "dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "trips_data_all"
      + delete_contents_on_destroy = false
      + etag                       = (known after apply)
      + id                         = (known after apply)
      + last_modified_time         = (known after apply)
      + location                   = "europe-west6"
      + project                    = "composed-facet-339115"
      + self_link                  = (known after apply)

      + access {
          + domain         = (known after apply)
          + group_by_email = (known after apply)
          + role           = (known after apply)
          + special_group  = (known after apply)
          + user_by_email  = (known after apply)

          + view {
              + dataset_id = (known after apply)
              + project_id = (known after apply)
              + table_id   = (known after apply)
            }
        }
    }

  # google_storage_bucket.data-lake-bucket will be created
  + resource "google_storage_bucket" "data-lake-bucket" {
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "EUROPE-WEST6"
      + name                        = "dtc_data_lake_composed-facet-339115"
      + project                     = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + uniform_bucket_level_access = true
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "Delete"
            }

          + condition {
              + age                   = 30
              + matches_storage_class = []
              + with_state            = (known after apply)
            }
        }

      + versioning {
          + enabled = true
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

google_bigquery_dataset.dataset: Creating...
google_storage_bucket.data-lake-bucket: Creating...
google_bigquery_dataset.dataset: Creation complete after 2s [id=projects/composed-facet-339115/datasets/trips_data_all]
google_storage_bucket.data-lake-bucket: Creation complete after 2s [id=dtc_data_lake_composed-facet-339115]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```

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