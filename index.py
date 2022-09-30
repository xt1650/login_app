from flask import Flask,jsonify, request,render_template
import json
import webview


app = Flask(__name__,static_folder='./assets', template_folder='./templates')

class Api:
    def __init__(self):
        self.cancel_heavy_stuff_flag = False

    def girisPost(self,eposta,sifre):
        self.response = {
            'eposta':eposta,
            'sifre' : sifre
        }
        print(self.response)

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
   


if __name__=='__main__':
    api = Api()
    window = webview.create_window('PyWebView & Flask', app,js_api=api)
    webview.start()    



