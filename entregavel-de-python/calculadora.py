def somar(a, b):
    """Retorna a soma de a e b."""
    return a + b
 
 
def subtrair(a, b):
    """Retorna a - b."""
    return a - b
 
 
def multiplicar(a, b):
    """Retorna a * b."""
    return a * b
 
 
def dividir(a, b):
    """Retorna a / b, ou None se b for zero."""
    if b == 0:
        print("Erro: divisão por zero.")
        return None
    return a / b