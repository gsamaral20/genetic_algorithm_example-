
# Importação das bibliotecas que serão utilizadas no projeto
import pandas as pd
import pygad 
from item import itens
from restricoes import restringir_capacidade_mochila, restringir_item_genero, restringir_item_obrigatorio, restringir_itens_estacao, restringir_peca_intimas, restringir_volume_mochila

# Input das informações gerais da viagem
genero_viajante = str(input("Informe o gênero: "))
capacidade_mochila = float(input("Insira a capacidade da mochila: "))
volume_mochila = float(input("Insira o volume da mochila: "))
numero_dias_viagem = int(input("Insira o número de dias da viagem: "))
estacao = str(input("Informe a estação do ano que vai viajar: "))


# População inicial 

def fitness_function(ga_instance, individuo, solution_idx):
    pontos_inicial = 0
    for indice, selecao in enumerate(individuo):
        pontos_inicial += selecao
    
    pontos_ajustados = pontos_inicial

    # Restrições duras primeiro (podem zerar direto)
    pontos_ajustados = restringir_item_genero(pontos_ajustados, genero_viajante, individuo, itens)
    if pontos_ajustados == 0:
        return 0

    pontos_ajustados = restringir_capacidade_mochila(pontos_ajustados, capacidade_mochila, individuo, itens)
    if pontos_ajustados == 0:
        return 0

    pontos_ajustados = restringir_volume_mochila(pontos_ajustados, volume_mochila, individuo, itens)
    if pontos_ajustados == 0:
        return 0

    # Restrições “suaves” com penalizações/recompensas
    pontos_ajustados = restringir_peca_intimas(pontos_ajustados, numero_dias_viagem, individuo, itens)
    pontos_ajustados = restringir_itens_estacao(pontos_ajustados, estacao, individuo, itens)
    pontos_ajustados = restringir_item_obrigatorio(pontos_ajustados, True, individuo, itens)

    return max(pontos_ajustados, 0)

gene_space = []
for i in range(0, numero_dias_viagem + 1):
    gene_space.append(i)

item_individuo = itens[0]
n_variaveis = 0
for atributo, valor in vars(item_individuo).items():
    if valor is not None:
        n_variaveis += 1

populacao = 10*n_variaveis

ga_instance = pygad.GA(
    num_generations=100, 
    sol_per_pop=populacao, 
    num_parents_mating=int(populacao*0.4), 
    fitness_func=fitness_function,
    num_genes=n_variaveis, 
    gene_type=int, 
    gene_space=gene_space, 
    parent_selection_type="rws",
    keep_elitism=3, 
    crossover_type="single_point", 
    crossover_probability=0.8,
    mutation_type="random", 
    mutation_percent_genes=10
)

ga_instance.run()

solution, fitness_value, _ = ga_instance.best_solution()

# Mostrar lista de itens correspondentes
for idx, qtd in enumerate(solution):
    if qtd > 0:
        print(f"{itens[idx].nome} - {qtd} unidade(s)")

ga_instance.plot_fitness()