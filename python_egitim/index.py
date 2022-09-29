import hashlib
import webview


        
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
        response = {
            'kullaniciadi':kullanici,
            'eposta':eposta,
            'sifre' : sifre
        }
        print(response)

   


if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Login', 'index.html', js_api=api)
    webview.start()