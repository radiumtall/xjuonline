from  flask import render_template,Blueprint,redirect,url_for,flash,request,session,make_response
from flask_login import LoginManager,login_user,UserMixin,logout_user,login_required,current_user
from application.Form import Login_Form,Func_User,Func_Admin
from application.UserDb import Users
from application.DatasDb import Datas,db
from  application.Safe import check_arg
import os.path
import json
import datetime
import html
import cgi
import xlwt
from io import BytesIO


XJUSEC=Blueprint('xjuonline',__name__)

@XJUSEC.route('/welcome')
def index():
    # print(session)
    if  current_user.is_authenticated:
        return render_template('appliacation/index.html',datetime=str(datetime.date.today()),name=cgi.escape(session['stu_name']))
    else:
        return redirect(url_for('xjuonline.login'))
            # return "login"

@XJUSEC.route('/login')
def login():
    form = Login_Form()
    return render_template('appliacation/login.html', form=form)
@XJUSEC.route('/check_login',methods=['GET','POST'])
def check_login():
    if request.method == "POST":
        form = Login_Form()
        username = form.username.data
        password = form.password.data
        if check_arg(username,password):
            
        # print(username+passwd)
            if username!="" and password != "":
                user = Users.query.filter_by(username=username).first()
                if user is not  None and user.password==password:
                    login_user(user)
                    session['name'] = user.username
                    session['flag'] = user.flag
                    session['stu_name'] = user.stu_name
                    return redirect(url_for('xjuonline.index'))
                else:
                    return redirect(url_for('xjuonline.login'))
            else:
                return  render_template('hack.html')
        else:
            return  render_template('hack.html')
    else:
        return render_template('hack.html')
@XJUSEC.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已退出登录')
    return redirect(url_for('index'))


@XJUSEC.route('/func',methods=['GET','POST'])
def func_user():
    if  current_user.is_authenticated:
        form = Func_User()
        return  render_template('appliacation/func.html',form=form)
    else:
        return redirect(url_for('xjuonline.login'))

@XJUSEC.route('/info',methods=['GET','POST'])
def GetInfo():
    form = Func_User()
    mes = ''
    status_1 = form.status_1.data
    status_2 = form.status_2.data
    status_3 = form.status_3.data
    stu_name = form.stu_name.data
    time = str(datetime.date.today())
    allow_data_status = ['Yes','No']
    if status_1 not in allow_data_status or status_2 not in allow_data_status or status_3 not in allow_data_status or stu_name == '' or stu_name == None:
        mes = '请正确填写数据！'
        return  render_template('appliacation/message.html',message=mes)
    else:
        if  session['stu_name'] == stu_name:
            if check_arg(status_1,status_2,status_3,stu_name) == False:
                return render_template('hack.html')
            else:
                data = Datas.query.filter_by(username=session['name'])
                if data is not None :
                    try:
                        if data[-1].time == str(datetime.date.today()):
                            mes = '你今天已经提交过啦！'
                            return  render_template('appliacation/message.html',message=mes)
                    except:
                        pass
                try:
                    data_in_db = Datas(status_1=status_1,status_2=status_2,status_3=status_3,stu_name=stu_name,time=time,username=session['name'])
                    db.session.add(data_in_db)
                    db.session.commit()
                    mes =  '成功提交'
                    return  render_template('appliacation/message.html',message=mes)
                except Exception as e :
                    print(e)
                    sp = '--'
                    open('log','a+').write(time+sp+session['name']+e)
                    mes =  '写入数据库出错!请及时联系管理员'
                    return  render_template('appliacation/message.html',message=mes)
        else:
            mes = '姓名和账号不匹配!'
            return  render_template('appliacation/message.html',message=mes)

@XJUSEC.route('/admin_for_download_datas',methods=['GET','POST'])
def func_admin():
    if  current_user.is_authenticated:
        if session['flag'] != '1':
            ip = request.remote_addr
            open('log','a+').write(str(datetime.date.today())+'--'+session['name']+'--'+ip+'\n')
            return render_template('hack.html')
        form = Func_Admin()
        if request.method == "POST":
            action = form.action.data
            time = form.time.data
        else :
            time = str(datetime.date.today())
            action = 'view'

        if action == 'view':
            num = 0
            id_list= []
            info={}
            if time == 'all':
                datas_v = Datas.query.all()
            else:
                datas_v = Datas.query.filter(Datas.time.like("%"+time+"%" if time is not None else "")).all()
            for i in datas_v:
                num += 1
                data = {}
                data['time'] = i.time
                data['username'] = i.username
                data['name'] = i.stu_name
                data['s1'] = i.status_1
                data['s2'] = i.status_2
                data['s3'] = i.status_3
                info[str(num)]=data
            for j in range(num):
                id_list.append(str(j+1))
            return  render_template('appliacation/admin.html',id_list=id_list,info=info,form=form)
        if action == 'download':
            if time == 'all':
                datas_v = Datas.query.all()
            else:
                datas_v = Datas.query.filter(Datas.time.like("%"+time+"%" if time is not None else "")).all()
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet(time, cell_overwrite_ok=True)
            row0 = ['id', 'time', 'stu_id', 'stu_name','status_1','status_2','status_3','type']
            for i in range(0, len(row0)):  # 将这些字段写入xls文件
                ws.write(0, i, row0[i])
            k = 1
            for i in datas_v:  # 循环每一列
                for j in range(int(len(row0))):# 在每列添加数据
                    if j == 0:
                        ws.write(k, j, k)
                    if j == 1:
                        ws.write(k, j, i.time)
                    if j == 2:
                        ws.write(k, j, i.username)
                    if j == 3:
                        ws.write(k, j, i.stu_name)
                    if j == 4:
                        ws.write(k, j, i.status_1)
                    if j == 5:
                        ws.write(k, j, i.status_1)
                    if j == 6:
                        ws.write(k, j, i.status_1)
                    if j == 7:
                        flag = Users.query.filter_by(username=i.username)[0].flag
                        if flag == '1':
                            tmp = '管理员'
                        if flag == '2':
                            tmp = "学生"
                        if flag == "3":
                            tmp = "老师"
                        ws.write(k, j, tmp)
                k += 1
            sio = BytesIO()  # 将获取的数据在内存中写，有时会用到StringIO()
            wb.save(sio)  # 将文件流保存
            sio.seek(0)  # 光标
            response = make_response(sio.getvalue())  # 
            response.headers['Content-type'] = 'application/vnd.ms-excel'  # 指定返回的类型
            response.headers['Transfer-Encoding'] = 'chunked'
            response.headers['Content-Disposition'] = 'attachment;filename={}.xls'.format(time)  # 设定用户浏览器显示的保存文件名
            return response
    else:
        return redirect(url_for('xjuonline.login'))
