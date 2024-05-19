from flask import Flask, render_template
import csv
import os

app = Flask(__name__)

# Function to read CSV file
def read_csv_file(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data


#index.html
@app.route('/')
def welcome():
    return "welcome"

# Route to display CSV file
def createtopicroutes(topic, url):
    @app.route(url)
    def display_csv():
        filename = os.path('/data',topic)  # Your CSV file name
        data = read_csv_file(filename)
        headers = data[0]  # Assuming first row is header
        rows = data[1:]     # Assuming data starts from second row
        return render_template('display_csv.html', headers=headers, rows=rows)

topiclist = [('home', '/home'),
            ('about', '/about'),
            ('contact', '/contact')]
for topic, url in topiclist:
    createtopicroutes(topic, url)






if __name__ == '__main__':
    app.run(debug=True)
