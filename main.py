from flask import Flask, request, render_template, url_for
app = Flask(__name__)

items = [
    {
        'id': 1,
        'name': 'Manpower App',
        'description': '[some description]',
        'url': '[someurl.com]'
    },
    {
        'id': 2,
        'name': 'Row Counts',
        'description': '[some description]',
        'url': '[someurl.com]'
    }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html', title = 'Contact')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/items')
def item_route():
    return render_template('items.html', items=items, title = 'Items')

@app.route('/music')
def music():
    return render_template('music.html', title = 'Music')

if __name__ == '__main__':
    app.run(debug=True)