# Step 1: Install the Connector

'''
Determine the version of the Snowflake Connector for Python that you plan to install.

To install the dependent libraries, run the pip (or pip3) command and point to the requirements file for that version of the connector.

For example, the latest Snowflake Connector for Python version is 2.4.2 
and you are using Python 3.7 To install the dependent libraries for that version of the connector, run the following command:
'''
pip install -r https://raw.githubusercontent.com/snowflakedb/snowflake-connector-python/v2.4.2/tested_requirements/requirements_37.reqs

## To install the connector, run the following command:
pip install snowflake-connector-python==2.4.2
pip install "snowflake-connector-python[secure-local-storage,pandas]"

# Step 2: Verify the Installation
import snowflake.connector

''' 
Setting Up Browser-based SSO, set the authenticator login parameter/option to external browser
'''
# Step 3: Create  the Connection by 
conn = snowflake.connector.connect(
user = 'username',
password = '',
account = 'company',
warehouse = 'xxx_WAREHOUSE',
database = 'xxx',
schema='xxx',
authenticator='externalbrowser')

# Step 4: Create cursor
curs = conn.cursor()

# Execute SQL statement
# Curs.execute ("SELECT * from Tablename")
# Curs.execute("USE ROLE <CDS_PROD_ROLE>")

curs.execute("USE ROLE CDS_PROD_ROLE")

sql = "select * from Tablename"

curs.execute(sql)

# Fetch the result set from the cursor and deliver it as the pandas DataFrame
df = curs.fetch_pandas_all()

