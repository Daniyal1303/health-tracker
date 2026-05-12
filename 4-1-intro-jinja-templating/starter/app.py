from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user = {'username': 'Daniyal',}
    items = ['item1','item2','item3'] 
    return render_template('index.html', title='Home', user=user, items=items)

if __name__ == '__main__':
    app.run(debug=True)
