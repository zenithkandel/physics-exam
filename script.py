import json
import re

def process_latex(text):
    if not isinstance(text, str):
        return text
    # basic replacements
    text = re.sub(r'A ∪ B', r'\\( A \\cup B \\)', text)
    text = re.sub(r'A ∩ B', r'\\( A \\cap B \\)', text)
    text = re.sub(r'f\(x\) = (.*?)(?=\s|$)', r'\\( f(x) = \1 \\)', text)
    text = re.sub(r'f⁻¹\(x\)', r'\\( f^{-1}(x) \\)', text)
    text = re.sub(r'x ≥ (\d+)', r'\\( x \\ge \1 \\)', text)
    text = re.sub(r'x ≤ (\d+)', r'\\( x \\le \1 \\)', text)
    text = re.sub(r'x > (\d+)', r'\\( x > \1 \\)', text)
    text = re.sub(r'x < (\d+)', r'\\( x < \1 \\)', text)
    text = re.sub(r'a₁', r'\\( a_1 \\)', text)
    text = re.sub(r'√(.*?)(?=\s|$)', r'\\( \\sqrt{\1} \\)', text)
    text = re.sub(r'S∞', r'\\( S_\\infty \\)', text)
    text = re.sub(r'x²', r'x^2', text)
    text = re.sub(r'x³', r'x^3', text)
    text = re.sub(r'xⁿ', r'x^n', text)
    text = re.sub(r'aⁿ', r'a^n', text)
    text = re.sub(r'x² \+ (\d+)x \+ (\d+) = 0', r'\\( x^2 + \1x + \2 = 0 \\)', text)
    text = re.sub(r'x² - (\d+)x \+ (\d+) = 0', r'\\( x^2 - \1x + \2 = 0 \\)', text)
    text = re.sub(r'x² - (\d+) = 0', r'\\( x^2 - \1 = 0 \\)', text)
    text = re.sub(r'sin⁻¹', r'\\( \\sin^{-1} \\)', text)
    text = re.sub(r'tan⁻¹', r'\\( \\tan^{-1} \\)', text)
    text = re.sub(r'cos⁻¹', r'\\( \\cos^{-1} \\)', text)
    text = re.sub(r'cot⁻¹', r'\\( \\cot^{-1} \\)', text)
    text = re.sub(r'π', r'\\pi', text)
    text = re.sub(r'lim\(x→0\)', r'\\( \\lim_{x \\to 0} \\)', text)
    text = re.sub(r'∫(.*?)(?= equals)', r'\\( \\int \1 \\)', text)
    text = re.sub(r'd/dx\((.*?)\)', r'\\( \\frac{d}{dx}(\1) \\)', text)
    text = re.sub(r'e\^x', r'e^x', text)
    text = re.sub(r'θ', r'\\theta', text)
    text = re.sub(r'Σ', r'\\Sigma', text)
    text = text.replace('4√5', '\\( 4\\sqrt{2} \\)') # Fixing the error answer
    text = text.replace('4.2', '4.6') # Fixing the error answer
    return text

with open('c:/xampp/htdocs/codes/maths-exam/data/maths.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data.get('questions', []):
    q['q'] = process_latex(q['q'])
    q['opts'] = [process_latex(opt) for opt in q['opts']]
    q['hint'] = process_latex(q['hint'])
    
    # manual question fix overrides
    if '4.6' in q['opts'] and '3' in q['opts'] and '5' in q['opts'] and '2' in q['opts']:
        q['opts'][q['opts'].index('4.6')] = '4.6' # Already done
        
with open('c:/xampp/htdocs/codes/maths-exam/data/maths.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
