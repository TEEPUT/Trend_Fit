import os
from flask import Flask, render_template, request, redirect, session
# from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from forms import RegisterForm, LoginForm
from models import db
from models import User
from werkzeug.security import check_password_hash

app = Flask(__name__)

@app.route('/Main.html')
def main():
    userid = session.get('userid', None)
    return render_template('Main.html', userid=userid)

@app.route('/Sub1.html')
def sub1():
    userid = session.get('userid', None)
    return render_template('Sub1.html', userid=userid)

@app.route('/Sub2.html')
def sub2():
    userid = session.get('userid', None)
    return render_template('Sub2.html', userid=userid)

@app.route('/Sub3.html')
def sub3():
    userid = session.get('userid', None)
    return render_template('Sub3.html', userid=userid)

@app.route('/Sub4.html')
def sub4():
    userid = session.get('userid', None)
    return render_template('Sub4.html', userid=userid)

@app.route('/Sub5.html')
def sub5():
    userid = session.get('userid', None)
    return render_template('Sub5.html', userid=userid)

@app.route('/Sub6.html')
def sub6():
    userid = session.get('userid', None)
    return render_template('Sub6.html', userid=userid)

@app.route('/Sub7.html')
def sub7():
    userid = session.get('userid', None)
    return render_template('Sub7.html', userid=userid)

@app.route('/Sub8.html')
def sub8():
    userid = session.get('userid', None)
    return render_template('Sub8.html', userid=userid)

@app.route('/Sub9.html')
def sub9():
    userid = session.get('userid', None)
    return render_template('Sub9.html', userid=userid)

@app.route('/Board.html')
def board():
    userid = session.get('userid', None)
    return render_template('Board.html', userid=userid)


@app.route('/Login.html', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        userid = form.data.get('userid')
        user = User.query.filter_by(userid=userid).first()
        if user and check_password_hash(user.password, form.data.get('password')):
            print('{}가 로그인 했습니다'.format(userid))
            session['userid'] = userid
            return redirect('/Main.html')
        form.userid.errors.append('Invalid userid or password')
    return render_template('Login.html', form=form)


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('userid', None)
    return redirect('/Main.html')

@app.route('/Register.html', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        usertable = User(
            email=form.data.get('email'),
            password=form.data.get('password')
        )
        usertable.userid = form.data.get('userid')

        db.session.add(usertable)
        db.session.commit()

        return redirect('/Login.html')
    return render_template('Register.html', form=form)

if __name__ == "__main__":

    basedir = os.path.abspath(os.path.dirname(__file__))
    dbfile = os.path.join(basedir, 'db.sqlite')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True #사용자에게 정보 전달완료하면 teadown. 그 때마다 커밋=DB반영
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #추가 메모리를 사용하므로 꺼둔다
    app.config['SECRET_KEY'] = 'ciyi8189'

    csrf = CSRFProtect()
    csrf.init_app(app)

    db.init_app(app) #app설정값 초기화
    db.app = app #Models.py에서 db를 가져와서 db.app에 app을 명시적으로 넣는다
    with app.app_context():
        db.create_all()  # DB 생성

    app.run(host="127.0.0.1", port=5000, debug=True)