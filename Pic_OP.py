
from PIL import Image
from PIL.ExifTags import TAGS

def get_photo_taken_time(photo_path):
    # 打开图片
    try:
        img = Image.open(photo_path)
        # 获取图片的EXIF信息
        exif_data = img._getexif()
        # 如果图片包含EXIF信息
        if exif_data:
            # 遍历EXIF信息，找到拍摄时间
            for tag_id in exif_data:
                # 将EXIF标签ID转换为人类可读的名称
                tag = TAGS.get(tag_id, tag_id)
                # print(tag)
                if tag == 'DateTimeOriginal':
                    # 打印拍摄时间
                    print('原始时间:', exif_data[tag_id])
                    return str(exif_data[tag_id]).strip()
        # 如果没有找到拍摄时间，返回None
        return None
    except:
        return None

# 替换为你的照片路径
#photo_path = '/Users/KK/Desktop/KK/江家圈子/pic/3H4A3357.jpg'
#get_photo_taken_time(photo_path)