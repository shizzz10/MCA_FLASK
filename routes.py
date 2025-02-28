from app import app
from flask import render_template, session, redirect, url_for, flash
from functools import wraps
from forms import sign_in




# Decorator definition (as shown above)
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            flash('You need to log in first!', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function



# Define the login route
@app.route('/',  methods=['GET', 'POST'])
def index():
    return render_template('index.html')


# Define the about route
@app.route('/about')
def about():
    return render_template('about.html')


# Define the contact route
@app.route('/contact')
def contact():
    return render_template('contact.html')


# Define the committee route
@app.route('/committee')
def committee():
    return render_template('committee.html')


# Define the artists route
@app.route('/artists')
def artists():
    return render_template('artists.html')


# Define the events route
@app.route('/events')
def events():
    return render_template('events.html')


# Define the gallery route
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


# Define the membership route
@app.route('/membership')
def membership():
    return render_template('membership.html')


# Define the news route
@app.route('/news')
def news():
    return render_template('news.html')


# Define the open_event_post route
@app.route('/open_event_post')
def open_event_post():
    return render_template('open_event_post.html')


# Define the open_news_post route
@app.route('/open_news_post')
def open_news_post():
    return render_template('open_news_post.html')




# Define the login route
@app.route('/login',  methods=['GET', 'POST'])
def login():
    form = sign_in()  # Initialize the form
    if 'logged_in' in session:  # Check if user is logged in
        flash('You need to logout first!', 'warning')
        return redirect(url_for('admin'))

    if form.validate_on_submit():  # Check if the form is submitted and valid
        username = form.username.data
        password = form.password.data

        # Check if the username and password match the ones in the config
        if username == app.config['ADMIN_USERNAME'] and password == app.config['ADMIN_PASSWORD']:
            session['logged_in'] = True  # Store logged-in status in the session
            flash('Login successful!', 'success')
            return redirect(url_for('admin'))  # Redirect to a protected page
        else:
            flash('Invalid username or password', 'danger')  # Invalid login
            # print('not logged in')
            return redirect(url_for('admin'))

    return render_template('login.html', form=form)

# Define the login route
@app.route('/admin')
@login_required
def admin():
    # if 'logged_in' not in session:  # Check if user is logged in
    #     flash('You need to log in first!', 'warning')
    #     return redirect(url_for('login'))

    return render_template('admin_pages/admin.html')

# Define the login route
@app.route('/add_blog',  methods=['GET', 'POST'])
@login_required
def add_blog():
    return render_template('admin_pages/add_blog.html')

# Define the login route
@app.route('/add_news',  methods=['GET', 'POST'])
@login_required
def add_news():
    return render_template('admin_pages/add_news.html')

# Define the login route
@app.route('/add_obituary',  methods=['GET', 'POST'])
@login_required
def add_obituary():

    return render_template('admin_pages/add_obituary.html')

# Define the login route
@app.route('/add_event',  methods=['GET', 'POST'])
@login_required
def add_event():
    return render_template('admin_pages/add_event.html')

# Define the login route
@app.route('/add_artist',  methods=['GET', 'POST'])
@login_required
def add_artist():
    return render_template('admin_pages/add_artist.html')


# Define the login route
@app.route('/edit_about_us',  methods=['GET', 'POST'])
@login_required
def edit_about_us():
    return render_template('admin_pages/edit_about_us.html')


# Define the login route
@app.route('/edit_static_pages_content',  methods=['GET', 'POST'])
@login_required
def edit_static_pages_content():
    return render_template('admin_pages/edit_static_pages_content.html')


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)  # Remove the logged-in status from the session
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))  # Redirect to the login page