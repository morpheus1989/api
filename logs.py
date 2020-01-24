from flask import g

def log():
    print(g.user)