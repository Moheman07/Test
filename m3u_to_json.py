import json

# دالة لتحليل ملف M3U
def parse_m3u(file_path):
    channels = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('#EXTINF'):
                parts = line.split(',')
                name = parts[1].strip()
                link = next(file).strip()
                logo = ""  # أضف منطق لاستخراج الشعار إذا كان متاحًا
                channels.append({"name": name, "link": link, "logo": logo})
    return channels

# تحويل القنوات إلى JSON
def convert_to_json(channels):
    return json.dumps(channels, indent=4)

# استخدام المثال
m3u_file_path = 'path/to/your/file.m3u'
channels = parse_m3u(m3u_file_path)
json_data = convert_to_json(channels)
print(json_data)
