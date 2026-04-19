import streamlit as st
from biology_engine import *

st.set_page_config(page_title="基因突变模拟工具", layout="wide")

st.title("🧬 基因突变模拟工具")

# ===== 输入区域 =====
dna = st.text_input("请输入 DNA 序列：", "ATCG")

col1, col2 = st.columns(2)

with col1:
    mutation_type = st.selectbox(
        "选择突变类型",
        ["substitution", "insertion", "deletion"]
    )

with col2:
    index = st.number_input("突变位置（从0开始）", min_value=0, value=0)

new_base = None
if mutation_type != "deletion":
    new_base = st.selectbox("选择新碱基", ["A", "T", "C", "G"])

# ===== 执行按钮 =====
if st.button("🚀 执行突变"):

    mutated = mutate_dna(dna, mutation_type, index, new_base)

    st.divider()

    col1, col2 = st.columns(2)

    # ===== 左边：突变前 =====
    with col1:
        st.subheader("突变前")

        st.write("DNA:", dna)

        mrna_before = transcribe_dna_to_mrna(dna)
        st.write("mRNA:", mrna_before)

        protein_before = translate_mrna(mrna_before)
        st.write("蛋白质:", protein_before)

    # ===== 右边：突变后 =====
    with col2:
        st.subheader("突变后")

        st.write("DNA:", mutated)

        mrna_after = transcribe_dna_to_mrna(mutated)
        st.write("mRNA:", mrna_after)

        protein_after = translate_mrna(mrna_after)
        st.write("蛋白质:", protein_after)