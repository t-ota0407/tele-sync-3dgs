from google.cloud import storage
import os
import subprocess

def download_images_from_gcs(session_id):
    # サービスアカウントキーのパスを指定
    credentials_path = "tele-sync-455613-a5fafa094e4f.json"
    client = storage.Client.from_service_account_json(credentials_path)
    
    # バケット名を指定
    bucket_name = "telesync-20250402"
    bucket = client.bucket(bucket_name)
    
    # ダウンロード先のディレクトリを作成
    download_dir = f"data/{session_id}/input"
    os.makedirs(download_dir, exist_ok=True)
    
    # 指定されたsession_idのフォルダ内のファイルを取得
    blobs = bucket.list_blobs(prefix=f"{session_id}/")
    
    # 各ファイルをダウンロード
    for blob in blobs:
        if not blob.name.endswith('/'):  # フォルダ自体はスキップ
            # ファイル名を取得
            file_name = os.path.basename(blob.name)
            # ダウンロード先のパス
            download_path = os.path.join(download_dir, file_name)
            # ファイルをダウンロード
            blob.download_to_filename(download_path)
            print(f"ダウンロード完了: {file_name}")

def main():
    session_id = input("sessionIdを入力してください: ")
    download_images_from_gcs(session_id)
    print("すべてのファイルのダウンロードが完了しました。")

    subprocess.run(
        ['python', 'convert.py', '--colmap_executable',
         rf'"D:\Others\gaussian-splatting\COLMAP-3.9.1-windows-cuda\COLMAP.bat"',
         '-s', f'D:\Others\gaussian-splatting\data\{session_id}'])
    
    subprocess.run(
        ['python', 'train.py', '-s',
         f'D:\Others\gaussian-splatting\data\{session_id}'])

if __name__ == "__main__":
    main()
