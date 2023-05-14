/*
* This is the table in a postgre DB used to store all the Food Trucks data read from the
* food trucks url provided
*
*/
DROP TABLE IF EXISTS food_trucks_repo;

CREATE TABLE IF NOT EXISTS food_trucks_repo
(
    id                                          serial primary key NOT NULL,
    food_truck_cnn                              numeric,
    food_truck_block_lot                        numeric,
    food_truck_block                            numeric,
    food_truck_lot                              numeric,
    food_truck_latitude                         numeric,
    food_truck_longitude                        numeric,
    food_truck_schedule                         varchar(200),
    food_truck_permit                           varchar(100),
    food_truck_status                           varchar(100),
    food_truck_facility_type                    varchar(100),
    food_truck_location_description             varchar(300),
    food_truck_items                            varchar(500),
    food_truck_location_id                      integer NOT NULL,
    food_truck_applicant                        varchar(300) NOT NULL,
    food_truck_address                          varchar(500) NOT NULL,
    food_truck_approved                         timestamp,
    food_truck_expiration                       timestamp,
    UNIQUE(food_truck_location_id)
);