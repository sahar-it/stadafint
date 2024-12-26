from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for simplicity
customers = []
bookings = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        customers.append({'name': name, 'email': email})
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        service = request.form['service']
        date = request.form['date']
        bookings.append({'customer_name': customer_name, 'service': service, 'date': date})
        return redirect(url_for('home'))
    return render_template('book.html', customers=customers)

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/bookings')
def view_bookings():
    return render_template('bookings.html', bookings=bookings)

@app.route('/services', methods=['GET', 'POST'])
def services():
    return render_template('services.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/Download_app', methods=['GET', 'POST'])
def Download_app():
    return render_template('Download_app.html')


app.run(debug=True)
