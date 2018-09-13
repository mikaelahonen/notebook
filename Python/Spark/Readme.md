# Spark

## Install

Install: `pip install pyspark`

## Run code in console

Run this command in command line: `pyspark`

## Spark concepts

### Spark context
The execution environment of the `spark`.

SparkContext runs in `Driver program` in the master node.

Worker nodes run the actual application.

### RDD
RDD = Resilient Distributed Dataset
* Run and operate on multiple nodes
* Immutable elements: Cannot be changed after created
* Recover automatically in case of failure

To types of operation are available for RDDs

**Transformation**. Operations to apply for RDD to create a new RDD. For example filter and group by.

**Action**. Perform a computation, send results to driver.

More in [tutorialspoints](https://www.tutorialspoint.com/pyspark/pyspark_rdd.htm).
