# Import required Flask functions
from flask import Flask, render_template, request
# from flask_heroku import Heroku

# Import required python packages
import random

# Configure app and database
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/joe_site'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# heroku = Heroku(app)

# Initiate db for app
from models.shared import db
db.init_app(app)

# Import models for Articles and Appeals
from models.articles import Articles
from models.appeals import Properties

# Set "homepage" to index.html
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index_view():
    return render_template('index.html')

# Assessment data project
@app.route('/data_assessment/', defaults={'assessment_type':None}, methods=['GET'])
@app.route('/data_assessment/<assessment_type>', methods=['GET'])
def assessment_view(assessment_type):
	# Find a result if button is clicked
	if assessment_type == 'overvalued_search':
		# Select a random id from the list of overvalued ids
		overvalued_ids = [
			21303190150000,
			21303190050000,
			21303010100000,
			21311150070000,
			21314170080000,
			21313310180000,
			21311000410000,
			21311000400000,
			21311000600000,
			21311000650000,
			21311000620000,
			21311000550000,
			21311000500000,
			21311000460000,
			21313090370000,
			21313240080000,
			21312150010000,
			21312080190000,
			21312330140000,
			21313280270000,
			21313260210000,
			21312020080000,
			21314090310000,
			21313030070000,
			21313190140000,
			21313150150000,
			21313200100000,
			21313240360000,
			21304180130000,
			21304180140000,
			21304180170000,
			21304180370000,
			21304180360000,
			21314010180000,
			21313290300000,
			21314010140000,
			21304020480000,
			21304020500000,
			21304020520000,
			21304020510000,
			21304020470000,
			21304020420000,
			21304020380000,
			21304020390000,
			21304020410000,
			21304020430000,
			21304120500000,
			21304120530000,
			21304120540000,
			21304120510000,
			21312320070000,
			21314010130000,
			21304170460000,
			21304170470000,
			21304170480000,
			21314270080000,
			21314000340000]
		overvalued_id = random.choice(overvalued_ids)
		# Select all information from the database for the random id
		selected_property = Properties.query.filter(Properties.id == overvalued_id).first()
		# Select all relevant properties
		relevant_query_results = Properties.query.filter(
			(Properties.id != overvalued_id) & 
			(Properties.neighborhood == selected_property.neighborhood) &
			(Properties.air == selected_property.air) &
			(Properties.attic == selected_property.attic) &
			(Properties.basement == selected_property.basement) &
			(Properties.garage == selected_property.garage) &
			(Properties.exterior == selected_property.exterior) &
			(Properties.classification == selected_property.classification) &
			(Properties.fireplaces <= selected_property.fireplaces) &
			(Properties.full_baths <= selected_property.full_baths) &
			(Properties.half_baths <= selected_property.half_baths) &
			(Properties.apartments <= selected_property.apartments)).all()
		# Convert relevant query results to list
		relevant_properties = [x for x in relevant_query_results]
		# Filer by building sqft in memory
		relevant_properties = [x for x in relevant_properties if (x.building_sqft - 50) <= selected_property.building_sqft <= (x.building_sqft + 50)]
		# Filter by land sqft in memory
		relevant_properties = [x for x in relevant_properties if (x.land_sqft - 50) <= selected_property.land_sqft <= (x.land_sqft + 50)]
		# Filter by lower assessed value in memory
		relevant_properties = [x for x in relevant_properties if (x.building_assessed_2016 < selected_property.building_assessed_2016) or (x.land_assessed_2016 < selected_property.land_assessed_2016)]
		# Calculate the average assessed value of relevant properties
		assessed_relevant = (sum([x.building_assessed_2016 for x in relevant_properties]) / len(relevant_properties)) + (sum([x.land_assessed_2016 for x in relevant_properties]) / len(relevant_properties))
		assessed_selected = selected_property.building_assessed_2016 + selected_property.land_assessed_2016
		overvalued = str(assessed_selected - assessed_relevant)
		# Return template with property information
		return render_template('data_assessment.html', selected_property=selected_property, overvalued=overvalued, relevant_properties=relevant_properties[-5:], assessed_selected=assessed_selected)
	return render_template('data_assessment.html', selected_property=None, overvalued=None, relevant_properties=None, assessed_selected=None)

# Bridges data project
@app.route('/data_bridges', methods=['GET'])
def bridge_view():
	return render_template('data_bridges.html')

# Journalism page
@app.route('/writing_journalism', methods=['GET'])
def journalism_view():
	# Select all academic articles from database
	journalism_articles = Articles.query.filter(Articles.article_type == 'journalism').all()
	# Only select the text of the articles
	journalism_texts = [x.article_text for x in journalism_articles]
	# Render the view with journalism_text in li in body
	return render_template('writing_journalism.html', texts=journalism_texts)

# Academic page
@app.route('/writing_academic', methods=['GET'])
def academic_view():
	# Select all academic articles from database
	academic_articles = Articles.query.filter(Articles.article_type == 'academic').all()
	# Only select the text of the articles
	academic_texts = [x.article_text for x in academic_articles]
	# Render the view with article_text in li in body
	return render_template('writing_academic.html', texts=academic_texts)

# Run app
if __name__ == '__main__':
    app.debug = True
    app.run()