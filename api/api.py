from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json, os, time, datetime
from werkzeug.utils import secure_filename

from concurrent.futures import ThreadPoolExecutor
from model.model import predict
executor = ThreadPoolExecutor(2)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'you-will-never-guess!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Mouyu0407@localhost:3306/zombie_company?charset=UTF8MB4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

cors = CORS(app, supports_credentials=True)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'upload')

class Company(db.Model):
    ID = db.Column(db.String(10), primary_key=True)
    RegistrationTime = db.Column(db.String(4))
    RegistrationCapital = db.Column(db.SmallInteger)
    Industry = db.Column(db.String(10))
    District = db.Column(db.String(5))
    Type = db.Column(db.String(10))
    Ucsp = db.Column(db.String(5))  # 控制人类型
    ControllingPersonID = db.Column(db.String(10))

    def __init__(self, ID, RegistrationTime, RegistrationCapital, Industry, District, Type, Ucsp, ControllingPersonID):
        self.ID = ID
        self.RegistrationTime = RegistrationTime
        self.RegistrationCapital = RegistrationCapital
        self.Industry = Industry
        self.District = District
        self.Type = Type
        self.Ucsp = Ucsp
        self.ControllingPersonID = ControllingPersonID

class BatchRecord(db.Model):
    ID = db.Column(db.Integer, autoincrement=True, primary_key=True)
    CreatTime = db.Column(db.DateTime, nullable=False, default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    FilePath = db.Column(db.String(20), nullable=False)


@app.route('/SingleInput', methods=['POST'])
def SingleInput():
    data = request.get_json()
    print(data)
    ID = data['ID']
    if not Company.query.filter_by(ID=ID).all():
        RegistrationTime = data['RegistrationTime']
        RegistrationCapital = data['RegistrationCapital']
        Industry = data['Industry']
        District = data['District']
        Type = data['Type']
        Ucsp = data['Ucsp']
        ControllingPersonID = data['ControllingPersonID']
        try:
            company = Company(ID, RegistrationTime, RegistrationCapital, Industry, District, Type, Ucsp, ControllingPersonID)
            db.session.add(company)
            db.session.commit()
            return '保存成功！'
        except:
            return '出现错误，请重试！'
    else:
        return '此公司ID已存在！'

@app.route('/getCompanyInfo', methods=['GET'])
def getCompanyInfo():
    Companys = Company.query.order_by(Company.ID).all()
    companys_list = []
    for a in Companys:
        company = {}
        company['ID'] = a.ID
        company['RegistrationTime'] = a.RegistrationTime
        company['RegistrationCapital'] = a.RegistrationCapital
        company['Industry'] = a.Industry
        company['District'] = a.District
        company['Type'] = a.Type
        company['Ucsp'] = a.Ucsp
        company['ControllingPersonID'] = a.ControllingPersonID
        companys_list.append(company)
    #print(companys_list)
    return json.dumps(companys_list)

@app.route('/Upload', methods=['POST'])
def Upload():
    if not os.path.exists(UPLOAD_PATH):
        os.mkdir(UPLOAD_PATH)
    file = request.files.get('file')
    time = request.form.get('time')
    type = request.form.get('type')
    FILE_PATH = os.path.join(UPLOAD_PATH, time)
    if not os.path.exists(FILE_PATH):
        os.mkdir(FILE_PATH)
    #filename = secure_filename(file.filename)
    file.save(os.path.join(FILE_PATH,type+'.csv'))
    # 判断4个文件是否上传完毕
    if len(os.listdir(FILE_PATH))== 4:
        #print('4个文件上传完毕！')
        MODEL_PATH = "/Users/mouyu/Public/GitHub/zombie_company/api/model/ModelLR.plk"
        # 异步对文件进行预测
        executor.submit(predict, FILE_PATH, MODEL_PATH)
    return type + 'accept!'

@app.route('/getBatchRecord', methods=['GET'])
def getBatchRecord():
    records = BatchRecord.query.order_by(BatchRecord.ID).all()
    records_list = []
    for a in records:
        record = {}
        record['ID'] = a.ID
        record['CreatTime'] = a.CreatTime.strftime('%Y-%m-%d %H:%M:%S')
        record['FilePath'] = a.FilePath
        records_list.append(record)
    return json.dumps(records_list)

@app.route('/addBatchRecord', methods=['POST'])
def addBatchRecord():
    data = request.get_json()
    filepath = data['FilePath']
    record = BatchRecord()
    record.CreatTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    record.FilePath = filepath
    db.session.add(record)
    db.session.commit()
    return 'ok'

@app.route('/getPredictState/<filepath>', methods=["GET"])
def getPredictState(filepath):
    RESULT_PATH = os.path.join(os.path.join(UPLOAD_PATH, filepath), 'predictResult.csv')
    if os.path.exists(RESULT_PATH):
        return 'True'
    else:
        return 'False'

@app.route('/Download/<filepath>', methods=['GET'])
def Download(filepath):
    RESULT_PATH = os.path.join(UPLOAD_PATH,filepath)
    #print(RESULT_PATH)
    return send_from_directory(RESULT_PATH, 'predictResult.csv', as_attachment=True)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)