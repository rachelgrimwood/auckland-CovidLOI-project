from urllib.request import urlopen, Request
import lxml.html
import cssselect
import mysql.connector
from mysql.connector import Error

pw = ""
db = "LOIs"
host = ""
user = ""

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

connection = create_server_connection(host, user, pw)

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

create_database_query = "CREATE DATABASE LOIs"
create_database(connection, create_database_query)

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

print (create_db_connection(host, user, pw, db))

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

create_table = """CREATE TABLE LOI_table(
  id INT,
  location CHAR(200),
  address CHAR(200),
  date CHAR(200),
  time CHAR(200),
  advice TEXT,
  added CHAR(200),
  updated INT
  )"""

connection = create_db_connection(host, user, pw, db) 
execute_query(connection, create_table) 

link = "https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-health-advice-public/contact-tracing-covid-19/covid-19-contact-tracing-locations-interest"
url = Request(link, headers={'User-Agent': 'Mozilla/5.0'})

def get_tuples():
    response = urlopen(url).read().decode("utf-8")

    startindex = response.find("<tbody>")
    endindex = response.find("</tbody>", startindex)
    locations = response[startindex:endindex]

    markup = lxml.html.fromstring(locations)

    tbl = []
    rows = markup.cssselect("tr")
    for row in rows:
        tbl.append(list())
        for td in row.cssselect("td"):
            tbl[-1].append(td.text_content().strip())

    mainlist = tbl

    LOIs = [] 
    n = 0
    while i < len(mainlist):
        LOIs.append((1, str(mainlist[n][0]), str(mainlist[n][1]), str(mainlist[n][2]), str(mainlist[n][3]), str(mainlist[n][4]), str(mainlist[n][5]), int(mainlist[n][5][0:2])))
        #first index is id, optional to set
        #int(mainlist[n][5][0:2]) gives an initial ordering number if needed (though only works because all the initial locations were added in august!)... the scraper adds time.time() to new items which puts them on top..
        n = n + 1

    return (LOIs)

LOIs = get_tuples()

def pop_item(listitem): 
    query = f"""
    INSERT INTO LOITable VALUES
    {listitem}
    """
    execute_query(connection, query)

for i in LOIs: 
    if "Auckland" in i[2]:
        pop_item(i)
