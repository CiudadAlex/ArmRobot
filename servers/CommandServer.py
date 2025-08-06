from flask import Flask, jsonify, request, render_template, make_response
from commanders.Commander import Commander
import threading

app = Flask(__name__)


@app.route('/known/<mode>', methods=['GET'])
def set_led(mode):
    print(f"Setting known mode: {mode}")
    success = Commander.execute(f"known {mode}")

    if success:
        return '', 204
    else:
        return f"Command {mode} not found", 400


@app.route('/ui', methods=['GET'])
def get_ui():
    return render_template('ui.html')


def run_server():
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8088, debug=False, use_reloader=False)).start()

