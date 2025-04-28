from PIL import Image
import os

def convert_png_to_jpg(directory):
    # ディレクトリ内のすべてのファイルを取得
    for filename in os.listdir(directory):
        if filename.lower().endswith(".png"):  # PNGファイルのみ処理
            png_path = os.path.join(directory, filename)
            jpg_path = os.path.join(directory, os.path.splitext(filename)[0] + ".jpg")
            
            # PNGを開いてJPGに変換
            with Image.open(png_path) as img:
                rgb_img = img.convert("RGB")  # JPGはRGBモードが必要
                rgb_img.save(jpg_path, "JPEG", quality=95)  # 高品質で保存
                
            print(f"Converted: {filename} -> {os.path.basename(jpg_path)}")

# 使用例: 変換するディレクトリを指定
directory_path = "./data/bld1/images"
convert_png_to_jpg(directory_path)
