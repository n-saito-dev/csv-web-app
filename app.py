from flask import Flask, render_template, request # requestを追加
import pandas as pd # pandasをインポート
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# データベースの保存先(同じフォルダ内の csv_history.db というファイルに保存する)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///csv_history.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# データベースの設計図(履歴を保存するテーブル)
class UploadHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False) # ファイル名
    upload_at = db.Column(db.DateTime, default=datetime.now) # アップロード日時

# データベースファイルを自動作成する魔法の命令
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename.endswith('.csv'):
            # 1. データベースに履歴を保存
            new_history = UploadHistory(filename=file.filename)
            db.session.add(new_history)
            db.session.commit()

            # 2. CSVを読み込んで表示
            df = pd.read_csv(file)
            data = df.to_html(classes='table table-striped', index=False, border=1)

    # --- ここを追加:データベースからすべての履歴を取得する ---
    histories = UploadHistory.query.order_by(UploadHistory.upload_at.desc()).all()
    # -------------------------------------------------

    # histories=histories を追加してHTMLに送る
    return render_template('index.html', data=data, histories=histories)

if __name__ == "__main__":
    app.run(debug=True)