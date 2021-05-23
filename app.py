import os

from flask import Flask, render_template, request, redirect, send_file, url_for

from functions import list_files, download_file, upload_file


app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "add_bucket_name"

@app.route("/storage")
def storage():
    contents = list_files("S3_file_manager")
    return render_template('storage.html', contents=contents)


@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(f.filename)
        upload_file(f"{f.filename}", BUCKET)

        return redirect("/storage")


@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        output = download_file(filename, BUCKET)

        return send_file(output, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
