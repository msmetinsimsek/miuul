import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option("display.width", 500)

blast_G_muris = pd.read_csv("output/blastn/G_intestinalis/G_muris.blastn", sep="\t", header=None)
blast_S_salmonicida = pd.read_csv("output/blastn/G_intestinalis/S_salmonicida.blastn", sep="\t",
                                  header=None)


blast_G_muris.columns = ["qseqid", "sseqid", "pident", "length", "mismatch", "gapopen",
                         "qstart", "qend", "sstart", "send", "evalue", "bitscore"]

blast_S_salmonicida.columns = ["qseqid", "sseqid", "pident", "length", "mismatch", "gapopen",
                               "qstart", "qend", "sstart", "send", "evalue", "bitscore"]

num_hits_blast_G_muris = len(blast_G_muris)

num_hits_blast_S_salmonicida = len((blast_S_salmonicida))

print("Number of hits for Giardia intentinalis & Giardia muris: ", num_hits_blast_G_muris)

print("Number of hits for Giardia intentinalis & Spironucleus salmonicida: ", num_hits_blast_S_salmonicida)


# histogram grafiği blast_G_muris

sns.histplot(blast_G_muris, x="pident")
plt.show()




# heatmap

pivot_table = pd.pivot_table(blast_G_muris, values="lenght", index="qseqid", columns="sseqid")
sns.heatmap(pivot_table)
plt.show()



# scatter plot

sns.scatterplot(blast_G_muris.reset_index(), x="index", y="bitscore", hue="pident")
plt.show()


sns.scatterplot(blast_G_muris.reset_index(), x="index", y="length", hue="pident")
plt.show()


input = "output/tRNAscan/G_muris.tRNA"
out = "plots/tRNAscan/G_muris.svg"


df = pd.read_csv(input, sep="\t", header=None, skiprows=3, usecols=[0, 1, 2, 3, 4, 5])
df.shape

df.columns = ["Name", "tRNA", "Begin", "End", "Type", "Codon"]

df.drop_duplicates(inplace=True)

df["Begin"] = pd.to_numeric(df["Begin"], errors="coerce")
df["End"] = pd.to_numeric(df["End"], errors="coerce")

df["y"] = range(1, len(df) + 1)


plt.figure(figsize=(10, 6))
plt.scatter(df["Begin"], df["y"], alpha=0.5, color="red", label="Begin")
plt.xlabel("Position in Genome")
plt.ylabel("tRNA")
plt.title("Distribution od tRNAs Across the Genome")
plt.savefig(out, format="svg", bbox_inches="tight", dpi=300)
plt.show()