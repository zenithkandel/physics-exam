import json
import re

def to_katex(text):
    if not isinstance(text, str):
        return text
        
    text = re.sub(r'1/\(ax \+ b\)', r'\\frac{1}{ax+b}', text)
    text = re.sub(r'S∞ = a/\(1-r\)', r'S_\\infty = \\frac{a}{1-r}', text)
    text = re.sub(r'Sn = a\(rⁿ-1\)/\(r-1\)', r'S_n = \\frac{a(r^n-1)}{r-1}', text)
    text = re.sub(r'Sn = n/2\[2a \+ \(n-1\)d\]', r'S_n = \\frac{n}{2}[2a + (n-1)d]', text)
    text = re.sub(r'a/\(1-1/2\)', r'\\frac{a}{1 - \\frac{1}{2}}', text)
    text = re.sub(r'64/10', r'\\frac{64}{10}', text)
    text = re.sub(r'1/0\.5', r'\\frac{1}{0.5}', text)
    text = re.sub(r'4/1', r'\\frac{4}{1}', text)
    text = re.sub(r'-b/a', r'-\\frac{b}{a}', text)
    text = re.sub(r'c/a', r'\\frac{c}{a}', text)
    
    text = re.sub(r'\((x-3)\)/2', r'\\frac{x-3}{2}', text)
    text = re.sub(r'\((x\+3)\)/2', r'\\frac{x+3}{2}', text)
    text = re.sub(r'x/2', r'\\frac{x}{2}', text)
    text = re.sub(r'1/2', r'\\frac{1}{2}', text)
    text = re.sub(r'1/4', r'\\frac{1}{4}', text)
    
    text = re.sub(r'π/6', r'\\frac{\\pi}{6}', text)
    text = re.sub(r'π/4', r'\\frac{\\pi}{4}', text)
    text = re.sub(r'π/3', r'\\frac{\\pi}{3}', text)
    text = re.sub(r'π/2', r'\\frac{\\pi}{2}', text)
    text = re.sub(r'2nπ', r'2n\\pi', text)
    text = re.sub(r'nπ', r'n\\pi', text)
    
    text = re.sub(r'2/7', r'\\frac{2}{7}', text)
    text = re.sub(r'3/7', r'\\frac{3}{7}', text)
    text = re.sub(r'6/7', r'\\frac{6}{7}', text)
    text = re.sub(r'1/7', r'\\frac{1}{7}', text)
    text = re.sub(r'2/13', r'\\frac{2}{13}', text)
    text = re.sub(r'3/13', r'\\frac{3}{13}', text)
    text = re.sub(r'6/13', r'\\frac{6}{13}', text)
    text = re.sub(r'2/5', r'\\frac{2}{5}', text)
    text = re.sub(r'3/5', r'\\frac{3}{5}', text)
    text = re.sub(r'6/5', r'\\frac{6}{5}', text)
    
    text = re.sub(r'40/5', r'\\frac{40}{5}', text)
    text = re.sub(r'160/5', r'\\frac{160}{5}', text)
    text = re.sub(r'0\.1/0\.3', r'\\frac{0.1}{0.3}', text)
    text = re.sub(r'1/3', r'\\frac{1}{3}', text)
    text = re.sub(r'1/√2', r'\\frac{1}{\\sqrt{2}}', text)
    text = re.sub(r'√3/2', r'\\frac{\\sqrt{3}}{2}', text)
    text = re.sub(r'1/√3', r'\\frac{1}{\\sqrt{3}}', text)
    
    text = re.sub(r'\(e\^x - 1\)/x', r'\\frac{e^x - 1}{x}', text)
    text = re.sub(r'\(sin x\)/x', r'\\frac{\\sin x}{x}', text)
    text = re.sub(r'x³/3', r'\\frac{x^3}{3}', text)
    
    text = re.sub(r'1/x', r'\\frac{1}{x}', text)
    text = re.sub(r'1/\(x ln 10\)', r'\\frac{1}{x \\ln 10}', text)
    text = re.sub(r'xⁿ⁺¹/\(n\+1\)', r'\\frac{x^{n+1}}{n+1}', text)
    
    text = re.sub(r'P\(A/B\)', r'P(A|B)', text)
    
    text = re.sub(r'd/dx', r'\\frac{d}{dx}', text)
    
    return text

with open('c:/xampp/htdocs/codes/maths-exam/data/maths.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data.get('questions', []):
    q['opts'] = [to_katex(o) if '\\frac' not in o else o for o in q['opts']]
    q['q'] = to_katex(q['q'])
    q['hint'] = to_katex(q['hint'])
    # wrap in math if has \\frac but no \\(
    q['opts'] = [f'\\( {o} \\)' if '\\frac' in o and '\\(' not in o else o for o in q['opts']]

with open('c:/xampp/htdocs/codes/maths-exam/data/maths.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
