'''
Now that you know the primary differences between a data engineer and a data
scientist, get ready to explore the data engineer's toolbox! Learn in detail
about different types of databases data engineers use, how parallel computing is
a cornerstone of the data engineer's toolkit, and how to schedule data processing
jobs using scheduling frameworks.
'''


'''
The database schema

A PostgreSQL database is set up in your local environment, which contains this
database schema. It's been filled with some example data. You can use pandas to
query the database using the read_sql() function. You'll have to pass it a
database engine, which has been defined for you and is called db_engine.

The pandas package imported as pd will store the query result into a DataFrame
object, so you can use any DataFrame functionality on it after fetching the
results from the database.
'''
# Complete the SELECT statement
data = pd.read_sql("""
SELECT first_name, last_name FROM "Customer"
ORDER BY last_name, first_name
""", db_engine)

# Show the first 3 rows of the DataFrame
print(data.head(3))

# Show the info of the DataFrame
print(data.info())



'''
Joining on relations
'''
# Complete the SELECT statement
data = pd.read_sql("""
SELECT * FROM "Customer"
INNER JOIN "Order"
ON "Order"."customer_id"="Customer"."id"
""", db_engine)

# Show the id column of data
print(data.id)



'''
From task to subtasks

For this exercise, you will be using parallel computing to apply the function
take_mean_age() that calculates the average athlete's age in a given year in the
Olympics events dataset. The DataFrame athlete_events has been loaded for you
and contains amongst others, two columns:

Year: the year the Olympic event took place
Age: the age of the Olympian

You will be using the multiprocessor.Pool API which allows you to distribute
your workload over several processes. The function parallel_apply() is defined
in the sample code. It takes in as input the function being applied, the
grouping used, and the number of cores needed for the analysis. Note that the
@print_timing decorator is used to time each operation.
'''
# Function to apply a function over multiple cores
@print_timing
def parallel_apply(apply_func, groups, nb_cores):
    with Pool(nb_cores) as p:
        results = p.map(apply_func, groups)
    return pd.concat(results)

# Parallel apply using 1 core
parallel_apply(take_mean_age, athlete_events.groupby('Year'), 1)

# Parallel apply using 2 cores
parallel_apply(take_mean_age, athlete_events.groupby('Year'), 2)

# Parallel apply using 4 cores
parallel_apply(take_mean_age, athlete_events.groupby('Year'), 4)



'''
Using a DataFrame

In the previous exercise, you saw how to split up a task and use the low-level
python multiprocessing.Pool API to do calculations on several processing units.

It's essential to understand this on a lower level, but in reality, you'll never
use this kind of APIs. A more convenient way to parallelize an apply over several
groups is using the dask framework and its abstraction of the pandas DataFrame,
for example.

The pandas DataFrame, athlete_events, is available in your workspace.
'''
import dask.dataframe as dd

# Set the number of pratitions
athlete_events_dask = dd.from_pandas(athlete_events, npartitions = 4)

# Calculate the mean Age per Year
print(athlete_events_dask.groupby('Year').Age.mean().compute())



'''
A PySpark groupby

You've seen how to use the dask framework and its DataFrame abstraction to do
some calculations. However, as you've seen in the video, in the big data world
Spark is probably a more popular choice for data processing.

In this exercise, you'll use the PySpark package to handle a Spark DataFrame.
The data is the same as in previous exercises: participants of Olympic events
between 1896 and 2016.

The Spark Dataframe, athlete_events_spark is available in your workspace.

The methods you're going to use in this exercise are:

.printSchema(): helps print the schema of a Spark DataFrame.
.groupBy(): grouping statement for an aggregation.
.mean(): take the mean over each group.
.show(): show the results.
'''
# Print the type of athlete_events_spark
print(type(athlete_events_spark))

# Print the schema of athlete_events_spark
print(athlete_events_spark.printSchema())

# Group by the Year, and find the mean Age
print(athlete_events_spark.groupBy('Year').mean("Age"))

# Group by the Year, and find the mean Age
print(athlete_events_spark.groupBy('Year').mean("Age").show())




'''
Running PySpark files

In this exercise, you're going to run a PySpark file using spark-submit. This
tool can help you submit your application to a spark cluster.

For the sake of this exercise, you're going to work with a local Spark instance
running on 4 threads. The file you need to submit is in
/home/repl/spark-script.py. Feel free to read the file:

cat /home/repl/spark-script.py
You can use spark-submit as follows:

spark-submit \
  --master local[4] \
  /home/repl/spark-script.py
'''

'''
