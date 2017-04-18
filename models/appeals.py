from shared import db

# Create our property info model
class Properties(db.Model):
    __tablename__ = "properties"

    # Primary Key
    id = db.Column("pin14_id", db.BIGINT, primary_key=True)

    # Data
    age = db.Column(db.Integer)
    air = db.Column(db.TEXT)
    apartments = db.Column(db.Integer)
    assessor_office_url = db.Column(db.TEXT)
    attic = db.Column(db.TEXT)
    basement = db.Column(db.TEXT)
    building_assessed_2015 = db.Column(db.Integer)
    building_assessed_2016 = db.Column(db.Integer)
    building_sqft = db.Column(db.Integer)
    city = db.Column(db.TEXT)
    classification = db.Column(db.Integer)
    desc = db.Column(db.TEXT)
    est_market_value_2015 = db.Column(db.Integer)
    est_market_value_2016 = db.Column(db.Integer)
    exterior = db.Column(db.TEXT)
    fireplaces = db.Column(db.Integer)
    full_baths = db.Column(db.Integer)
    half_baths = db.Column(db.Integer)
    garage = db.Column(db.TEXT)
    image_url = db.Column(db.TEXT)
    land_assessed_2015 = db.Column(db.Integer)
    land_assessed_2016 = db.Column(db.Integer)
    land_sqft = db.Column(db.Integer)
    neighborhood = db.Column(db.Integer)
    official_pin14 = db.Column(db.TEXT)
    property_location = db.Column(db.TEXT)
    res_type = db.Column(db.TEXT)
    township = db.Column(db.TEXT)
    use = db.Column(db.TEXT)

    def __init__(self, id, age, air, apartments, assessor_office_url, attic, basement,
    	building_assessed_2015, building_assessed_2016, building_sqft, city, classification,
    	desc, est_market_value_2015, est_market_value_2016, exterior, fireplaces, full_baths, half_baths, garage, image_url,
    	land_assessed_2015, land_assessed_2016, land_sqft, neighborhood, official_pin14, property_location,
    	res_type, township, use):
        self.pin14_id = id
        self.age = age
        self.air = air
        self.apartments = apartments
        self.assessor_office_url = assessor_office_url
        self.attic = attic
        self.basement = basement
        self.building_assessed_2015 = building_assessed_2015
        self.building_assessed_2016 = building_assessed_2016
        self.building_sqft = building_sqft
        self.city = city
        self.classification = classification
        self.desc = desc
        self.est_market_value_2015 = est_market_value_2015
        self.est_market_value_2016 = est_market_value_2016
        self.exterior = exterior
        self.fireplaces = fireplaces
        self.full_baths = full_baths
        self.half_baths = half_baths
        self.garage = garage
        self.image_url = image_url
        self.land_assessed_2015 = land_assessed_2015
        self.land_assessed_2016 = land_assessed_2016
        self.land_sqft = land_sqft
        self.neighborhood = neighborhood
        self.official_pin14 = official_pin14
        self.property_location = property_location
        self.res_type = res_type
        self.township = township
        self.use = use

    def __repr__(self):
        return '<pin14 %r>' % self.id
