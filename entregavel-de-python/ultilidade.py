def celsius_para_fahrenheit(celsius):
    """Converte Celsius para Fahrenheit."""
    return celsius * 9 / 5 + 32
 
 
def validar_senha(senha):
    """Retorna True se a senha tiver 8+ caracteres e pelo menos um número."""
    tem_numero = any(letra.isdigit() for letra in senha)
    return len(senha) >= 8 and tem_numero
 
 
def calcular_caixa(*precos):
    """Retorna a soma de todos os preços recebidos."""
    return sum(precos)
 
 
def montar_ficha_aluno(**dados):
    """Retorna um texto com os dados do aluno."""
    texto = ""
    for campo, valor in dados.items():
        texto += f"{campo}: {valor}\n"
    return texto
 
 
def adicionar_item_seguro(lista, item):
    """Retorna uma cópia da lista com o item, sem alterar a original."""
    copia = lista.copy()
    copia.append(item)
    return copia