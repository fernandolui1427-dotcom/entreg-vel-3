import calculadora
import utilidades
 
print(calculadora.somar(8, 3))
print(calculadora.subtrair(8, 3))
print(calculadora.multiplicar(8, 3))
print(calculadora.dividir(8, 4))
print(calculadora.dividir(8, 0))
 
print(utilidades.celsius_para_fahrenheit(25))
print(utilidades.validar_senha("senha1234"))
print(utilidades.calcular_caixa(10, 5.5, 2))
print(utilidades.montar_ficha_aluno(nome="Ana", idade=20))
 
frutas = ["maçã", "banana"]
novas_frutas = utilidades.adicionar_item_seguro(frutas, "uva")
print(frutas)
print(novas_frutas)