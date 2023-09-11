from flask import Flask

app = Flask(__name__)


@app.route('/account', method=['POST', 'GET'])
@login_required
def account():
    form = UpdateAccountDetailsForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        #comment 2 46
        current_user.email = form.email.data
        current_user.password = form.password.data
        current_user.year_group = form.year_group.data
        current_user.house = form.house.data
        db.session.commit()
    elif:
    return


if __name__ == '__main__':
    app.run()
