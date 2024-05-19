from flask import Flask, render_template
import csv

app = Flask(__name__)

# Function to read CSV file
def read_csv_file(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

# Route to display CSV file
@app.route('/')
def display_csv():
    filename = 'data\3D.csv'  # Your CSV file name
    data = read_csv_file(filename)
    headers = data[0]  # Assuming first row is header
    rows = data[1:]     # Assuming data starts from second row
    return render_template('display_csv.html', headers=headers, rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
