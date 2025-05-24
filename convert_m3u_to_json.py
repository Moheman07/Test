import re
import json

channels = []
current_group = None

with open('channels.m3u', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line.startswith('#EXTM3U'):
            continue
        elif line.startswith('#EXTINF'):
            match = re.search(r'tvg-logo="([^"]*)".*?,(.*)', line)
            if match:
                logo, title = match.groups()
                url = next(file).strip() if not file._io.closed else ''
                channel = {
                    'title': title.strip(),
                    'logo': logo.strip() or 'https://via.placeholder.com/100',
                    'url': url.strip(),
                    'group': current_group
                }
                if url == '0.0.0.0':
                    current_group = title.strip()
                channels.append(channel)

# حفظ جميع القنوات (بدون تصفية)
with open('channels.json', 'w', encoding='utf-8') as file:
    json.dump(channels, file, ensure_ascii=False, indent=2)
