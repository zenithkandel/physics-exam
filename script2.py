import json
import re

def process_latex(text):
    if not isinstance(text, str):
        return text
    text = re.sub(r'1/\(ax \+ b\)', r'\\( \\frac{1}{ax+b} \\)', text)
    text = re.sub(r'a sin bx and a cos bx', r'\\( a \\sin bx \\) and \\( a \\cos bx \\)', text)
    text = re.sub(r'eˣ', r'\\( e^x \\)', text)
    text = re.sub(r'ln x', r'\\( \\ln x \\)', text)
    text = re.sub(r'x \+ y = 0', r'\\( x + y = 0 \\)', text)
    text = re.sub(r'second degree equation in x and y', r'second degree equation in \\(x\\) and \\(y\\)', text)
    text = re.sub(r'second degree in x and y', r'second degree in \\(x\\) and \\(y\\)', text)
    return text

with open('c:/xampp/htdocs/codes/maths-exam/data/maths-syllabus.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

if 'units' in data:
    for u in data['units']:
        if 'topics' in u:
            u['topics'] = [process_latex(t) for t in u['topics']]

with open('c:/xampp/htdocs/codes/maths-exam/data/maths-syllabus.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
