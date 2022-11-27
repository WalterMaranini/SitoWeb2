from flask import Flask, render_template, redirect, request, send_from_directory
from werkzeug.utils import secure_filename

import sqlite3
import os

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

DataBasePath = './database.db'
StaticsPath = "./statics"


@app.route('/')
def index():
    connection = sqlite3.connect(DataBasePath)
    connection.row_factory = sqlite3.Row
    posts = connection.execute('SELECT * FROM Posts').fetchall()
    connection.close()
    return render_template('Index.html', posts=posts)


@app.route('/<int:idx>/delete', methods=('POST',))
def delete(idx):
    connection = sqlite3.connect(DataBasePath)
    connection.row_factory = sqlite3.Row
    connection.execute('DELETE FROM Posts WHERE id=?', (idx,))
    connection.commit()
    connection.close()
    return redirect('/')


@app.route('/<int:idr>/download', methods=('POST',))
def download(idr):
    connection = sqlite3.connect(DataBasePath)
    connection.row_factory = sqlite3.Row
    row = connection.execute('SELECT info FROM Posts WHERE id=?', (idr,)).fetchone()
    connection.close()
    return send_from_directory(StaticsPath, row['info'], as_attachment=True)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        tit = request.form['title']
        info = request.form['content']
        connection = sqlite3.connect(DataBasePath)
        connection.row_factory = sqlite3.Row
        connection.execute('INSERT INTO Posts (titolo, info) VALUES (?, ?)', (tit, info))
        connection.commit()
        connection.close()
        return redirect('/')
    return render_template('create.html')


@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(StaticsPath, filename))
        return 'file uploaded successfully'


@app.route('/StaticFiles/<path:filename>', methods=['GET', ])
def downloadfile(filename):
    return send_from_directory(StaticsPath, filename)


if __name__ == "__main__":
    app.run()

