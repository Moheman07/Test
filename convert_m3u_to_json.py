import re
import json

def parse_m3u(file_path):
    channels = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if line.startswith('#EXTINF'):
                # استخراج اسم القناة ورابط اللوغو
                match = re.search(r'tvg-logo="([^"]+)"\s*,(.+)', line)
                if match:
                    logo = match.group(1)
                    name = match.group(2).strip()
                    # التحقق من وجود الرابط في السطر التالي
                    if i + 1 < len(lines) and not lines[i + 1].startswith('#'):
                        url = lines[i + 1].strip()
                        channels.append({
                            "name": name,
                            "url": url,
                            "logo": logo
                        })
    return channels

def save_to_json(channels, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(channels, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    channels = parse_m3u('channels.m3u')
    save_to_json(channels, 'channels.json')
