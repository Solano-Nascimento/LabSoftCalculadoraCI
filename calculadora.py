import re

pattern = r'^\s*(-?\d+(?:\.\d+)?)\s*([+\-/*^])\s*(-?\d+(?:\.\d+)?)\s*$'

def soma(a: float | int, b: float | int) -> float | int:
    return a + b

def subtracao(a: float | int, b: float | int) -> float | int:
    return a - b

def multiplicacao(a: float | int, b: float | int) -> float | int:
    return a * b

def divisao(a: float | int, b: float | int) -> float | int:
    if b == 0:
        return None
    return a / b

def potenciacao(a: float | int, b: float | int) -> float | int:
    if a == 0 and b == 0:
        return None
    return a ** b

def parse_num(s):
    if '.' in s or 'e' in s.lower():
        return float(s)
    else:
        return int(s)

def calcular(expr):
    match = re.match(pattern, expr)
    if not match:
        return None
    
    a_str, op, b_str = match.groups()
    a = parse_num(a_str)
    b = parse_num(b_str)

    try:
        if op == '+':
            return soma(a, b)
        elif op == '-':
            return subtracao(a, b)
        elif op == '*':
            return multiplicacao(a, b)
        elif op == '/':
            return divisao(a, b)
        elif op == '^':
            return potenciacao(a, b)
    except Exception:
        return None    
