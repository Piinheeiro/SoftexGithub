from abc import ABC, abstractmethod

# Classe Base Abstrata
class Produto(ABC):
    def __init__(self, nome, preco_base):
        self.nome = nome
        self.preco_base = preco_base
    
    
    def calcular_preco_final(self):
        """Método abstrato que deve ser implementado pelas subclasses"""
        pass
    
   # def __str__(self):
    #    return f"{self.nome} (R$ {self.preco_base:.2f})"

# Classe Derivada para Produtos Físicos
class ProdutoFisico(Produto):
    def __init__(self, nome, preco_base, custo_frete):
        super().__init__(nome, preco_base)
        self.custo_frete = custo_frete
    
    def calcular_preco_final(self):
        """Calcula preço final incluindo custo do frete"""
        return self.preco_base + self.custo_frete
    
    def __str__(self):
        return f"{super().__str__()} + frete R$ {self.custo_frete:.2f}"

# Classe Derivada para Produtos Digitais
class ProdutoDigital(Produto):
    def __init__(self, nome, preco_base, taxa_servico):
        super().__init__(nome, preco_base)
        self.taxa_servico = taxa_servico
    
    def calcular_preco_final(self):
        """Calcula preço final incluindo taxa de serviço"""
        return self.preco_base + self.taxa_servico
    
    def __str__(self):
        return f"{super().__str__()} + taxa R$ {self.taxa_servico:.2f}"

# Área de Testes - Simulação do Carrinho de Compras
def main():
    print("=== LOJA VIRTUAL - CARRINHO DE COMPRAS ===\n")
    
    # Criando produtos para o carrinho
    carrinho = [
        ProdutoFisico("Livro: Python para Iniciantes", 50.00, 15.00),
        ProdutoDigital("E-book: Data Science", 35.00, 2.50),
        ProdutoFisico("Caneca Personalizada", 25.00, 8.00),
        ProdutoDigital("Curso Online: Web Development", 120.00, 5.00),
        ProdutoFisico("Livro: Algoritmos Avançados", 80.00, 12.00),
        ProdutoDigital("Assinatura Premium", 29.90, 1.50)
    ]
    
    # Calculando preços finais e total da compra
    total_compra = 0.0
    
    print("Itens no carrinho:")
    print("-" * 50)
    
    for i, produto in enumerate(carrinho, 1):
        preco_final = produto.calcular_preco_final()
        total_compra += preco_final
        
        print(f"{i}. {produto}")
        print(f"   Preço final: R$ {preco_final:.2f}")
        print()
    
    print("-" * 50)
    print(f"TOTAL DA COMPRA: R$ {total_compra:.2f}")
    print("=" * 50)

if __name__ == "__main__":
    main()