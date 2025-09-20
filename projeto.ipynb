import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
import csv
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Configurações iniciais
sns.set(style="whitegrid")
#file_path = r"C:\Users\HugoSouza\Desktop\Projeto_Bruno\export\export.csv"
file_path = r"export.csv"

with open(file_path, "r", encoding="utf-8") as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    f.seek(0)
    df = pd.read_csv(f, delimiter=dialect.delimiter)

df['ADMISSAO'] = pd.to_datetime(df['ADMISSAO'], errors='coerce', dayfirst=True)
df['DESLIGAMENTO'] = pd.to_datetime(df['DESLIGAMENTO'], errors='coerce', dayfirst=True)

categorical_cols = ['UF', 'CARGO', 'FUNCAO', 'ESPECIALIDADE', 'SITUACAO', 'SE', 'REFERENCIA']
for col in categorical_cols:
    df[col] = df[col].astype('category')

df = df.dropna(subset=['ADMISSAO'])

# Estatísticas descritivas
estatisticas = ""
estatisticas += f"Intervalo de Admissão: {df['ADMISSAO'].min().date()} → {df['ADMISSAO'].max().date()}\n"
estatisticas += f"Intervalo de Desligamento: {df['DESLIGAMENTO'].min().date()} → {df['DESLIGAMENTO'].max().date()}\n\n"
estatisticas += "Situação dos Funcionários:\n"
estatisticas += df['SITUACAO'].value_counts().to_string() + "\n\n"
estatisticas += "Top 10 UFs com mais registros:\n"
estatisticas += df['UF'].value_counts().head(10).to_string() + "\n\n"

# Gráfico 1
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='SITUACAO', order=df['SITUACAO'].value_counts().index)
plt.title("Distribuição por Situação")
plt.tight_layout()
grafico1_path = "grafico_situacao.png"
plt.savefig(grafico1_path)
plt.close()

# Gráfico 2
plt.figure(figsize=(12, 6))
top_ufs = df['UF'].value_counts().head(10).index
sns.countplot(data=df[df['UF'].isin(top_ufs)], x='UF', hue='SITUACAO')
plt.title("Situação por UF (Top 10)")
plt.legend(title="Situação")
plt.tight_layout()
grafico2_path = "grafico_ufs_top10.png"
plt.savefig(grafico2_path)
plt.close()

# Teste Qui-quadrado
contingencia = pd.crosstab(df['UF'], df['SITUACAO'])
chi2, p, dof, expected = chi2_contingency(contingencia)
estatisticas += "Teste de Qui-quadrado para proporção de desligados por UF:\n"
estatisticas += f"Estatística Qui²: {chi2:.2f}\n"
estatisticas += f"p-valor: {p:.4f}\n"
estatisticas += (
    "→ Há evidências de diferença significativa.\n" if p < 0.05
    else "→ Não há evidências suficientes de diferença.\n"
)

# Criar Janela
janela = tk.Tk()
janela.title("Análise de Dados - Funcionários")
janela.geometry("1000x800")
# janela.state('zoomed')

frame = ttk.Frame(janela)
frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(frame)
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Texto com resultados
label_texto = tk.Label(scrollable_frame, text=estatisticas, justify="left", anchor="w", font=("Courier", 10))
label_texto.pack(padx=10, pady=10, anchor="w")

# Função para inserir imagens
def inserir_imagem(caminho):
    imagem = Image.open(caminho)
    imagem = imagem.resize((800, 400))
    foto = ImageTk.PhotoImage(imagem)
    label = tk.Label(scrollable_frame, image=foto)
    label.image = foto
    label.pack(pady=10)

# Mostrar os gráficos
inserir_imagem(grafico1_path)
inserir_imagem(grafico2_path)

janela.mainloop()
