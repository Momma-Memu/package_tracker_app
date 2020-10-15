from flask import Flask, render_template, redirect, url_for
from app.shipping_form import ShippingForm
from app.login_form import LoginForm
from config import Config
from flask_migrate import Migrate
from app.models import db, Package, User
from flask_login import LoginManager, current_user, logout_user, login_user, login_required


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view='login'


@login.user_loader
def load_user(id):
    if id:
        return User.query.get(int(id))
    else:
        return None



# @app.route('/')
# @login_required
# def base_route():
#     print(current_user.id)
#     packages = Package.query.all()
#     return render_template('package_status.html', packages=packages)

@app.route('/')
@login_required
def base_route():
    packages = Package.query.filter(Package.user_id == current_user.id).all()
    return render_template('package_status.html', packages=packages)



@app.route('/new_package', methods=["GET", "POST"])
@login_required
def new_package():
    form = ShippingForm()

    userId = int(current_user.id)
    print(userId)

    if form.validate_on_submit():
        data = form.data
        Package.advance_all_locations()
        new_package = Package(
            sender=data["sender"],
            recipient=data["recipient"],
            origin=data["origin"],
            destination=data["destination"],
            location=data["origin"],
            user_id=userId
            )
        db.session.add(new_package)
        db.session.commit()
        return redirect('/')

    return render_template('shipping_request.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('.base_route'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter(User.username == username).first()
        if not username or not user.check_password(password):
            return redirect(url_for(".login"))
        login_user(user)
        return redirect(url_for('.base_route'))
    return render_template('login.html', form=form)

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))