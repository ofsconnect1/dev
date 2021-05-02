from flask import render_template, url_for, flash, redirect, request
from OFSConnect import app, db, bcrypt
from OFSConnect.forms import RegistrationForm, LoginForm, UpdateProfileForm, PostForm
from OFSConnect.models import Post,User
import secrets
import os
from PIL import Image
from flask_login import login_user, current_user, logout_user, login_required

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
'''
@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
@login_required
def home():
    if current_user.is_authenticated: # This is not required as we are using @login_required decorator
        print("@@@@@@@@@@@@@@ :",current_user.is_authenticated)
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
        # image_file = url_for('static',filename='profile_pics/'+current_user.image_file)
        # return render_template('home.html',title='home', posts=posts,inside='true',connections=connections,image_file=image_file)
        print("------------====================================",request.method)
        form = PostForm()
        if request.method == 'POST':
            print("POST method aahe")
            # if form.validate_on_submit():
            print("Hi 1")
            post = Post(title='title',content=form.content.data, author=current_user)
            print("Hi 2",post)
            db.session.add(post)
            db.session.commit()
            flash('Your post has been created!', 'success')
            return redirect(url_for('home'))
        else :
            print("GET method aahe")
            image_file = url_for('static',filename='profile_pics/'+current_user.image_file)
            return render_template('home.html',title='home',inside='true',connections=connections,image_file=image_file,form=form, posts=posts)
        image_file = url_for('static',filename='profile_pics/'+current_user.image_file)
        return render_template('home.html',title='home',inside='true',connections=connections,image_file=image_file,form=form,posts=posts)
    else : # This is not required as we are using @login_required decorator
        flash(f'Please login to access the site!', 'warning')
        return redirect(url_for('login'))
'''

@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
@login_required
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
    form = PostForm()
    image_file = url_for('static',filename='profile_pics/'+current_user.image_file)
    if request.method =='GET':
        print("GET method aahe")
        print("Hi 2",current_user.posts)
        posts = Post.query.all()
        
        return render_template('home.html',title='home',inside='true',connections=connections,image_file=image_file,form=form,posts=posts)
    
    elif request.method =='POST':
        print("POST method aahe",form.content.data)
        if form.validate_on_submit():
            print("validating...............................")
            print("validating submit method aahe")
            # if form.validate_on_submit():
            print("Hi 1")
            print("Here---- ", type(form.title.data), len(form.title.data))
            title='1'
            if len(form.title.data)==0:
                title = form.content.data[0:6]
            else :
                title = form.title.data
            
            post = Post(title=title,content=form.content.data, author=current_user)
            print("Hi 2",post.content)
            db.session.add(post)
            db.session.commit()
            flash('Your post has been created!', 'success')
            return redirect(url_for('home'))
        return render_template('home.html',title='home',inside='true',connections=connections,image_file=image_file,form=form,posts=posts)
    

    






'''

        image_file = url_for('static',filename='profile_pics/'+current_user.image_file)
        form = UpdateProfileForm()
        if form.validate_on_submit():
            print("---------------------------------------------------------------------------------------------")
            if form.picture.data:
                picture_file = save_picture(form.picture.data)
                current_user.image_file = picture_file
            current_user.username = form.username.data
            current_user.email = form.email.data
            db.session.commit()
            flash(f'Your Profile updated successfully!', 'success')
            return redirect(url_for('edit_profile'))
        elif request.method =='GET':
            form.username.data=current_user.username
            form.email.data=current_user.email
        return render_template('edit_profile.html', title='Event',inside='true', form=form,connections=connections, posts=posts, image_file = image_file)
    else :
        flash(f'Please login to access the site!', 'warning')
        return redirect(url_for('login'))



















'''
@app.route("/about")
@login_required
def about():
    if current_user.is_authenticated:
        print("I am here..................")
        image_file = url_for('static',filename='profile_pics/'+current_user.image_file)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2",image_file)
        return render_template('about.html', title='About',inside='true',image_file=image_file)
    else :
        flash(f'Please login to access the site!', 'warning')
        return redirect(url_for('login'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! You can login now.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register',inside='true', form=form)

"""
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",bcrypt.check_password_hash(user.password, form.password.data))
        # if form.email.data == 'admin@gmail.com' and form.password.data == 'admin':
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            print("Hello................")
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next_page')
            flash(f'You have been logged in!, {user.username}', 'success')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

"""

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)





@app.route("/logout")
@login_required
def logout():
    logout_user()
    
    return redirect(url_for('login'))


@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    if current_user.is_authenticated:
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
        image_file = url_for('static',filename='profile_pics/'+current_user.image_file)
        form = RegistrationForm()
        if form.validate_on_submit():
            flash(f'Profile created for {form.username.data}!', 'success')
            return redirect(url_for('profile'))
        return render_template('profile.html', title='Profile',inside='true', form=form,connections=connections, posts=posts, image_file=image_file)
    else :
        flash(f'Please login to access the site!', 'warning')
        return redirect(url_for('login'))

@app.route("/notifications")
@login_required
def notifications():
    if current_user.is_authenticated:
        image_file = url_for('static',filename='profile_pics/'+current_user.image_file)
        return render_template('notifications.html', title='notifications',inside='true', image_file=image_file)
    else :
        flash(f'Please login to access the site!', 'warning')
        return redirect(url_for('login'))


@app.route("/connections")
@login_required
def connections():
    if current_user.is_authenticated:
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
        image_file = url_for('static',filename='profile_pics/'+current_user.image_file)
        pending_requests = [{'name':'Name1 Sirname1'},{'name':'Name2 Sirname2'},{'name':'Name3 Sirname3'}]

        return render_template('connections.html',image_file=image_file, title='connections',inside='true',pending_requests=pending_requests,connections=connections)
    else :
        flash(f'Please login to access the site!', 'warning')
        return redirect(url_for('login'))

@app.route("/group", methods=['GET', 'POST'])
@login_required
def group():
    if current_user.is_authenticated:
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
    else :
        flash(f'Please login to access the site!', 'warning')
        return redirect(url_for('login'))


@app.route("/page", methods=['GET', 'POST'])
@login_required
def page():
    if current_user.is_authenticated:
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
            flash(f'Page created for {form.username.data}!', 'success')
            return redirect(url_for('page'))
        return render_template('page.html', title='Page',inside='true', form=form,connections=connections, posts=posts)
    else :
        flash(f'Please login to access the site!', 'warning')
        return redirect(url_for('login')) 



@app.route("/event", methods=['GET', 'POST'])
@login_required
def event():
    if current_user.is_authenticated:
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
            flash(f'Event created for {form.username.data}!', 'success')
            return redirect(url_for('event'))
        return render_template('event.html', title='Event',inside='true', form=form,connections=connections, posts=posts)
    else :
        flash(f'Please login to access the site!', 'warning')
        return redirect(url_for('login'))


def save_profile_pic(form_pic):
    random_hex = secrets.token_hex(8)
    _, file_ext = os.path.splitext(form_pic.filename) # _ is filename as we are not going to use this we took it as "_"
    picture_file_name = random_hex + file_ext
    picture_path = os.path.join(app.route,'static/profile_pics',picture_file_name)
    form_pic.save(picture_path)
    return picture_file_name

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route("/edit_profile", methods=['GET', 'POST'])
@login_required
def edit_profile():
    if current_user.is_authenticated:
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
        image_file = url_for('static',filename='profile_pics/'+current_user.image_file)
        form = UpdateProfileForm()
        if form.validate_on_submit():
            print("---------------------------------------------------------------------------------------------")
            if form.picture.data:
                picture_file = save_picture(form.picture.data)
                current_user.image_file = picture_file
            current_user.username = form.username.data
            current_user.email = form.email.data
            db.session.commit()
            flash(f'Your Profile updated successfully!', 'success')
            return redirect(url_for('edit_profile'))
        elif request.method =='GET':
            form.username.data=current_user.username
            form.email.data=current_user.email
        return render_template('edit_profile.html', title='Event',inside='true', form=form,connections=connections, posts=posts, image_file = image_file)
    else :
        flash(f'Please login to access the site!', 'warning')
        return redirect(url_for('login'))



@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')

"""
@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))"""
