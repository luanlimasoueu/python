from validacpf import ValidaCpf

cpf = ValidaCpf('413.717.708-24')

if cpf.valida():
    print( 'CPF válido.')
else:
     print( 'CPF não é válido.')

    
