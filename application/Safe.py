from flask import session,request
import datetime
def check_arg(*args):
    black_list = [
    'select',
    'union',
    ' ',
    '/**/',
    "'",
    '"',
    "-",
    '+',
    '}',
    '{',
    ')',
    '(',
    '#',
    ',',
    'cat',
    'ls',
    'mv',
    'cp',
    'add'
    ]
    sp = '--'
    time = str(datetime.date.today())
    for i in args:
        for j in black_list :
            if j in i:
                ip = request.remote_addr
                open('log','a+').write(time+sp+ip+sp+i+'\n')
                return False
            else :
                return True