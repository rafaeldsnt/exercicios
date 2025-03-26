import sys


def calculadora(num1,num2,op):
    match op:
        case "+": return (int(num1) + int(num2))
        case "-": return int(num1) - int(num2)
        case "*": return int(num1) * int(num2)
        case "/": return int(num1) / int(num2)
        case default: return "Operação desconhecida"

def test_calculadora(argumentos):
      resultado = calculadora(argumentos[0],argumentos[1],argumentos[2])
      print(f"A operação escolhida foi {argumentos[2]} é o resultado é {resultado}")


def CountWordsText(argumentos):
    print(argumentos)
    countWords = len(argumentos[0].split())
    print(f"O texto possui {countWords} palavras")


     

if __name__ == "__main__":
    #test_calculadora(sys.argv[1:])
    CountWordsText(sys.argv[1:])



