'''
Having been exposed to the toolbox of data engineers, it's now time to jump into
the bread and butter of a data engineer's workflow! With ETL, you will learn how
to extract raw data from various sources, transform this raw data into
actionable insights, and load it into relevant databases ready for consumption!
'''

'''
Data sources
In the previous video you've learned about three ways of extracting data:

Extract from text files, like .txt or .csv
Extract from APIs of web services, like the Hackernews API
Extract from a database, like a SQL application database for customer data
We also briefly touched upon row-oriented databases and OLTP.
'''

'''
Fetch from an API
'''
import requests

# Fetch the Hackernews post
resp = requests.get("https://hacker-news.firebaseio.com/v0/item/16222426.json")

# Print the response parsed as JSON
print(resp.json())

# Assign the score of the test to post_score
post_score = resp.json()['score']
print(post_score)




'''
Read from a database
'''
# Function to extract table to a pandas DataFrame
def extract_table_to_pandas(tablename, db_engine):
    query = "SELECT * FROM {}".format(tablename)
    return pd.read_sql(query, db_engine)

# Connect to the database using the connection URI
connection_uri = "postgresql://repl:password@localhost:5432/pagila"
db_engine = sqlalchemy.create_engine(connection_uri)

# Extract the film table into a pandas DataFrame
extract_table_to_pandas('film', db_engine)

# Extract the customer table into a pandas DataFrame
extract_table_to_pandas('customer', db_engine)



'''
