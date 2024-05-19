from flask import Flask, render_template
import os
import pandas as pd
from scraper import scrape_topics



app = Flask(__name__)

topic_list = scrape_topics().values.tolist()
print(topic_list[][0])

#index.html
@app.route('/')
def welcome():
    return render_template('index.html', topiclist=topic_list)


topiclist = [('3D', '/3d'),
             ('Ajax', '/ajax'),
             ('Algotrithm', '/algorithm')]
# Route to display CSV file
for topic, url in topiclist:
    def display_csv():
        data = pd.read_csv('data/Amp.csv', header=None)
        data = data.values.tolist()
        headers = data[0]  # Assuming first row is header
        rows = data[1:]     # Assuming data starts from second row
        return render_template('display_csv.html', headers=headers, rows=rows)
    
    app.add_url_rule(url, f'route_{url}', display_csv)

    






if __name__ == '__main__':
    app.run(debug=True)
