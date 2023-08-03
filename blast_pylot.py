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

