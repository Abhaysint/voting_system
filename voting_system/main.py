import json
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

vote_count = {'Candidate 1': 0, 'Candidate 2': 0}

# Load previous vote counts from file if it exists
try:
    with open('votes.json', 'r') as file:
        vote_count = json.load(file)
except FileNotFoundError:
    pass


@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if request.method == 'POST':
        selected_candidate = request.form['candidate']
        vote_count[selected_candidate] += 1

        # Save the updated vote counts to file
        with open('votes.json', 'w') as file:
            json.dump(vote_count, file)

        return render_template('thank_you.html')
    return render_template('vote.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reset')
def reset():
    vote_count['Candidate 1'] = 0
    vote_count['Candidate 2'] = 0
    return redirect('/')


@app.route('/results')
def results():
    return render_template('results.html', vote_count=vote_count)


if __name__ == '__main__':
    app.run(debug=True)
