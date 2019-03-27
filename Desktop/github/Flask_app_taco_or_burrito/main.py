from classification import Classifier
from flask import *
from  PIL import Image
import os
app = Flask(__name__)

UPLOAD_FOLDER = './upload/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
flag=1
MODEL = None
#機械学習モデルにデータを投げる関数
def resp_predict(img_url):
    global MODEL
    global flag
    if flag:
        MODEL = Classifier()
        flag = 0

    img = Image.open(img_url)
    output = MODEL.predict(img)

    return output
@app.route("/", methods=['GET', 'POST'])
def home():

    #GETの場合、引数なしのページ
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            img_file = request.files['img_file']
            if img_file != "":
                filename = img_file.filename #画像ファイル名
                img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) #uploadフォルダに保存
                img_url = UPLOAD_FOLDER +filename

                result = resp_predict(img_url) #予測
                return render_template('home.html', img_url=img_url,result = result) #画像urlと予測結果の引数を含めた
        except:
            return render_template('home.html')

#web上に画像を表示されるための関数
@app.route("/upload/<filename>")
def image_show(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == "__main__":
    app.run(debug = True)