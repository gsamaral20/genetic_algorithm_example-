
# Importação das bibliotecas que serão utilizadas no projeto
import pandas as pd
import pygad 
from item import itens
from restricoes import restringir_capacidade_mochila, restringir_genero, restringir_item_obrigatorio, restringir_itens_estacao, restringir_peca_intimas, restringir_volume_mochila, restringir_item_unitario, recompensar_peca_intimas, restringir_categoria

# Input das informações gerais da viagem
genero_viajante = "masculino" #str(input("Informe o gênero: "))
capacidade_mochila = 10 #float(input("Insira a capacidade da mochila: "))
volume_mochila = 10 #float(input("Insira o volume da mochila: "))
numero_dias_viagem = 4 #int(input("Insira o número de dias da viagem: "))
estacao = "verão" #str(input("Informe a estação do ano que vai viajar: "))

#print("Quantidade de itens importados:", len(itens))


# População inicial 

def fitness_function(ga_instance, individuo, solution_idx):
    pontos_inicial = sum(individuo)

    # Comente as restrições duras para teste:
    #pontos_ajustados = restringir_item_genero(pontos_inicial, genero_viajante, individuo, itens)
    #if pontos_ajustados == 0:
        #return 0

    pontos_ajustados = restringir_capacidade_mochila(pontos_inicial, capacidade_mochila, individuo, itens)
    #if pontos_ajustados == 0:
    #     return 0

    pontos_ajustados = restringir_volume_mochila(pontos_ajustados, volume_mochila, individuo, itens)
    # if pontos_ajustados == 0:
    #     return 0

    #pontos_ajustados = pontos_inicial

    # Deixe as restrições suaves para ajudar na evolução:
    pontos_ajustados = restringir_genero(pontos_ajustados, genero_viajante, individuo, itens)
    pontos_ajustados = restringir_peca_intimas(pontos_ajustados, numero_dias_viagem, individuo, itens)
    pontos_ajustados = restringir_itens_estacao(pontos_ajustados, estacao, individuo, itens)
    pontos_ajustados = restringir_item_obrigatorio(pontos_ajustados, individuo, itens)
    pontos_ajustados = restringir_item_unitario(pontos_ajustados, individuo, itens)
    pontos_ajustados = recompensar_peca_intimas(pontos_ajustados, numero_dias_viagem, individuo, itens)
    pontos_ajustados = restringir_categoria(pontos_ajustados, numero_dias_viagem, individuo, itens)

    print(f"Indivíduo #{solution_idx}: {individuo} - Fitness: {pontos_ajustados}")
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

num_genes = len(itens)

ga_instance = pygad.GA(
    num_generations=100, 
    sol_per_pop=populacao, 
    num_parents_mating=int(populacao*0.4), 
    fitness_func=fitness_function,
    num_genes = len(itens), 
    gene_type=int, 
    gene_space = list(range(numero_dias_viagem + 1)), 
    parent_selection_type="tournament",
    keep_elitism=3, 
    crossover_type="single_point", 
    crossover_probability=0.8,
    mutation_type="random", 
    mutation_probability=0.05,
    mutation_percent_genes=10
)

ga_instance.run()

solution, fitness_value, _ = ga_instance.best_solution()

# Mostrar lista de itens correspondentes
for idx, qtd in enumerate(solution):
    if qtd > 0:
        print(f"{itens[idx].nome} - {qtd} unidade(s)")

ga_instance.plot_fitness()