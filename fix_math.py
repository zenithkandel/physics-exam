import json
import re

with open('data/maths.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def fix_superscripts(text):
    if not isinstance(text, str): return text
        
    def repl(match):
        s = match.group(0)
        normal = ""
        for c in s:
            if c == '⁰': normal += '0'
            elif c == '¹': normal += '1'
            elif c == '²': normal += '2'
            elif c == '³': normal += '3'
            elif c == '⁴': normal += '4'
            elif c == '⁵': normal += '5'
            elif c == '⁶': normal += '6'
            elif c == '⁷': normal += '7'
            elif c == '⁸': normal += '8'
            elif c == '⁹': normal += '9'
            elif c == '⁺': normal += '+'
            elif c == '⁻': normal += '-'
            elif c == 'ⁿ': normal += 'n'
            else: normal += c
        return f"^{{{normal}}}"
        
    pattern = re.compile(r'[⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻ⁿ]+')
    text = pattern.sub(repl, text)
    
    text = text.replace('½', '\\frac{1}{2}')
    text = text.replace('¼', '\\frac{1}{4}')
    text = text.replace('¾', '\\frac{3}{4}')
    text = text.replace('∫', '\\int ')
    text = text.replace('∞', '\\infty ')
    text = text.replace('±', '\\pm ')
    text = text.replace('θ', '\\theta ')
    text = text.replace('π', '\\pi ')
    text = text.replace('≤', '\\le ')
    text = text.replace('≥', '\\ge ')
    text = text.replace('≠', '\\neq ')
    text = text.replace('≈', '\\approx ')
    text = text.replace('Δ', '\\Delta ')
    text = text.replace('∑', '\\sum ')
    text = text.replace('√', '\\sqrt ')
    text = text.replace('×', '\\times ')
    text = text.replace('÷', '\\div ')
    text = text.replace('→', '\\to ')
    return text

def wrap_math(text):
    if not isinstance(text, str): return text
    if '\\(' in text or '\\[' in text: return text
    if '<' in text and '>' in text: return text
    if "Does not exist" in text or "None of" in text: return text
    
    if re.fullmatch(r'[A-Za-z\s]+', text): return text
    
    return f"\\( {text} \\)"

for q in data.get('questions', []):
    q['q'] = fix_superscripts(q.get('q', ''))
    q['hint'] = fix_superscripts(q.get('hint', ''))
    
    new_opts = []
    for opt in q.get('opts', []):
        o = fix_superscripts(opt)
        o = wrap_math(o)
        new_opts.append(o)
    q['opts'] = new_opts

with open('data/maths.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("done")
