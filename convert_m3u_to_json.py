import re
import json
import logging

# إعداد التسجيل لتتبع الأخطاء
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

channels = []
current_group = None

try:
    with open('channels.m3u', 'r', encoding='utf-8') as file:
        line_number = 0
        for line in file:
            line_number += 1
            line = line.strip()
            if not line or line.startswith('#EXTM3U'):
                continue
            elif line.startswith('#EXTINF'):
                match = re.search(r'tvg-logo="([^"]*)".*?,(.*)', line)
                if match:
                    logo, title = match.groups()
                    # قراءة السطر التالي (الرابط) إذا كان موجودًا
                    try:
                        next_line = next(file, '').strip()
                        line_number += 1
                        url = next_line if next_line else ''
                    except StopIteration:
                        url = ''  # نهاية الملف، لا رابط
                    channel = {
                        'title': title.strip(),
                        'logo': logo.strip() or 'https://via.placeholder.com/100',
                        'url': url.strip(),
                        'group': current_group
                    }
                    if url == '0.0.0.0':
                        current_group = title.strip()
                        logging.info(f"Group detected: {current_group}")
                    channels.append(channel)
                    logging.info(f"Processed channel: {title} at line {line_number}")
                else:
                    logging.warning(f"Invalid #EXTINF format at line {line_number}: {line}")
            else:
                logging.warning(f"Skipping unexpected line {line_number}: {line}")
except FileNotFoundError:
    logging.error("File channels.m3u not found")
    raise
except Exception as e:
    logging.error(f"Error processing channels.m3u: {str(e)}")
    raise

# حفظ جميع القنوات (بدون تصفية)
try:
    with open('channels.json', 'w', encoding='utf-8') as file:
        json.dump(channels, file, ensure_ascii=False, indent=2)
    logging.info("Successfully created channels.json")
except Exception as e:
    logging.error(f"Error writing channels.json: {str(e)}")
    raise
