from flask import Flask, render_template, send_from_directory
import subprocess
import os

app = Flask(__name__, template_folder=os.path.dirname(os.path.abspath(__file__)))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    try:
        # Thực hiện lệnh python3 ./main.py
        subprocess.run(["python3", "./importFile/main.py"])
        return 'Script executed successfully.'
    except Exception as e:
        return f'Error executing script: {str(e)}'
    
@app.route('/output-file')
def get_output_file():
    try:
        # Đường dẫn đến tệp output.txt
        file_path = ('/Users/hung/Documents/GitHub/AmazonTranscribeApp/texts/output.txt')

        # Trả về nội dung của tệp output.txt
        with open(file_path, 'r') as file:
            content = file.read()
        
        return content

    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
