class MyError(Exception):
    ...
    
class OtherError(Exception):
    ...

def levantar():
    raise MyError("ErroA", "ErroB", "ErroC")

try:
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    raise OtherError("Vou relançar a execao") from error