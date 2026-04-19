# ===== 1. DNA -> mRNA =====
dna_to_mrna_map = {
    'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'
}

# ===== 2. 完整密码子表（标准）=====
codon_table = {
    'UUU':'Phe','UUC':'Phe','UUA':'Leu','UUG':'Leu',
    'CUU':'Leu','CUC':'Leu','CUA':'Leu','CUG':'Leu',
    'AUU':'Ile','AUC':'Ile','AUA':'Ile','AUG':'Met',
    'GUU':'Val','GUC':'Val','GUA':'Val','GUG':'Val',

    'UCU':'Ser','UCC':'Ser','UCA':'Ser','UCG':'Ser',
    'CCU':'Pro','CCC':'Pro','CCA':'Pro','CCG':'Pro',
    'ACU':'Thr','ACC':'Thr','ACA':'Thr','ACG':'Thr',
    'GCU':'Ala','GCC':'Ala','GCA':'Ala','GCG':'Ala',

    'UAU':'Tyr','UAC':'Tyr','UAA':'Stop','UAG':'Stop',
    'CAU':'His','CAC':'His','CAA':'Gln','CAG':'Gln',
    'AAU':'Asn','AAC':'Asn','AAA':'Lys','AAG':'Lys',
    'GAU':'Asp','GAC':'Asp','GAA':'Glu','GAG':'Glu',

    'UGU':'Cys','UGC':'Cys','UGA':'Stop','UGG':'Trp',
    'CGU':'Arg','CGC':'Arg','CGA':'Arg','CGG':'Arg',
    'AGU':'Ser','AGC':'Ser','AGA':'Arg','AGG':'Arg',
    'GGU':'Gly','GGC':'Gly','GGA':'Gly','GGG':'Gly'
}

# ===== 3. 转录 =====
def transcribe_dna_to_mrna(dna):
    return ''.join([dna_to_mrna_map.get(b, '?') for b in dna.upper()])

# ===== 4. 翻译（从AUG开始）=====
def translate_mrna(mrna):
    protein = []

    start = mrna.find("AUG")
    if start == -1:
        return []

    for i in range(start, len(mrna), 3):
        codon = mrna[i:i+3]
        if len(codon) < 3:
            break

        aa = codon_table.get(codon, '???')

        if aa == 'Stop':
            break

        protein.append(aa)

    return protein

# ===== 5. 突变 =====
def mutate_dna(seq, mtype, index, new_base=None):
    seq = seq.upper()

    if index < 0 or index >= len(seq):
        return seq

    if mtype == "substitution":
        seq = list(seq)
        seq[index] = new_base
        return ''.join(seq)

    if mtype == "insertion":
        return seq[:index] + new_base + seq[index:]

    if mtype == "deletion":
        return seq[:index] + seq[index+1:]

    return seq

# ===== 6. 突变影响判断 =====
def analyze_mutation(protein_before, protein_after):

    if protein_before == protein_after:
        return "Silent Mutation（无影响）"

    if len(protein_after) < len(protein_before):
        return "Nonsense Mutation（提前终止）"

    return "Missense Mutation（蛋白质改变）"
