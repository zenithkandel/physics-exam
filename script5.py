import json
import re

with open('data/maths.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Fix nested \(\) and also expand cheatsheet
def fix_nested(text):
    if not isinstance(text, str): return text
    
    # We remove inner \( and \) 
    # Actually, a simpler way is to just strip all \(\) and re-wrap the whole thing if it's math
    # Or just replace nested ones
    while "\\( \\(" in text or "\\(  \\(" in text:
        text = text.replace("\\( \\(", "\\(")
        text = text.replace("\\(  \\(", "\\(")
    while "\\) \\)" in text or "\\)  \\)" in text:
        text = text.replace("\\) \\)", "\\)")
        text = text.replace("\\)  \\)", "\\)")
    
    text = text.replace("\\( f(x) = \\( \\sqrt{(x-2)} \\) \\)", "\\( f(x) = \\sqrt{(x-2)} \\)")
    return text

for q in data.get('questions', []):
    q['q'] = fix_nested(q['q'])
    q['opts'] = [fix_nested(opt) for opt in q['opts']]
    q['hint'] = fix_nested(q['hint'])

# Expand cheatsheet!
if 'cheatsheet' in data:
    data['cheatsheet'].extend([
        {
          "title": "Calculus: Limits & Derivatives",
          "icon": "calculator",
          "items": [
            "<strong>Limits:</strong> \\( \\lim_{x \\to 0} \\frac{\\sin x}{x} = 1 \\)",
            "<strong>Limits:</strong> \\( \\lim_{x \\to 0} \\frac{e^x - 1}{x} = 1 \\)",
            "<strong>Chain Rule:</strong> \\( \\frac{d}{dx}[f(g(x))] = f'(g(x))g'(x) \\)",
            "<strong>Product Rule:</strong> \\( \\frac{d}{dx}(uv) = u\\frac{dv}{dx} + v\\frac{du}{dx} \\)",
            "<strong>Quotient Rule:</strong> \\( \\frac{d}{dx}(\\frac{u}{v}) = \\frac{v\\frac{du}{dx} - u\\frac{dv}{dx}}{v^2} \\)"
          ]
        },
        {
          "title": "Analytic Geometry (Straight Lines)",
          "icon": "chart-line",
          "items": [
            "<strong>Distance between points:</strong> \\( d = \\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2} \\)",
            "<strong>Mid-point formula:</strong> \\( (\\frac{x_1+x_2}{2}, \\frac{y_1+y_2}{2}) \\)",
            "<strong>Slope of line:</strong> \\( m = \\frac{y_2-y_1}{x_2-x_1} = -\\frac{A}{B} \\)",
            "<strong>Angle between lines:</strong> \\( \\tan \\theta = \\pm \\frac{m_1-m_2}{1+m_1 m_2} \\)",
            "<strong>Perpendicular Distance:</strong> \\( d = \\frac{|Ax_1+By_1+C|}{\\sqrt{A^2+B^2}} \\)"
          ]
        },
        {
          "title": "Vectors & 3D Geometry",
          "icon": "arrow-up-right",
          "items": [
            "<strong>Dot Product:</strong> \\( \\vec{a} \\cdot \\vec{b} = |\\vec{a}||\\vec{b}|\\cos \\theta \\)",
            "<strong>Cross Product:</strong> \\( |\\vec{a} \\times \\vec{b}| = |\\vec{a}||\\vec{b}|\\sin \\theta \\)",
            "<strong>Direction Cosines:</strong> \\( l = \\cos \\alpha, m = \\cos \\beta, n = \\cos \\gamma \\)",
            "<strong>Relation of DC:</strong> \\( l^2 + m^2 + n^2 = 1 \\)",
            "<strong>Collinear vectors condition:</strong> \\( \\vec{a} = k\\vec{b} \\)"
          ]
        }
    ])

with open('data/maths.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
