from urllib.request import urlopen, Request
import lxml.html
import cssselect
import mysql.connector
from mysql.connector import Error

pw = ""
db = ""
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
        print("Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

connection = create_server_connection(host, user, pw)

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Database connection successful")
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

connection = create_db_connection(host, user, pw, db) 

MOH_link = "https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-health-advice-public/contact-tracing-covid-19/covid-19-contact-tracing-locations-interest"
MOH_url = Request(MOH_link, headers={'User-Agent': 'Mozilla/5.0'})

my_link = "https://auckland-loi.herokuapp.com"
my_url = Request(my_link, headers={'User-Agent': 'Mozilla/5.0'})

def get_list(url, table_start, table_end):
    response = urlopen(url).read().decode("utf-8")

    start_index = response.find(table_start)
    end_index = response.find(table_end, start_index)
    locations = response[start_index:end_index]

    markup = lxml.html.fromstring(locations)

    tbl = []
    rows = markup.cssselect("tr")
    for row in rows:
        tbl.append(list())
        for td in row.cssselect("td"):
            tbl[-1].append(td.text_content().strip())

    for a in tbl:
        for b in a:
            b = str(b)

    LOIs = tbl
    return (LOIs)

MOH_LOIs = get_list(MOH_url, "<tbody>", "</tbody>") #gets the LOI table from MOH website
my_LOIs = get_list(my_url, "</tr>", "</table>") #gets the LOI table from my website

def pop_item(list_item): 
    query = f"""
    INSERT INTO LOITable VALUES
    {list_item}
    """
    execute_query(connection, query)
