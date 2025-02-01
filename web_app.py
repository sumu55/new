from flask import Flask, render_template, request, jsonify
import asyncio
from LEGEND import run_attack  # Import directly from LEGEND.py

app = Flask(__name__)
ALLOWED_USER_ID = 6494426295

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/attack', methods=['POST'])
def attack():
    user_id = request.form.get('user_id')
    if int(user_id) != ALLOWED_USER_ID:
        return jsonify({'status': 'error', 'message': 'Unauthorized user'})
    
    ip = request.form.get('ip')
    port = request.form.get('port')
    duration = request.form.get('duration')
    
    # Create event loop and run attack
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_attack(user_id, ip, port, duration, None))
    
    return jsonify({'status': 'success', 'message': 'Attack launched successfully'})

if __name__ == '__main__':
    app.run(debug=True)
