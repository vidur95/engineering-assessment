import psycopg2
from load_data import FoodTruck

"""
The purpose of this file is to fetch the data from the DB for food trucks based on the api request
and return the required results. More api requests can be coded based on the types of requests.
These are some sample api requests
"""


class FetchData:
    def __int__(self):
        pass

    """
    Connect to the DB. The values provided here for connection are just sample values that are to replaced with real values
    when used in prod or UAT or dev
    """

    def connectToDb(self):
        conn = psycopg2.connect(host="host", port="5555", database="food_trucks_db", user="user", password="password")
        return conn

    """
    This method will return the list of all locations for a given food truck name (applicant) provided
    by the user
    """

    def getFoodTrucksLocationsByName(self, name=""):
        conn = self.connectToDb()
        cur = conn.cursor()
        sql_query = "SELECT food_truck_location_description FROM food_trucks_repo where food_truck_applicant = %s"
        cur.execute(sql_query, (name,))
        result = []
        for row in cur.fetchall():
            result.append(row)
        if conn:
            conn.close()
        return result

    """
    This method will return the address for a given food truck location description provided
    by the user
    """

    def getFoodTruckAddressByLocationDescription(self, name=""):
        conn = self.connectToDb()
        cur = conn.cursor()
        sql_query = "SELECT food_truck_address FROM food_trucks_repo where food_truck_location_description = %s"
        cur.execute(sql_query, (name,))
        result = []
        for row in cur.fetchall():
            result.append(row)
        if conn:
            conn.close()
        return result

    """
    This method will return the location for a given food truck location id provided
    by the user
    """

    def getFoodTruckLocationDescriptionById(self, locId):
        conn = self.connectToDb()
        cur = conn.cursor()
        sql_query = "SELECT food_truck_location_description FROM food_trucks_repo where food_truck_location_id = %s"
        cur.execute(sql_query, (locId,))
        result = []
        for row in cur.fetchall():
            result.append(row)
        if conn:
            conn.close()
        return result


if __name__ == '__main__':
    foodTruck = FoodTruck()
    foodTruck.processFoodTruckData()
    fetchData = FetchData()
