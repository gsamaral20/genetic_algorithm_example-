# Definições das classes dos itens de viagem

class Item:
    def __init__(self, nome, peso, volume, categoria, genero, estacao = None, obrigatorio = False, multiplo = False):
        self.nome = nome
        self.peso = peso
        self.volume = volume
        self.categoria = categoria
        self.estacao = estacao
        self.genero = genero
        self.obrigatorio = obrigatorio
        self.multiplo = multiplo

itens = [
    # Itens unissex (sem estação definida)
    Item("chinelo", 0.3, 1.2, "calçado", "unissex", obrigatorio=True),
    Item("tênis", 0.8, 2.0, "calçado", "unissex"),
    Item("bota de trilha", 1.2, 3.5, "calçado", "unissex"),
    Item("bota", 1.1, 3.0, "calçado", "unissex", estacao="inverno"),
    Item("meia", 0.05, 0.1, "roupa íntima", "unissex", obrigatorio=True, multiplo=True),
    Item("calça jeans", 0.7, 1.5, "roupa inferior", "unissex"),
    Item("calça chino", 0.6, 1.2, "roupa inferior", "unissex"),
    Item("calça trilha", 0.65, 1.3, "roupa inferior", "unissex"),
    Item("shorts", 0.4, 0.9, "roupa inferior", "unissex", estacao="verao", multiplo=True),
    Item("shorts esporte", 0.35, 0.8, "roupa inferior", "unissex", estacao="verao"),
    Item("calção de banho", 0.3, 0.7, "roupa inferior", "unissex", estacao="verao"),
    Item("cueca", 0.1, 0.15, "roupa íntima", "unissex", obrigatorio=True, multiplo=True),
    Item("camiseta", 0.3, 0.8, "roupa superior", "unissex", obrigatorio=True, multiplo=True),
    Item("camisa esporte", 0.35, 0.9, "roupa superior", "unissex", estacao="verao"),
    Item("camisa manga longa", 0.4, 1.0, "roupa superior", "unissex", multiplo=True),
    Item("camisa manga curta", 0.35, 0.8, "roupa superior", "unissex", estacao="verao", multiplo=True),
    Item("jaqueta corta vento", 0.6, 1.2, "roupa superior", "unissex", estacao="outono"),
    Item("jaqueta jeans", 0.9, 1.8, "roupa superior", "unissex", estacao="inverno"),
    Item("suéter", 0.7, 1.5, "roupa superior", "unissex", estacao="outono"),
    Item("moletom", 0.8, 1.7, "roupa superior", "unissex", estacao="outono"),
    Item("sobretudo", 1.3, 2.5, "roupa superior", "unissex", estacao="inverno"),
    Item("gorro", 0.2, 0.3, "acessório", "unissex", estacao="inverno"),
    Item("luva", 0.15, 0.2, "acessório", "unissex", estacao="inverno"),
    Item("cachecol", 0.3, 0.5, "acessório", "unissex", estacao="inverno"),
    Item("toalha rápida", 0.4, 0.8, "higiene", "unissex"),
    Item("shampoo 100ml", 0.15, 0.2, "higiene", "unissex"),
    Item("condicionador 100ml", 0.15, 0.2, "higiene", "unissex"),
    Item("perfume 100ml", 0.3, 0.4, "higiene", "unissex", obrigatorio=True),
    Item("desodorante rollon 100ml", 0.2, 0.25, "higiene", "unissex", obrigatorio=True),
    Item("protetor solar 100ml", 0.25, 0.3, "higiene", "unissex", estacao="verao"),
    Item("pasta de dente 100ml", 0.1, 0.15, "higiene", "unissex", obrigatorio=True),
    Item("escova de dente", 0.1, 0.15, "higiene", "unissex", obrigatorio=True),
    Item("celular", 0.2, 0.3, "eletrônico", "unissex"),
    Item("carregador", 0.15, 0.2, "eletrônico", "unissex", obrigatorio=True),
    Item("power bank", 0.4, 0.6, "eletrônico", "unissex", obrigatorio=True),
    Item("passaporte", 0.05, 0.1, "documento", "unissex", obrigatorio=True),
    Item("colírio 10ml", 0.05, 0.1, "higiene", "unissex"),
    Item("sabonete em barra", 0.1, 0.15, "higiene", "unissex"),
    Item("máscara para dormir", 0.05, 0.1, "acessório", "unissex"),
    Item("travesseiro de pescoço", 0.3, 0.7, "acessório", "unissex"),
    Item("fone de ouvido", 0.1, 0.2, "eletrônico", "unissex", obrigatorio=True),
    Item("pijama", 0.6, 1.0, "roupa", "unissex", estacao="inverno"),

    # Itens femininos extras
    Item("calcinha", 0.1, 0.15, "roupa íntima", "feminino", obrigatorio=True, multiplo=True),
    Item("sutiã", 0.15, 0.2, "roupa íntima", "feminino", obrigatorio=True, multiplo=True),
    Item("vestido", 0.6, 1.3, "roupa superior", "feminino", estacao="verao", multiplo=True),
    Item("blusa regata", 0.25, 0.5, "roupa superior", "feminino", estacao="verao", multiplo=True),
    Item("saia", 0.4, 0.8, "roupa inferior", "feminino", estacao="outono", multiplo=True),
    Item("casaco leve", 0.7, 1.2, "roupa superior", "feminino", estacao="outono"),
    Item("jaqueta de couro", 0.9, 1.5, "roupa superior", "feminino", estacao="inverno"),
    Item("chapéu", 0.2, 0.3, "acessório", "feminino", estacao="verao"),
    Item("bijuterias", 0.1, 0.1, "acessório", "feminino"),
    Item("maquiagem básica", 0.3, 0.4, "higiene", "feminino", obrigatorio=True),
    Item("absorventes", 0.15, 0.2, "higiene", "feminino", obrigatorio=True, multiplo=True),
    Item("escova de cabelo", 0.15, 0.3, "higiene", "feminino", obrigatorio=True),
    Item("secador de cabelo portátil", 0.6, 0.8, "eletrônico", "feminino"),
    Item("creme hidratante", 0.2, 0.3, "higiene", "feminino"),
    Item("perfume extra", 0.1, 0.05, "higiene", "feminino"),
    Item("legging", 0.4, 0.7, "roupa inferior", "feminino"),
    Item("roupão", 0.8, 1.5, "roupa", "feminino", estacao="inverno"),
    Item("biquíni", 0.2, 0.4, "roupa", "feminino", estacao="verao"),
    Item("maiô", 0.3, 0.5, "roupa", "feminino", estacao="verao"),
]

#print("Quantidade de itens no item.py:", len(itens))
