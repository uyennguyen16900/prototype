from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/signin')
def signin_page():
    return render_template('signin.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/gallery')
def gallery_page():
    return render_template('gallery.html')

if __name__ == '__main__':
    app.run(debug=True)
