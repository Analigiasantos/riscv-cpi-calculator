import sys

# Verificar se o usuário passou o arquivo
if len(sys.argv) < 2:
    print("Uso: python script_cpi_riscv.py <arquivo_dump>")
    sys.exit(1)

arquivo_dump = sys.argv[1]

# Mapeamento de opcode para tipo e ciclos
opcode_ciclos = {
    "0110011": ("R", 4),      # R-type
    "0010011": ("I", 4),      # I-type (immediate ALU)
    "0000011": ("Load", 5),   # Load
    "0100011": ("Store", 4),  # Store
    "1100011": ("Branch", 3), # Branch
    "1101111": ("Jump", 3),   # JAL
    "1100111": ("JumpReg", 3),# JALR
    "0010111": ("AUIPC", 3),  # U-type
    "0110111": ("LUI", 3),    # U-type
}

# Inicialização
total_ciclos = 0
contagem_tipo = {}
instr_total = 0

# Ler arquivo de dump
with open(arquivo_dump, "r") as f:
    instrs = [line.strip() for line in f.readlines()]

# Processar instruções
for instr in instrs:
    if len(instr) != 32:
        print(f"Instrução inválida (não 32 bits): {instr}")
        continue
    opcode = instr[25:32]  # últimos 7 bits
    tipo_ciclo = opcode_ciclos.get(opcode)
    if tipo_ciclo:
        tipo, ciclos = tipo_ciclo
    else:
        tipo, ciclos = ("Desconhecido", 0)
    
    total_ciclos += ciclos
    contagem_tipo[tipo] = contagem_tipo.get(tipo, 0) + 1
    instr_total += 1

# Calcular CPI médio
cpi_medio = total_ciclos / instr_total if instr_total > 0 else 0

# Imprimir relatório
print("Relatório de ciclos - RISC-V multiciclo")
print("---------------------------------------")
print(f"{'Tipo':<12} | {'Qtde Instr.':<10} | {'Ciclos/Instr.':<12}")
print("---------------------------------------")
for tipo, qtde in contagem_tipo.items():
    ciclos_instr = next((c for t, c in opcode_ciclos.values() if t == tipo), 0)
    print(f"{tipo:<12} | {qtde:<10} | {ciclos_instr:<12}")
print("---------------------------------------")
print(f"Total de ciclos: {total_ciclos}")
print(f"CPI médio: {cpi_medio:.2f}")
