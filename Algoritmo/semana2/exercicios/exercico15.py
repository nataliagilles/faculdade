maior_candidatos_por_vaga= 0
maior-codigo= 0
total_candidatos= 0

codigo_curso= int(input("Digite o código do curso:  "))

while codigo_curso != 0:
    vagas= int(input("Digite o número de vagas:  "))

    candidatos_homens= int(input("Digite o número de candidatos homens:  "))
    candidatas_femininas= int(input("Digite o número de candidatas mulheres:  "))

    total_curso= candidatos_homens + candidatas_femininas
    candidato_por_vaga= total_curso / vagas
    percentual_feminino= (candidatas_femininas / total_curso)* 100

    print(f"Curso: {codigo_curso}")
    print(f"Candidatos por vaga: {candidato_por_vaga}")
    print(f"Percentual femino: {percentual_feminino}")

    if candidato_por_vaga > maior_candidatos_por_vaga:
    maior_candidatos_por_vaga= candidato_por_vaga
    codigo_maior= codigo_curso

    total_candidatos += total_curso
    
    codigo_curso= int(input("Digite o código do curso (0 para terminar):  "))

print(f"Maior número de candidatos {maior_candidatos_por_vaga.2f}")
print(f"Código do curso com maior candidatos por vaga: {codigo_maior}")
print(f"Total de candidatos em todos os cursos: {total_candidatos}")

