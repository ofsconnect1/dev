from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'author': 'xyz',
        # 'title': 'Blog Post 1',
        'content': '1st post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Abc',
        # 'title': 'Blog Post 2',
        'content': '2nd post content',
        'date_posted': 'April 21, 2018'
    }
]

# default
@app.route("/")
@app.route("/home")
def home():
    connections=[
    {
        'name': 'Abc Schafer',
    },
    {
        'name': 'Pqr Doe',
    },
    {
        'name': 'Xyz -',
    }
]
    return render_template('home.html',title='home', posts=posts,inside='true',connections=connections)


@app.route("/about")
def about():
    return render_template('about.html', title='About',inside='true')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register',inside='true', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'admin':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/profile", methods=['GET', 'POST'])
def profile():
    connections=[
    {
        'name': 'Abc Schafer',
    },
    {
        'name': 'Pqr Doe',
    },
    {
        'name': 'Xyz -',
    }
]

    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Profile created for {form.username.data}!', 'success')
        return redirect(url_for('profile'))
    return render_template('profile.html', title='Profile',inside='true', form=form,connections=connections, posts=posts)

@app.route("/notifications")
def notifications():

    return render_template('notifications.html', title='notifications',inside='true')


@app.route("/connections")
def connections():
    connections=[
    {
        'name': 'Abc Schafer',
    },
    {
        'name': 'Pqr Doe',
    },
    {
        'name': 'Xyz -',
    }
]

    pending_requests = [{'name':'Name1 Sirname1'},{'name':'Name2 Sirname2'},{'name':'Name3 Sirname3'}]

    return render_template('connections.html', title='connections',inside='true',pending_requests=pending_requests,connections=connections)

@app.route("/group", methods=['GET', 'POST'])
def group():
    connections=[
    {
        'name': 'Abc Schafer',
    },
    {
        'name': 'Pqr Doe',
    },
    {
        'name': 'Xyz -',
    }
]

    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Group created for {form.username.data}!', 'success')
        return redirect(url_for('group'))
    return render_template('group.html', title='Profile',inside='true', form=form,connections=connections, posts=posts)

if __name__ == '__main__':
    app.run(debug=True)