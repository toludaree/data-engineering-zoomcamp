# Introduction to Batch Processing
Batch Processing is data processing done in batches e.g. weekly, daily, hourly e.t.c. as opposed to streaming that's done in realtime. This processing is usually called batch jobs. Batch Jobs can be done with:
- Python scripts
- SQL
- Spark

Worflow Orchestration tools like Airflow are used here too

Advantages
- Easy to manage
- Easy to retry
- Scalability is also easy

Disadvantages
- Delay

# Introduction to Spark
Apache Spark is a distributed multi-language data-processing engine.
It is multi-language in the sense that you can write spark jobs in Scala, Python (PySpark), Java, R but Spark's native language is Scala.
It is distributed as the jobs are run on a cluster that can have thousands of machines
Spark also supports Streaming jobs. A streaming job can be seen as a sequence of small batches and the same techniques can be applied
We use Spark when a simple SQL job cannot cover our usecase
If your batch jobs can be expressed as SQL, then use Hive, Presto, AWS Athems