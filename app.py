from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, emit
from badge_generator import create_badge
from questions import questions   # import the questions list

app = Flask(__name__)
app.secret_key = "supersecretkey"
socketio = SocketIO(app)

players = {}
current_question = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/join', methods=['POST'])
def join():
    name = request.form['name']
    players[name] = 0
    session['player'] = name
    return redirect(url_for('quiz'))

@app.route('/quiz')
def quiz():
    return render_template("quiz.html", questions=questions)

@socketio.on('start_game')
def start_game():
    global current_question
    # pick the first question for now
    current_question = questions[0]
    emit('new_question', current_question, broadcast=True)

@socketio.on('submit_answer')
def submit_answer(data):
    player = session.get('player')
    answer = data['answer']
    if answer == current_question['correct']:
        players[player] += 1
    emit('update_leaderboard', players, broadcast=True)

@socketio.on('end_game')
def end_game():
    winner = max(players, key=players.get)
    badge_path = create_badge(winner)
    emit('game_over', {'winner': winner, 'badge': badge_path}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
