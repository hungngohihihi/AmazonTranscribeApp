from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    try:
        # Thực hiện lệnh python3 ./main.py
        subprocess.run(["python3", "./main.py"])
        return 'Script executed successfully.'
    except Exception as e:
        return f'Error executing script: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
