from flask import Flask, render_template
import csv
import os
import pandas as pd

app = Flask(__name__)


#index.html
@app.route('/')
def welcome():
    return render_template('index.html')


topiclist = [('3D', '/3d'),
            ('Ajax', '/ajax'),
            ('Algotrithm', '/algorithm')]
# Route to display CSV file
for topic, url in topiclist:
    def display_csv():
        #filename = 'C:/Users/Sparsh Celly/Desktop/Flask Projects/GithubScraper/data/3D.csv' # Your CSV file name
        data = pd.read_csv('../data/3d.csv')
        #data = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        headers = data[0]  # Assuming first row is header
        rows = data[1:]     # Assuming data starts from second row
        return render_template('display_csv.html', headers=headers, rows=rows)
    
    app.add_url_rule(url, f'route_{url}', display_csv)

    






if __name__ == '__main__':
    app.run(debug=True)
