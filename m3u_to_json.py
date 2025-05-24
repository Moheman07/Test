import json
import os

def create_channels_json(output_file):
    channels = [
        {
            "name": "القناة الأولى",
            "url": "http://example.com/channel1",
            "logo": "logos/channel1.png",
            "guide": "guides/channel1.pdf"
        },
        {
            "name": "القناة الثانية",
            "url": "http://example.com/channel2",
            "logo": "logos/channel2.png",
            "guide": "guides/channel2.pdf"
        }
        # يمكنك إضافة المزيد من القنوات هنا
    ]
    
    # إنشاء مجلدات إذا لم تكن موجودة
    os.makedirs("logos", exist_ok=True)
    os.makedirs("guides", exist_ok=True)
    
    # حفظ البيانات في ملف JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(channels, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    create_channels_json('channels.json')
