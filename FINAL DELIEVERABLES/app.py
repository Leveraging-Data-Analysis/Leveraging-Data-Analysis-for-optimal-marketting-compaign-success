from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def open_html():
    folder_path = 'C:/Users/samue/Desktop/'  # Specify the path to your desktop folder
    return send_from_directory(folder_path, 'Leveraging Data Analysis.html')

if __name__ == '__main__':
    app.run(debug=True)