from flask import Flask, render_template, request # requestを追加
import pandas as pd # pandasをインポート
import io # メモリ上でファイルを扱うための道具

app = Flask(__name__)

@app.route('/')
def index():
    # templatesフォルダの中のindex.htmlを表示させる
    return render_template('index.html')

# アップロードされたファイルを受け取るための「住所」を作る
@app.route('/upload', methods=['POST'])
def upload_file():
    # 画面から送られてきたファイルを取得
    file = request.files.get('file')

    if file and file.filename.endswith('.csv'):
        # 1. アップロードされたCSVを読み込む
        # (ファイルの実体ではなく「データの中身」を直接読み込んでいます)
        df = pd.read_csv(file)

        # 2. 前回の加工ロジックを実行!
        # 名前を大文字にする (カラム名が 'name' の場合)
        if 'name' in df.columns:
            df['name'] = df['name'].str.upper()

        # 年齢を+1する (カラム名が 'age' の場合)
        if 'age' in df.columns:
            # errors='coerce' は、もし数字じゃない文字が入っていてもエラーにせず無視する
            df['age'] = pd.to_numeric(df['age'], errors='coerce') + 1

        # 3. 加工した結果を「HTMLの表」に変換する
        # index=False は、左端の行番号を表示しない設定です
        data_html = df.to_html(classes='table table-striped', index=False)

        return f"""
            <h1>加工完了!</h1>
            <div style="margin-bottom: 20px;">{data_html}</div>
            <a href="/">戻る</a>
        """
    
    return "CSVファイルをアップロードしてください"

if __name__ == "__main__":
    app.run(debug=True)