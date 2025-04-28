from PIL import Image
import os

# 変換対象のフォルダパスを指定
folder_path = r'D:\Others\gaussian-splatting\data\bmxrmpbs_3_800_600\input'

# 出力フォルダ（元と同じならそのまま上書きされます）
output_folder = folder_path  # または r'C:\path\to\output'

# リサイズ後のサイズ
target_size = (800, 600)

# 処理実行
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        image_path = os.path.join(folder_path, filename)
        with Image.open(image_path) as img:
            resized_img = img.resize(target_size, Image.LANCZOS)
            save_path = os.path.join(output_folder, filename)
            resized_img.save(save_path)
            print(f"Resized: {filename}")
