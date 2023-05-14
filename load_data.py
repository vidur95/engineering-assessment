import psycopg2
import requests

"""
The purpose of this file is to read the data from the url for food trucks and load it into the DB on demand
This file can be executed anytime and it will only insert data for the new food truck location ids
"""

class FoodTruck:
    """
    This is the url provided for fetching all food trucks data
    """
    FOOD_TRUCKS_URL = 'https://data.sfgov.org/Economy-and-Community/Mobile-Food-Facility-Permit/rqzj-sfat/data'

    def __int__(self):
        self.food_trucks_url = FoodTruck.FOOD_TRUCKS_URL

    """
    Read data from the url provided for food trucks
    """
    def getListOfFoodTrucks(self):
        data = None
        response = requests.get(self.food_trucks_url)
        if response is not None:
            data = response.json()
        return data


    """
    Connect to the DB. The values provided here for connection are just sample values that are to replaced with real values
    when used in prod or UAT or dev
    """
    def connectToDb(self):
        conn = psycopg2.connect(host="host", port="5555", database="food_trucks_db", user="user", password="password")
        return conn


    def getFoodTrucksLocationIds(self):
        conn = self.connectToDb()
        cur = conn.cursor()
        cur.execute("SELECT food_truck_location_id FROM food_trucks_repo")
        result = []
        for row in cur.fetchall():
            location_id = row[0]
            result.append(str(location_id))
        conn.close()
        return result


    """
    Load the data in the DB
    """
    def processFoodTruckData(self):
        conn = self.connectToDb()
        cur = conn.cursor()
        food_trucks = self.getListOfFoodTrucks()
        food_truck_location_ids = self.getFoodTrucksLocationIds()

        for food_truck in food_trucks:
            if food_truck['locationid'] in food_truck_location_ids:
                continue

            fooditems = ""
            latitude = ""
            longitude = ""
            applicant = ""
            cnn = ""
            address = ""
            blocklot = ""
            lot = ""
            block = ""
            permit = ""
            status = ""
            facilitytype = ""
            locationdescription = ""
            schedule = ""
            approved = ""
            expirationdate = ""

            if "fooditems" in food_truck:
                fooditems = food_truck['fooditems']
            if "latitude" in food_truck:
                latitude = food_truck['latitude']
            if "longitude" in food_truck:
                longitude = food_truck['longitude']
            if "applicant" in food_truck:
                applicant = food_truck['applicant']
            if "cnn" in food_truck:
                cnn = food_truck['cnn']
            if "address" in food_truck:
                address = food_truck['address']
            if "blocklot" in food_truck:
                blocklot = food_truck['blocklot']
            if "lot" in food_truck:
                lot = food_truck['lot']
            if "block" in food_truck:
                block = food_truck['block']
            if "permit" in food_truck:
                permit = food_truck['permit']
            if "status" in food_truck:
                status = food_truck['status']
            if "facilitytype" in food_truck:
                facilitytype = food_truck['facilitytype']
            if "locationdescription" in food_truck:
                locationdescription = food_truck['locationdescription']
            if "schedule" in food_truck:
                schedule = food_truck['schedule']
            if "approved" in food_truck:
                approved = food_truck['approved']
            if "expirationdate" in food_truck:
                expirationdate = food_truck['expirationdate']

            insert_query = '''
                INSERT INTO food_trucks_repo
                (food_truck_location_id, food_truck_applicant, food_truck_address,
                food_truck_status,food_truck_facility_type,food_truck_location_description,
                food_truck_items,food_truck_latitude, food_truck_longitude, food_truck_approved,
                food_truck_cnn,food_truck_block_lot,food_truck_block, food_truck_lot,
                food_truck_schedule, food_truck_permit, food_truck_facility_type,
                food_truck_expiration)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                '''
            cur.execute(insert_query, (food_truck['locationid'], applicant, address, status,
                                       facilitytype, locationdescription, fooditems, latitude,
                                       longitude, approved, cnn, blocklot, block, lot,
                                       schedule, permit, facilitytype, expirationdate))
        conn.commit()
        if conn:
            conn.close()
