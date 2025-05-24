import re
import json

channels = []
current_group = None

with open('channels.m3u', 'r', encoding='utf-8') as file:
    lines = file.readlines()  # قراءة كل الأسطر مقدمًا
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('#EXTM3U'):
            i += 1
            continue
        elif line.startswith('#EXTINF'):
            match = re.search(r'tvg-logo="([^"]*)".*?,(.*)', line)
            if match:
                logo, title = match.groups()
                # التحقق من وجود سطر تالي للرابط
                url = ''
                if i + 1 < len(lines):
                    url = lines[i + 1].strip()
                    i += 2  # تخطي سطر الرابط
                else:
                    i += 1  # نهاية الملف، لا رابط
                channel = {
                    'title': title.strip(),
                    'logo': logo.strip() or 'https://via.placeholder.com/100',
                    'url': url.strip(),
                    'group': current_group
                }
                if url == '0.0.0.0':
                    current_group = title.strip()
                channels.append(channel)
        else:
            i += 1

# حفظ جميع القنوات (بدون تصفية)
with open('channels.json', 'w', encoding='utf-8') as file:
    json.dump(channels, file, ensure_ascii=False, indent=2)
