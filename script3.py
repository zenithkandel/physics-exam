import json
import re

def process_fractions(text):
    if not isinstance(text, str):
        return text
    
    # fractions
    text = re.sub(r'(\d+)/(\d+)', r'\\(\frac{\1}{\2}\\)', text)
    text = re.sub(r'\((x-3)\)/2', r'\\(\frac{x-3}{2}\\)', text)
    text = re.sub(r'x/2', r'\\(\frac{x}{2}\\)', text)
    text = re.sub(r'\((x\+3)\)/2', r'\\(\frac{x+3}{2}\\)', text)
    text = re.sub(r'Sn = n/2\[2a \+ \(n-1\)d\]', r'\\(S_n = \frac{n}{2}[2a + (n-1)d]\\)', text)
    text = re.sub(r'n/2', r'\\frac{n}{2}', text)
    
    # specific limits, integrals
    text = re.sub(r'\(\\*frac\{d\}\{dx\}\(x\^n\)\) = nx\^\{n-1\}', r'\\(\\frac{d}{dx}(x^n) = nx^{n-1}\\)', text)
    text = re.sub(r'\(\\(.*?)\\)', r'\\(\1\\)', text) # cleanup nested
    text = re.sub(r'\\(\\(.*?)\\)\\)', r'\\(\1\\)', text) # cleanup nested
    
    # We will let KaTeX handle inline math
    # Just wrap expressions in \( ... \) if they represent math.
    
    return text

with open('c:/xampp/htdocs/codes/maths-exam/data/maths.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data.get('questions', []):
    q['q'] = process_fractions(q['q'])
    q['opts'] = [process_fractions(opt) for opt in q['opts']]
    q['hint'] = process_fractions(q['hint'])
        
with open('c:/xampp/htdocs/codes/maths-exam/data/maths.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
