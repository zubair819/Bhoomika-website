from flask import Flask, render_template, request, redirect, url_for
import csv
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registration.html')
def registration():
    return render_template('registration.html')

@app.route('/submit_registration', methods=['POST'])
def submit_registration():
    name = request.form['name']
    branch = request.form['branch']
    semester = request.form['semester']
    email = request.form['email']
    event = request.form['event']
    
     # Check if the data already exists in the CSV file
    with open('registrations.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if [name, branch, semester, email, event] == row:
                return 'This data is already submitted.'
            
    with open('registrations.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, branch, semester, email, event])
    
    return redirect(url_for('registration_success'))

@app.route('/registration_success')
def registration_success():
    return 'Your response has been submitted.'

@app.route('/events.html')
def events():
    return render_template('events.html')

if __name__ == '__main__':
    app.run(debug=True)
