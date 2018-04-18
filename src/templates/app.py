import os
from flask import Flask, render_template, request

__author__='Sayali'

app = Flask(__name__, static_folder="images")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("Couldn't create uplaod directory: {}".format((target)))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print("Accept files:",filename)
        print("save it to: ",destination)
        upload.save(destination)

    return render_template("complete.html", image_name=filename)

if __name__ == "__main__":
    app.run(port=5000, debug= True)
