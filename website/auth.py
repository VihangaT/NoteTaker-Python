from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    data= request.form
    print(data)
    return render_template("login.html",text="Testing")


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email=request.form.get('email')
        firstName=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        if len(email)<8:
            flash("Email must be greater than 8 charactors",category='error')
        elif len(firstName) <2 :
            flash("Firstname must be greater than 2 charactors",category='error')
        elif password1 != password2:
            flash("Your passwords don't match",category='error')
        elif len(password1) <7 :
            flash("Password must be greater than 7 charactors",category='error')
        else:
            flash("User Account Created",category='Success')
            print(request.form)

    return render_template("sign_up.html")