import os #디렉토리 절대 경로
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

dbdir = os.path.abspath(os.path.dirname(__file__)) #현재 파일이 있는 디렉토리 절대 경로
dbfile = os.path.join(dbdir, 'db.sqlite') #데이터베이스 파일을 만든다

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True #사용자 요청이 끝나면 커밋=DB반영 한다
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #추가 메모리를 사용하므로 꺼둔다

db = SQLAlchemy(app)

class User(db.Model): #데이터 모델을 나타내는 객체 선언
    __tablename__ = 'user_table' #테이블 이름
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
 
    def __repr__(self):
        return f"<User('{self.id}', '{self.username}', '{self.email}')>"
    
with app.app_context():
    db.create_all()

@app.route('/')
def hello():
	return 'Hello World!'