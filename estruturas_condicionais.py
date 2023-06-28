from ocrmypdf import InputFileError


MAIOR_IDADE = 18

idade = int(input("Informe a sua idade: "))

if idade >=MAIOR_IDADE:
    print("Maior idade, pode tirar a cnh.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Manior de idade, pode tirar a CNH")
else:
    print("Ainda não pode tirar a CNH.")