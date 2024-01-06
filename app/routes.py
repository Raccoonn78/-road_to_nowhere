from flask import (jsonify, current_app, render_template ,  
                    Flask, render_template, request, redirect,  
                    url_for, Blueprint, request, flash, make_response, session)
from sqlalchemy import func
# from flask_script import Manager, Command, Shell
from forms import ContactForm
from db import conn
from sqlalchemy import create_engine
from decorators.errors_catch import catch_error
import logging
from db.db_main import BaseModel
import json

bp = Blueprint('routes', __name__)

@bp.route('/loging/',  methods=['post', 'get'])
def autoriz():

    message = ''
    username=''
    password=''
    logging.info(f"{request.method}")
    if request.method == 'POST':
        
        username = request.form.get('username')  # запрос к данным формы
        password = request.form.get('password')
    logging.info(f"{message}>>{username}>>{password}>>")
    if username == 'root' and password == 'root':
        message = "Correct username and password"
        return redirect(url_for('routes.all_table',  _external=True) )
    else:
        message = "Wrong username or password"

    return render_template('autorizat.html' , message=message)




@bp.route('/contact/', methods=['get', 'post'])
def contact():   
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        print(name)
        print(email)
        print(message)
	    # здесь логика базы данных
        print("\nData received. Now redirecting ...")
        logging.info(f'contact>>{name}>>{email}>>{message} ')
        return redirect(url_for('routes.contact',  _external=True) )

    return render_template('contact.html', form=form)




@bp.route('/cookie/')
def cookie(): # проверка на существование куки
    if not request.cookies.get('foo'):
        res = make_response("Setting a cookie")
        res.set_cookie('foo', 'bar', max_age=60*60*24*365*2)
    else:
        res = make_response(f"Value of cookie foo is {request.cookies.get('foo')}")
    return res

@bp.route('/delete-cookie/')
def delete_cookie():
    res = make_response("Cookie Removed")
    res.set_cookie('foo', 'bar', max_age=0)
    return res



@bp.route('/article/', methods=['POST',  'GET'])
def article():
    if request.method == 'POST':
        logging.info(request.form)
        res = make_response("")
        res.set_cookie("font", request.form.get('font'), 60*60*24*15)
        res.headers['location'] = url_for('routes.article')
        return res, 302 # 302 означает что произошел редирект 

    return render_template('article.html')


@bp.route('/visits-counter/')
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # чтение и обновление данных сессии
    else:
        session['visits'] = 1  # настройка данных сессии
    return "Total visits: {}".format(session.get('visits'))

@bp.route('/delete-visits/')
def delete_visits():
    session.pop('visits', None)  # удаление данных о посещениях
    return 'Visits deleted'



@bp.route('/all_table_db/') 
def all_table(): # получение всех таблиц из БД
    logging.info(f"{BaseModel.get_all_tables()}")
    if BaseModel.get_all_tables():
        return json.dumps(BaseModel.get_all_tables())
    else:
        return json.dumps({'talbe':"CLEAR"})