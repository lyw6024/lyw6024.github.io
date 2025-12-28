import os
import requests

# 入力ファイル
INPUT_FILE = "tile-urls.txt"   # ここをあなたのファイル名に変更
# 画像保存先ディレクトリ
OUTPUT_DIR = "images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

BASE_URL = "https://www.sogensha.jp/tetsudo/rdweb2025-contents/map/{}/{}/{}"

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            # 改行を除去
            line = line.strip()
            if not line:
                continue  # 空行はスキップ

            # ここで1行を分割
            # 例: 「aaa bbb ccc ddd」のようにスペース区切りなら split()
            #    「aaa,bbb,ccc,ddd」のようにカンマ区切りなら split(",")
            parts = line.split()  # 必要なら line.split(",") に変更

            if len(parts) < 3:
                print(f"{i}行目: 列数が足りません -> {line}")
                continue

            v1, v2, v3 = parts[0], parts[1], parts[2]

            # URL作成
            url = BASE_URL.format(v1, v2, v3)

            # 保存ファイル名（例: 3_4.png をそのまま使う）
            filename = f"{v3}"
            os.makedirs(OUTPUT_DIR+"/"+v1+"/"+v2, exist_ok=True)
            out_path = os.path.join(OUTPUT_DIR+"/"+v1+"/"+v2, filename)

            print(f"ダウンロード: {url} -> {out_path}")

            try:
                resp = requests.get(url, timeout=10)
                resp.raise_for_status()  # エラー時に例外

                with open(out_path, "wb") as img_file:
                    img_file.write(resp.content)
            except Exception as e:
                print(f"  ダウンロード失敗: {e}")

if __name__ == "__main__":
    main()
