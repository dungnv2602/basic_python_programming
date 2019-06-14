from flask import Flask, render_template
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.csrf import CSRFProtect, CSRFError
from wtforms import StringField, IntegerField, PasswordField, Form, FormField
from wtforms.validators import InputRequired, Length, AnyOf

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LdW844UAAAAAJ-eELC_SazaO5_nFvzJvhLiaytg'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LdW844UAAAAAC93KscNMhsOv5yXEr4MRRirxRC7'
# app.config['TESTING'] = True

csrf = CSRFProtect(app)


@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400


class TelephoneForm(Form):
    country_code = IntegerField('country code')
    area_code = IntegerField('area code')
    number = StringField('number')


class LoginForm(FlaskForm):

    username = StringField('username', validators=[InputRequired('A username is required!'), Length(min=5, max=10, message='Must be between 5 and 10 characters.')])

    password = PasswordField('password', validators=[InputRequired('Password is required!')])

    gender = StringField('gender', validators=[InputRequired('Gender is required!'), AnyOf(values=['male', 'female'])])

    home_phone = FormField(TelephoneForm)

    office_phone = FormField(TelephoneForm)

    recaptcha = RecaptchaField()


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = LoginForm()

    if form.validate_on_submit():
        return '<h1>The username is {}. The password is {}.'.format(form.username.data, form.password.data)
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
