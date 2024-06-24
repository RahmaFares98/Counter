from flask import Flask, render_template, session, redirect, request, url_for

app = Flask(__name__)
app.secret_key = 'secret_key'  # for session

@app.route('/')
def index():
    if 'visit_count' not in session:
        session['visit_count'] = 0
    if session.get('flag', True):
        session['visit_count'] += 1  # Increment visit_count on every visit
    session['flag'] = True  # Reset the flag after checking
    if 'counter' not in session:
        session['counter'] = 0
    return render_template('index.html', visit_count=session['visit_count'], counter=session['counter'])

@app.route('/incrementby2', methods=['POST'])
def increment_by_2():
    session['counter'] += 2
    session['flag'] = False  # Prevent visit_count increment on redirect
    return redirect(url_for('index'))

@app.route('/increment', methods=['POST'])
def increment():
    increment_value = int(request.form.get('increment_value', 1))
    session['counter'] += increment_value
    session['flag'] = False  # Prevent visit_count increment on redirect
    return redirect(url_for('index'))

@app.route('/destroy_session', methods=['GET'])
def destroy_session():
    session.clear()
    return redirect(url_for('index'))

@app.route('/reset', methods=['GET'])
def reset():
    session['counter'] = 0
    session['flag'] = False  # Prevent visit_count increment on redirect
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)