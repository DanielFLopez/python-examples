def decorator(f):
    def new_function(a, b):
        if a % 2 == 0:
          print("El valor de a, es par!")
        else:
          print("El valor de a, es impar!")
        return f(a, b)
    return new_function

@decorator
def add(a, b):
  try:
    resultado = a / b
  except:
    return "Cambien el valor de b"
  return resultado

print(add(2, 3))
print(add(20, 4))
print(add(20, 0))
