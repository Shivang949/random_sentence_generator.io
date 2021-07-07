from flask import Flask, request, render_template
from main import random_story_generator
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action') == 'Submit':
            story = random_story_generator()
            return render_template('index.html', data=story)

    elif request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

