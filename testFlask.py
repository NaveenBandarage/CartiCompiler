from flask import Flask, request, render_template
from livereload import server
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['textbox']
    processed_text = text.upper()
    return processed_text

if __name__ == '__main__':
    app.run(debug=True)
    server = Server(app.wsgi_app)
    server.serve()


#export FLASK_APP=testFlask.py
#flask run
#this is how you deploy to the web.