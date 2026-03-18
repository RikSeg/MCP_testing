from operator import mul

from fastmcp import FastMCP
from typing import Union

mcp = FastMCP(
    name="CalculationsMcpServer",
    instructions= "Este é um servidor MCP que oferece ferramentas para cálculos matemáticos. As ferramentas disponíveis incluem adição, subtração, multiplicação, divisão, potência e raiz quadrada. Use essas ferramentas para realizar cálculos conforme necessário."
    )

@mcp.tool(
        name="Adicionar",
        description="Adicionar dois números"
)
def add(numero1: float, numero2: float) -> float:
    """
    Adiciona dois números.

    Args:
        numero1 (float): primeiro número
        numero2 (float): segundo número
    """
    sum = numero1 + numero2
    return sum

@mcp.tool(
        name="Subtrair",
        description="Subtrair dois números"
)
def subtract(numero1: float, numero2: float) -> float:
    """Subtrai dois números.
    
    Args:
        numero1 (float): primeiro número
        numero2 (float): segundo número

    Returns:
        sub (float): número resultante da subtração
    """
    sub = numero1 - numero2
    return sub

@mcp.tool(
        name="Multiplicar",
        description="Multiplicar dois números"
)
def multiply(numero1: float, numero2: float) -> float:
    """Multiplica dois números.

    Args:
        numero1 (float): primeiro numero
        numero2 (float): segundo numero

    Returns:
        nul (float): numero resultante da multiplicação
    """
    mul = numero1 * numero2
    return mul

@mcp.tool(
        name="Dividir",
        description="Dividir dois números"
)
def divide(numero1: float, numero2: float) -> float:
    """Divide dois números.

    Args:
        numero1 (float): número dividido
        numero2 (float): número divisor

    Raises:
        ZeroDivisionError: quando o divisor é zero, o que não é permitido

    Returns:
        float: número resultante da divisão
    """
    if numero2 == 0:
        raise ZeroDivisionError("Divisão por zero não permitida")
    div = numero1 / numero2
    return div

@mcp.tool(
        name="Potencia",
        description="Calcular a potência de um número"
)
def power(numero: float, potencia: float) -> Union[float, float]:
    """Calcula Potência de um número pelo outro

    Args:
        numero (float): Número base da potência
        potencia (float): Número expoente da potência

    Raises:
        ValueError: quando a base é zero e o expoente é menor ou igual a zero, o que não é definido

    Returns:
        float: número resultante da potência
    """
    if numero == 0 and potencia <= 0:
        raise ValueError("0 elevado a zero ou a um número negativo não é definido")
    pot = numero ** potencia
    return pot

@mcp.tool(
        name="RaizQuadrada",
        description="Calcular a raiz quadrada de um número"
)
def sqrt(numero: float) -> float:
    """Raiz quadrada de um número

    Args:
        numero (float): Numero do qual se deseja calcular a raiz quadrada

    Raises:
        ValueError: quando o número é negativo, pois não é possível calcular a raiz quadrada de um número negativo

    Returns:
        float: número resultante da raiz quadrada
    """
    if numero < 0:
        raise ValueError("Não é possível calcular raiz quadrada de número negativo")
    sqrt = numero ** 0.5
    return sqrt

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000)