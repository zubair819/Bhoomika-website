from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Connect to your MongoDB Atlas cluster
client = MongoClient("mongodb+srv://zubairmohammed091:BpDmNLNi838XkBKN@cluster0.adghs1o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["bhoomika"]
main_collection = db["registrations"]
dance_collection = db["reg_for_dance"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registration.html')
def registration():
    return render_template('registration.html')

@app.route('/submit_registration', methods=['POST'])
def submit_registration():
    name = request.form['name']
    usn=request.form['usn']
    branch = request.form['branch']
    semester = request.form['semester']
    email = request.form['email']
    
    # Check if the data already exists in the MongoDB collection
    if main_collection.find_one({"name": name, "usn":usn,"branch": branch, "semester": semester, "email": email}):
        return 'This data is already submitted.'
    
    # Insert the registration data into the MongoDB collection
    registration_data = {
        "name": name,
        "usn":usn,
        "branch": branch,
        "semester": semester,
        "email": email
    }
    main_collection.insert_one(registration_data)
    
    return redirect(url_for('registration_success'))

@app.route('/registration_success')
def registration_success():
    return 'Your response has been submitted.'

@app.route('/events.html')
def events():
    return render_template('events.html')

@app.route('/registration_form_1.html', methods=['GET', 'POST'])
def registration_form_1():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        usn = request.form['usn']
        branch = request.form['branch']
        semester = request.form['semester']
        email = request.form['email']
        num_participants = request.form['participants']
        duration = request.form['duration']


        if dance_collection.find_one({"name": name, "usn": usn, "branch": branch, "semester": semester, "email": email, "num_participants":num_participants,"duration":duration}):
            return 'This data is already submitted.'
        else:
            # Insert data into MongoDB
            reg_data = {
                "name": name,
                "usn": usn,
                "branch": branch,
                "semester": semester,
                "email": email,
                "num_participants": num_participants,
                "duration": duration
            }
            dance_collection.insert_one(reg_data)

        return redirect(url_for('registrations_success'))

    return render_template('registration_form_1.html')

@app.route('/registrations_success')
def registrations_success():
    return 'Your response has been submitted.'

if __name__ == '__main__':
    app.run(debug=True)
