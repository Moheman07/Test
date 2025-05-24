import json

def m3u_to_json(links_file, json_file):
    # قراءة الروابط من ملف منفصل
    with open(links_file, 'r') as f:
        links = [line.strip() for line in f if line.strip()]
    
    # إنشاء قناة لكل رابط
    channels = [{'name': f'Channel {i+1}', 'url': url} 
               for i, url in enumerate(links)]
    
    # حفظ النتيجة في ملف JSON
    with open(json_file, 'w') as f:
        json.dump(channels, f, indent=4)

if __name__ == '__main__':
    m3u_to_json('links.txt', 'output.json')
