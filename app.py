import streamlit as st
from biology_engine import *

st.set_page_config(page_title="基因突变模拟工具", layout="wide")

st.title("🧬 基因突变模拟工具")

dna = st.text_input("请输入 DNA 序列：", "TACAAA")

col1, col2 = st.columns(2)

with col1:
    mutation = st.selectbox("突变类型", ["substitution", "insertion", "deletion"])

with col2:
    index = st.number_input("突变位置（从0开始）", min_value=0, value=0)

new_base = None
if mutation != "deletion":
    new_base = st.selectbox("新碱基", ["A", "T", "C", "G"])

if st.button("🚀 执行突变"):

    mutated = mutate_dna(dna, mutation, index, new_base)

    mrna_before = transcribe_dna_to_mrna(dna)
    mrna_after = transcribe_dna_to_mrna(mutated)

    protein_before = translate_mrna(mrna_before)
    protein_after = translate_mrna(mrna_after)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("突变前")
        st.write("DNA:", dna)
        st.write("mRNA:", mrna_before)
        st.write("蛋白质:", protein_before if protein_before else "未检测到（无AUG）")

    with col2:
        st.subheader("突变后")
        st.write("DNA:", mutated)
        st.write("mRNA:", mrna_after)
        st.write("蛋白质:", protein_after if protein_after else "未检测到（无AUG）")

    st.divider()

    result = analyze_mutation(protein_before, protein_after)
    st.success(f"突变影响分析：{result}")
