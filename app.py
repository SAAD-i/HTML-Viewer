from flask import Flask, render_template, request
from markupsafe import Markup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    html_content = ""
    if request.method == 'POST':
        if 'html_file' in request.files and request.files['html_file'].filename != '':
            html_file = request.files['html_file']
            html_content = html_file.read().decode('utf-8')
        else:
            html_content = request.form.get('html_content')
    return render_template('index.html', html_content=Markup(html_content))

if __name__ == '__main__':
    app.run(debug=True)
