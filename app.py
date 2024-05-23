from flask import Flask, request, render_template
import pandas as pd
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = request.form['user_id']  # Captures the user ID but does not use it in this simplified example
    time.sleep(5)
    return render_template('results.html', recommendations=recommend.to_html(index=False, classes='table'))

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/refine', methods=['GET', 'POST'])
def refine():
    if request.method == 'POST':
        user_id = request.form['user_id']
        song_selected = request.form['song_selected']
        likeness = request.form['likeness']
        # Here, you would process the refinement
        return render_template('refine.html', message="Preferences saved!", songs=songs_sample)
    return render_template('refine.html', songs=songs_sample)


if __name__ == '__main__':
    app.run(debug=True)
