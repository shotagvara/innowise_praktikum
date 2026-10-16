import logging
import os
import sys
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window


os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
os.environ["SPARK_LOCAL_IP"] = os.getenv("SPARK_LOCAL_IP", "127.0.0.1")
os.environ["SPARK_LOCAL_HOSTNAME"] = "localhost"

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

jdbc_jar = Path(__file__).parent / "postgresql-42.7.14.jar"

spark = (
    SparkSession.builder
    .appName("PagilaSparkTasks")
    .master("local[2]")
    .config("spark.driver.host", "127.0.0.1")
    .config("spark.driver.bindAddress", "127.0.0.1")
    .config("spark.driver.extraClassPath", str(jdbc_jar.resolve()))
    .config("spark.executor.extraClassPath", str(jdbc_jar.resolve()))
    .getOrCreate()
)
spark.sparkContext.setLogLevel("ERROR")


def load_table(table, columns):
    query = f"(SELECT {', '.join(columns)} FROM public.{table}) AS source"

    return (
        spark.read.format("jdbc")
        .option("url", "jdbc:postgresql://127.0.0.1:55432/pagila")
        .option("dbtable", query)
        .option("user", "postgres")
        .option("password", os.environ["PAGILA_DB_PASSWORD"])
        .option("driver", "org.postgresql.Driver")
        .load()
    )


film = load_table("film", ["film_id", "title"])
film_category = load_table("film_category", ["film_id", "category_id"])
category = load_table("category", ["category_id", "name"])
actor = load_table("actor", ["actor_id", "first_name", "last_name"])
film_actor = load_table("film_actor", ["actor_id", "film_id"])
inventory = load_table("inventory", ["inventory_id", "film_id"])
rental = load_table(
    "rental",
    ["rental_id", "customer_id", "inventory_id", "rental_date", "return_date"],
)
payment = load_table("payment", ["rental_id", "amount"])
customer = load_table("customer", ["customer_id", "address_id", "active"])
address = load_table("address", ["address_id", "city_id"])
city = load_table("city", ["city_id", "city"])


# 1. Output the number of movies in each category, sorted in descending order.
task1_result = (
    film_category
    .join(category, on="category_id")
    .groupBy("name")
    .count()
    .orderBy(F.desc("count"))
)
task1_result.show(truncate=False)

"""
+-----------+-----+
|       name|count|
+-----------+-----+
|      Drama|  152|
|      Music|  152|
|     Travel|  151|
|    Foreign|  150|
|      Games|  150|
|   Children|  150|
|     Action|  149|
|     Sci-Fi|  149|
|  Animation|  148|
|     Family|  147|
|   Classics|  147|
|        New|  147|
|     Sports|  145|
|Documentary|  145|
|     Comedy|  143|
|     Horror|  142|
+-----------+-----+
"""


# 2. Output the 10 actors whose movies rented the most, sorted in descending order.
task2_result = (
    actor
    .join(film_actor, on="actor_id")
    .join(inventory, on="film_id")
    .join(rental, on="inventory_id")
    .groupBy("actor_id", "first_name", "last_name")
    .count()
    .withColumnRenamed("count", "total_rentals")
    .orderBy(F.desc("total_rentals"))
    .limit(10)
)
task2_result.show(truncate=False)

"""
+--------+----------+-----------+-------------+
|actor_id|first_name|last_name  |total_rentals|
+--------+----------+-----------+-------------+
|107     |GINA      |DEGENERES  |2426         |
|181     |MATTHEW   |CARREY     |2247         |
|198     |MARY      |KEITEL     |2173         |
|144     |ANGELA    |WITHERSPOON|2146         |
|102     |WALTER    |TORN       |2074         |
|37      |VAL       |BOLGER     |2012         |
|150     |JAYNE     |NOLTE      |2010         |
|60      |HENRY     |BERRY      |1978         |
|23      |SANDRA    |KILMER     |1958         |
|90      |SEAN      |GUINESS    |1903         |
+--------+----------+-----------+-------------+
"""


# 3. Output the film category on which the most money has been spent.
task3_result = (
    payment
    .join(rental, on="rental_id")
    .join(inventory, on="inventory_id")
    .join(film_category, on="film_id")
    .join(category, on="category_id")
    .groupBy("name")
    .agg(F.sum("amount").alias("money_spent"))
    .orderBy(F.desc("money_spent"))
    .limit(1)
)
task3_result.show(truncate=False)

"""
+------+-----------+
|name  |money_spent|
+------+-----------+
|Action|26505.44   |
+------+-----------+
"""


# 4. Output the names of movies that are not in the inventory.
task4_result = (
    film
    .join(inventory, on="film_id", how="left_anti")
    .select("title")
)
task4_result.show(truncate=False)

"""
+---------------------+
|title                |
+---------------------+
|CHOCOLATE DUCK       |
|BUTCH PANTHER        |
|VOLUME HOUSE         |
|ORDER BETRAYED       |
|TADPOLE PARK         |
|KILL BROTHERHOOD     |
|FRANKENSTEIN STRANGER|
|CROSSING DIVORCE     |
|SUICIDES SILENCE     |
|CATCH AMISTAD        |
|PERDITION FARGO      |
|FLOATS GARDEN        |
|GUMP DATE            |
|WALLS ARTIST         |
|GLADIATOR WESTWARD   |
|HOCUS FRIDA          |
|ARSENIC INDEPENDENCE |
|MUPPET MILE          |
|FIREHOUSE VIETNAM    |
|ROOF CHAMPION        |
+---------------------+
only showing top 20 rows
"""


# 5. Output the top 3 actors in the "Children" category, including ties.
task5_result = (
    actor
    .join(film_actor, on="actor_id")
    .join(film_category, on="film_id")
    .join(category, on="category_id")
    .filter(F.col("name") == "Children")
    .groupBy("actor_id", "first_name", "last_name")
    .agg(F.countDistinct("film_id").alias("children_movies"))
)

window = Window.orderBy(F.desc("children_movies"))
task5_result = task5_result.withColumn("rank", F.rank().over(window))
task5_result = task5_result.filter(F.col("rank") <= 3)
task5_result.show(truncate=False)

"""
+--------+----------+---------+---------------+----+
|actor_id|first_name|last_name|children_movies|rank|
+--------+----------+---------+---------------+----+
|105     |SIDNEY    |CROWE    |9              |1   |
|139     |EWAN      |GOODING  |9              |1   |
|133     |RICHARD   |PENN     |9              |1   |
+--------+----------+---------+---------------+----+
"""


# 6. Output active and inactive customers by city, sorted by inactive descending.
task6_result = (
    customer
    .join(address, on="address_id")
    .join(city, on="city_id")
    .groupBy("city")
    .agg(
        F.sum(F.when(F.col("active") == True, 1).otherwise(0)).alias("active_customers"),
        F.sum(F.when(F.col("active") == False, 1).otherwise(0)).alias("inactive_customers"),
    )
    .orderBy(F.desc("inactive_customers"))
)
task6_result.show(truncate=False)

"""
+--------------------------+----------------+------------------+
|city                      |active_customers|inactive_customers|
+--------------------------+----------------+------------------+
|San Juan Bautista Tuxtepec|383             |18                |
|Uluberia                  |0               |1                 |
|Najafabad                 |0               |1                 |
|Pingxiang                 |0               |1                 |
|Xiangfan                  |0               |1                 |
|Kumbakonam                |0               |1                 |
|Szkesfehrvr               |0               |1                 |
|Charlotte Amalie          |0               |1                 |
|Kamyin                    |0               |1                 |
|Daxian                    |0               |1                 |
|Coatzacoalcos             |0               |1                 |
|Wroclaw                   |0               |1                 |
|Ktahya                    |0               |1                 |
|Bat Yam                   |0               |1                 |
|Southend-on-Sea           |0               |1                 |
|Amroha                    |0               |1                 |
|A Corua (La Corua)        |1               |0                 |
|Fengshan                  |1               |0                 |
|Chisinau                  |1               |0                 |
|Linz                      |1               |0                 |
+--------------------------+----------------+------------------+
only showing top 20 rows
"""


# 7. Output categories by total rental hours in cities starting with "a" and
#    separately in cities containing "-".
task7_data = (
    rental
    .join(customer, on="customer_id")
    .join(address, on="address_id")
    .join(city, on="city_id")
    .join(inventory, on="inventory_id")
    .join(film_category, on="film_id")
    .join(category, on="category_id")
    .filter(F.col("return_date").isNotNull())
    .withColumn(
        "rental_hours",
        (F.col("return_date").cast("long") - F.col("rental_date").cast("long")) / 3600,
    )
)

task7_a = (
    task7_data
    .filter(F.lower(F.col("city")).startswith("a"))
    .groupBy("name")
    .agg(F.round(F.sum("rental_hours"), 2).alias("total_rental_hours"))
    .orderBy(F.desc("total_rental_hours"))
)

task7_minus = (
    task7_data
    .filter(F.col("city").contains("-"))
    .groupBy("name")
    .agg(F.round(F.sum("rental_hours"), 2).alias("total_rental_hours"))
    .orderBy(F.desc("total_rental_hours"))
)

logger.info("Task 7 - Categories in cities starting with A:")
task7_a.show(truncate=False)

"""
+-----------+------------------+
|name       |total_rental_hours|
+-----------+------------------+
|Children   |62434.87          |
|New        |62142.84          |
|Foreign    |59379.05          |
|Sci-Fi     |58965.5           |
|Action     |58626.93          |
|Documentary|58122.48          |
|Travel     |57870.55          |
|Horror     |56445.77          |
|Games      |56124.66          |
|Sports     |55446.33          |
|Classics   |55170.87          |
|Family     |54443.09          |
|Music      |54413.88          |
|Drama      |53669.43          |
|Animation  |52367.99          |
|Comedy     |46957.24          |
+-----------+------------------+
"""


logger.info("Task 7 - Categories in cities containing '-':")
task7_minus.show(truncate=False)

"""
+-----------+------------------+
|name       |total_rental_hours|
+-----------+------------------+
|Sci-Fi     |37002.83          |
|Drama      |35871.95          |
|Documentary|35038.94          |
|New        |34386.06          |
|Foreign    |33844.61          |
|Music      |33497.3           |
|Travel     |33293.65          |
|Games      |32899.15          |
|Children   |32565.1           |
|Horror     |31331.64          |
|Sports     |31301.02          |
|Family     |30664.84          |
|Comedy     |30273.23          |
|Animation  |29991.74          |
|Action     |29943.07          |
|Classics   |29938.85          |
+-----------+------------------+
"""


spark.stop()
