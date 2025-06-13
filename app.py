from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

votes = {'팀A': 0, '팀B': 0, '팀C': 0}
cheers = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if request.method == 'POST':
        team = request.form.get('team')
        if team in votes:
            votes[team] += 1
        return redirect('/results')
    return render_template('vote.html')

@app.route('/results')
def results():
    return render_template('results.html', votes=votes)

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/cheer/<cls>')
def cheer(cls):
    return render_template('cheer.html', cls=cls)

@app.route('/api/cheer', methods=['POST'])
def api_cheer():
    data = request.get_json()
    cls = data.get('cls')
    cheers[cls] = cheers.get(cls, 0) + 1
    return jsonify({'count': cheers[cls]})

@app.route('/api/cheer-count')
def api_cheer_count():
    cls = request.args.get('cls')
    return jsonify({'count': cheers.get(cls, 0)})

if __name__ == '__main__':
    app.run(debug=True)
