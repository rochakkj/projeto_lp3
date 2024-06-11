
from validate_docbr import CPF
from flask import 


cpf = CPF()

print(cpf.generate(True))
print(cpf.generate(False))
