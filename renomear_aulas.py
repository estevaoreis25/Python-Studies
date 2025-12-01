"""
Script para renomear arquivos com 'copy' no nome para sequência numérica de aulas.
Encontra o último arquivo 'aula{numero}.py' sem 'copy' e continua a numeração.
"""
import os
import re
from pathlib import Path


def encontrar_ultimo_numero_aula(diretorio):
    """
    Encontra o maior número de aula sem 'copy' no nome.
    
    Args:
        diretorio: Path do diretório a ser verificado
        
    Returns:
        int: O maior número encontrado ou 0 se não houver arquivos
    """
    arquivos = list(diretorio.glob("aula*.py"))
    numeros = []
    
    for arquivo in arquivos:
        nome = arquivo.name
        # Ignora arquivos com 'copy' no nome
        if 'copy' in nome.lower():
            continue
        
        # Extrai apenas o número do nome (ex: aula47.py -> 47)
        match = re.match(r'aula\s*(\d+)\.py', nome)
        if match:
            numeros.append(int(match.group(1)))
    
    return max(numeros) if numeros else 0


def listar_arquivos_com_copy(diretorio):
    """
    Lista todos os arquivos que contêm 'copy' no nome, ordenados.
    
    Args:
        diretorio: Path do diretório a ser verificado
        
    Returns:
        list: Lista de Path objects ordenados
    """
    arquivos_copy = []
    
    # Padrões para encontrar arquivos com copy
    for arquivo in diretorio.glob("aula*copy*.py"):
        arquivos_copy.append(arquivo)
    
    # Ordena os arquivos para manter a ordem correta
    def extrair_numero_copy(nome):
        """Extrai o número do copy para ordenação correta"""
        # Procura por "copy" seguido de número ou apenas "copy"
        match = re.search(r'copy\s*(\d+)', nome.lower())
        if match:
            return int(match.group(1))
        elif 'copy' in nome.lower() and not re.search(r'copy\s*\d+', nome.lower()):
            return 0  # "aula47 copy.py" sem número vem primeiro
        return -1
    
    arquivos_copy.sort(key=lambda x: (
        re.match(r'aula(\d+)', x.name).group(1) if re.match(r'aula(\d+)', x.name) else '',
        extrair_numero_copy(x.name)
    ))
    
    return arquivos_copy


def renomear_arquivos(diretorio, dry_run=True):
    """
    Renomeia arquivos com 'copy' para a sequência numérica correta.
    
    Args:
        diretorio: Path do diretório com os arquivos
        dry_run: Se True, apenas mostra o que seria feito sem executar
        
    Returns:
        tuple: (sucesso, falhas) - contadores de operações
    """
    # Encontra o último número de aula
    ultimo_numero = encontrar_ultimo_numero_aula(diretorio)
    print(f"Último arquivo encontrado: aula{ultimo_numero}.py")
    print(f"Iniciando renomeação a partir de: aula{ultimo_numero + 1}.py\n")
    
    # Lista arquivos com copy
    arquivos_copy = listar_arquivos_com_copy(diretorio)
    
    if not arquivos_copy:
        print("Nenhum arquivo com 'copy' encontrado.")
        return 0, 0
    
    print(f"Encontrados {len(arquivos_copy)} arquivo(s) para renomear:\n")
    
    # Renomeia os arquivos
    contador_novo = ultimo_numero + 1
    sucesso = 0
    falhas = 0
    
    for arquivo in arquivos_copy:
        novo_nome = f"aula{contador_novo}.py"
        novo_caminho = diretorio / novo_nome
        
        # Verifica se o novo nome já existe
        if novo_caminho.exists():
            print(f"❌ ERRO: {novo_nome} já existe! Pulando {arquivo.name}")
            falhas += 1
            contador_novo += 1
            continue
        
        if dry_run:
            print(f"[SIMULAÇÃO] {arquivo.name} -> {novo_nome}")
        else:
            try:
                arquivo.rename(novo_caminho)
                print(f"✓ Renomeado: {arquivo.name} -> {novo_nome}")
                sucesso += 1
            except Exception as e:
                print(f"❌ Erro ao renomear {arquivo.name}: {e}")
                falhas += 1
        
        contador_novo += 1
    
    return sucesso, falhas


def main():
    """Função principal do script"""
    # Diretório atual (onde o script está)
    diretorio_atual = Path(__file__).parent
    
    print("=" * 60)
    print("Script de Renomeação de Arquivos de Aulas")
    print("=" * 60)
    print(f"Diretório: {diretorio_atual}\n")
    
    # Primeira execução: modo simulação
    print("--- MODO SIMULAÇÃO ---")
    print("Mostrando o que será feito sem executar...\n")
    sucesso_sim, falhas_sim = renomear_arquivos(diretorio_atual, dry_run=False)
    
    if sucesso_sim + falhas_sim == 0:
        print("\nNenhuma operação a ser realizada.")
        return
    
    # Pergunta ao usuário se quer prosseguir
    print("\n" + "=" * 60)
    resposta = input("\nDeseja executar a renomeação? (s/n): ").lower().strip()
    
    if resposta in ['s', 'sim', 'y', 'yes']:
        print("\n--- EXECUTANDO RENOMEAÇÃO ---\n")
        sucesso, falhas = renomear_arquivos(diretorio_atual, dry_run=False)
        
        print("\n" + "=" * 60)
        print(f"Renomeação concluída!")
        print(f"✓ Sucesso: {sucesso} arquivo(s)")
        if falhas > 0:
            print(f"❌ Falhas: {falhas} arquivo(s)")
        print("=" * 60)
    else:
        print("\nOperação cancelada pelo usuário.")


if __name__ == "__main__":
    main()
