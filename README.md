# riscv-cpi-calculator
Calcula o total de ciclos e CPI médio de programas RISC-V a partir de um dump de instruções

# RISC-V CPI Calculator

Este projeto contém um **script Python** para calcular o **total de ciclos** e o **CPI médio** de programas RISC-V, a partir de arquivos de dump de instruções (ROM). O script considera a execução em um **processador multiciclo**.

---

## 📂 Estrutura do projeto

- `script_cpi_riscv.py` → Script principal em Python.
- `dump.txt` → Exemplo de arquivo de dump com instruções RISC-V (uma instrução por linha, em binário).

---

## 🚀 Como usar

1. Clone ou faça download deste repositório.
2. Prepare seu arquivo de dump de instruções (`.dump` ou `.txt`), uma instrução por linha, em binário de 32 bits.
3. Execute o script no terminal:

```bash
python script_cpi_riscv.py <arquivo_dump>
