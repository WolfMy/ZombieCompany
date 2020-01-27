import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib
import os

#预处理函数 依次输入四个DataFrame 输出一个整合好的表
def preprocess(base, money_info, paient_info, year_report):
    #防止修改元数据
    base = base.copy()
    money_info = money_info.copy()
    paient_info = paient_info.copy()
    year_report = year_report.copy()

    #一、对年份进行缺失值填充 因为之后需要用年份来分组
    year_report["year"].fillna(method="ffill", inplace=True)
    money_info["year"].fillna(method="ffill", inplace=True)
    #二、对融资表 和 年报表 进行合并
    result_list = []
    years = [2015, 2016, 2017]
    for year in years:
        #一个表 某一年
        year_ = year_report[year_report["year"] == year]
        year_name = year_.columns
        #另一个表 某一年
        money_ = money_info[money_info["year"] == year]
        money_name = money_.columns
        #合起来
        merge_ = pd.merge(year_, money_, on=("ID", "year"))
        merge_.drop(columns="year", inplace=True)
        columns = list(set(merge_.columns.to_list()) - {"ID"})
        dic = {}
        for one in columns:
            dic[one] = str(year) + "_" + str(one)
        #处理完一年 改名字 放到列表里
        merge_.rename(columns=dic, inplace=True)
        result_list.append(merge_)
    #拼接
    two_tables = pd.merge(result_list[0], result_list[1])
    two_tables = pd.merge(two_tables, result_list[2])
    #三、对基本信息表的处理
    
    #测试集不提供flag吧
    #flag = base['flag'].copy()
    #base.drop(columns="flag", inplace=True)

    if "控制人ID" in base.columns:
        base.drop(columns="控制人ID", inplace=True)
    #四、将四个表合起来
    all_info = pd.merge(base, paient_info, on="ID")
    all_info = pd.merge(all_info, two_tables, on="ID")
    
    #测试集不提供flag吧
    #all_info['flag'] = flag

    return all_info

#对数据中的缺失值进行填充 无须返回值 直接修改
def fillna(data):
    #填充缺失值
    #1.注册时间 使用上一行的数据填充
    data["注册时间"].fillna(method="ffill", inplace=True)
    #2.注册资本 使用平均值填充
    data["注册资本"].fillna(data["注册资本"].mean(), inplace=True)
    #3.控制人持股比例 使用平均值填充
    data["控制人持股比例"].fillna(data["控制人持股比例"].mean(), inplace=True)
    #4.融资表 和 知识产权 全用0填充
    money_columns = [
        '2015_债权融资成本',
        '2015_债权融资额度',
        '2015_内部融资和贸易融资成本',
        '2015_内部融资和贸易融资额度',
        '2015_净利润',
        '2015_股权融资成本',
        '2015_股权融资额度',
        '2015_项目融资和政策融资成本',
        '2015_项目融资和政策融资额度',
        '2016_债权融资成本',
        '2016_债权融资额度',
        '2016_内部融资和贸易融资成本',
        '2016_内部融资和贸易融资额度',
        '2016_净利润',
        '2016_股权融资成本',
        '2016_股权融资额度',
        '2016_项目融资和政策融资成本',
        '2016_项目融资和政策融资额度',
        '2017_债权融资成本',
        '2017_债权融资额度',
        '2017_内部融资和贸易融资成本',
        '2017_内部融资和贸易融资额度',
        '2017_净利润',
        '2017_股权融资成本',
        '2017_股权融资额度',
        '2017_项目融资和政策融资成本',
        '2017_项目融资和政策融资额度',
        '专利',
        '商标',
        '著作权',
    ]
    for one in money_columns:
        data[one].fillna(0, inplace=True)
    #5.年报中一部分用平均值代替nan,净利润是营业总额*-0.1
    year_columns = [
        '2015_从业人数',
        '2015_资产总额',
        '2015_负债总额',
        '2015_营业总收入',
        '2015_主营业务收入',
        '2015_利润总额',
        '2015_纳税总额',
        '2015_所有者权益合计',
        '2016_从业人数',
        '2016_资产总额',
        '2016_负债总额',
        '2016_营业总收入',
        '2016_主营业务收入',
        '2016_利润总额',
        '2016_纳税总额',
        '2016_所有者权益合计',
        '2017_从业人数',
        '2017_资产总额',
        '2017_负债总额',
        '2017_营业总收入',
        '2017_主营业务收入',
        '2017_利润总额',
        '2017_纳税总额',
        '2017_所有者权益合计',
    ]
    jinglirun = [
        '2015_净利润',
        '2016_净利润',
        '2017_净利润',
    ]
    for one in year_columns:
        data[one].fillna(data[one].mean(), inplace=True)
    for one in jinglirun:
        tmp = one.split('_')[0]
        tmp2 = "营业总收入"
        tmp3 = tmp + "_" + tmp2
        data[one] = data[tmp3] * 0.1
    #6、其他的一些用前后值填充
    others = ['企业类型', '区域', '控制人类型', '行业']
    for one in others:
        data[one].fillna(method="ffill", inplace=True)

#特征工程 主要是离散化
def feature_engineering(data):
    vec = DictVectorizer(sparse=False, separator='_')
    train_set = vec.fit_transform(data.to_dict(orient="record"))
    train_set = pd.DataFrame(train_set)
    train_set.columns = vec.feature_names_
    return train_set.copy()

#将所有预处理函数整合在一起
def get_train_set(base, money_info, paient_info, year_report):
    processed_data = preprocess(base.copy(), money_info.copy(), paient_info.copy(), year_report.copy())
    fillna(processed_data)
    train_set = feature_engineering(processed_data)
    return train_set

def predict(FILE_PATH,MODEL_PATH):
    #读入数据
    base = pd.read_csv(os.path.join(FILE_PATH,'base.csv'),encoding="gbk")
    money_info = pd.read_csv(os.path.join(FILE_PATH,'money_info.csv'),encoding="gbk")
    paient_info = pd.read_csv(os.path.join(FILE_PATH,'paient_info.csv'),encoding="gbk")
    year_report = pd.read_csv(os.path.join(FILE_PATH,'year_report.csv'),encoding="gbk")

    #得到训练集
    train_set = get_train_set(base, money_info, paient_info, year_report)
    train_set = train_set[train_set["flag"]==1]

    LR = joblib.load(MODEL_PATH)
    
    result = get_result(train_set, LR)
    result.to_csv(os.path.join(FILE_PATH, "predictResult.csv"))
    return 'predit done!'

#传入训练集 和 预训练好的模型 函数内部自动保存结果 返回结果
def get_result(train_set, model):
    #传入的数据集不能有flag也不能有ID
    if "flag" in train_set.columns:
        X = train_set.drop(columns="flag")
    if "ID" in train_set.columns:
        ID = train_set["ID"]
        X = X.drop(columns="ID")
    result = pd.DataFrame()
    result["ID"] = ID
    result["pred"] = model.predict(X)
    return result