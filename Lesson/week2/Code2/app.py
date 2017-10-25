#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():

    teacher = {
            'name' : 'Aiden',
            'email': 'luojin@simplecloud.cn'
        }

    course = {
            'name': 'python Basic',
            'teacher':teacher, 
            'user_count':5348, 
            'price': 199.0, 
            'lab':None, 
            'is_private':False,
            'is_member_course':True, 
            'tag': ['python', 'big data', 'Linux']
        }
    return render_template('index.html', course=course)


