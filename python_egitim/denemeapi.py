from flask import Flask,jsonify, request,render_template
import json
import webview


app = Flask(__name__,static_folder='./assets', template_folder='./templates')

class Api:
    def __init__(self):
        self.cancel_heavy_stuff_flag = False

    def girisPost(self,eposta,sifre):
        response = {
            'eposta':eposta,
            'sifre' : sifre
        }
        return response

    def kayitOlPost(self,kullanici,eposta,sifre):
        self.response = {
            'kullaniciadi':kullanici,
            'eposta':eposta,
            'sifre' : sifre
        }
        print(self.response)

@app.route("/kayit",methods=['POST', 'GET'])
def kayitol():
    return render_template('kayitol.html')

@app.route("/",methods=['POST', 'GET'])
def index():
    return render_template('index.html')
   


@app.route("/login",methods=['POST', 'GET'])
def index11():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json1 = request.get_json()
        return 
    else:
        return 'Content-Type not supported!'


if __name__=='__main__':
    api = Api()
    window = webview.create_window('PyWebView & Flask', app,js_api=api)
    webview.start()    



