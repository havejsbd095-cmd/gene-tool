# ===== 1. 碱基配对规则 =====
dna_to_mrna_map = {
    'A': 'U',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

# ===== 2. 密码子表（简化版，可扩展）=====
codon_table = {
    'AUG': 'Met',  # 起始
    'UUU': 'Phe', 'UUC': 'Phe',
    'UUA': 'Leu', 'UUG': 'Leu',
    'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop'
}

# ===== 3. 转录 DNA -> mRNA =====
def transcribe_dna_to_mrna(dna):
    dna = dna.upper()
    return ''.join([dna_to_mrna_map.get(base, '?') for base in dna])

# ===== 4. 翻译 mRNA -> 蛋白质 =====
def translate_mrna(mrna):
    protein = []

    for i in range(0, len(mrna), 3):
        codon = mrna[i:i+3]

        if len(codon) < 3:
            break

        amino_acid = codon_table.get(codon, '???')

        if amino_acid == 'Stop':
            break

        protein.append(amino_acid)

    return protein

# ===== 5. 突变函数 =====
def mutate_dna(seq, mutation_type, index, new_base=None):
    seq = seq.upper()

    if index < 0 or index >= len(seq):
        return seq  # 防止报错

    if mutation_type == "substitution":
        seq_list = list(seq)
        seq_list[index] = new_base
        return ''.join(seq_list)

    elif mutation_type == "insertion":
        return seq[:index] + new_base + seq[index:]

    elif mutation_type == "deletion":
        return seq[:index] + seq[index+1:]

    return seq