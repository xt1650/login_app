
from flask import Flask
import webview
import sys
import threading

app = Flask(__name__)

@app.route('/')
def kayitOlPost(self,kullanici,eposta,sifre):
    self.response = {
        'kullaniciadi':kullanici,
        'eposta':eposta,
        'sifre' : sifre
    }
    print(self.response)

def start_server():
    app.run(host='0.0.0.0', port=80)

if __name__ == '__main__':

    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()

    webview.create_window("PyWebView & Flask", "index.html")
    webview.start()
    sys.exit()