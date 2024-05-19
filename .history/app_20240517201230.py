from flask import Flask, render_template
import os
import pandas as pd
from scraper import scrape_topics



app = Flask(__name__)

topic_list = scrape_topics()['title'].values.tolist()
print(topic_list)

#index.html
@app.route('/')
def welcome():
    return render_template('index.html', topiclist=topic_list)


# topiclist = [('3D', '/3d'),
#              ('Ajax', '/ajax'),
#              ('Algotrithm', '/algorithm')]
# Route to display CSV file

@app.route('/hey')
def display_csv():
        filename = 'data/' + '3D' + '.csv'
        data = pd.read_csv(filename, header=None)
        data = data.values.tolist()
        headers = data[0]  # Assuming first row is header
        rows = data[1:]     # Assuming data starts from second row
        return render_template('display_csv.html', headers=headers, rows=rows)

for topic, desc, url in scrape_topics().values.tolist():
    def nothing():
        return "nothing"
    
    route_path = '/' + topic.strip().lower()
    print(route_path)
    app.add_url_rule(route_path, f'route_{topic}', nothing)

    






if __name__ == '__main__':
    app.run(debug=True)
