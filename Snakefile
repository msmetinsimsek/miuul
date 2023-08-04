rule all:
   input:
        "output/tRNA_scan_result.txt",
        "output/G_intestinalis.tRNA",
        "output/G_intestinalis.stats",
       # "output/S_salmonicida.tRNA",
       # "output/S_salmonicida.stats",
        "output/tRNAscan/G_intestinalis.tRNA",
        expand("output/tRNAscan/{sp}.tRNA", sp=["G_muris", "G_intestinalis"]),
        expand("output/blastn/G_intestinalis/{sp}.blastn", sp=["G_muris", "S_salmonicida"])


rule tRNAscan:
    input: "resource/G_intestinalis.fasta"
 #: input: "resource/S_salmonicida.fasta"
    output: "output/tRNA_scan_result.txt",
    conda:
         "envs/environment.yml"
    shell: """tRNAscan-SE {input} -o {output}"""


rule tRNAscan_stats:
    input:
        genome = "resource/genomes/G_intestinalis.fasta"
    output:
        tRNA = "output/G_intestinalis.tRNA",
        stats = "output/G_intestinalis.stats"
    ## rule tRNAscan_stats:
#     input:
#         genome = "resource/genomes/S_salmonicida.fasta"
#     output:
#         tRNA = "output/S_salmonicida.tRNA",
#         stats = "output/S_salmonicida.stats"
    params:
        threads = 2
    conda:
        "envs/environment.yml"
    script:
        "scripts/tRNAscan_stats.py"

rule tRNAscan_stats_wildcard:
    input:
        genome= "resource/genomes/{genome}.fasta"
    output:
        tRNA= "output/tRNAscan/{genome}.tRNA",
        stats= "output/tRNAscan/{genome}.stats"
    params:
        threads= 2
    conda:
        "envs/environment.yml"
    script:
        "scripts/tRNAscan_stats.py"


rule makeblastdb:
    input:
        "resource/{type}/db/{db}.fasta"
    output:
        "output/{type}/db/{db}.ndb",
        "output/{type}/db/{db}.nhr",
        "output/{type}/db/{db}.nin",
        "output/{type}/db/{db}.not",
        "output/{type}/db/{db}.nsq",
        "output/{type}/db/{db}.ntf",
        "output/{type}/db/{db}.nto"
    params:
        outname = "output/{type}/db/{db}"
    conda:
        "envs/environment.yml"
    shell:
        "makeblastdb -dbtype nucl -in {input} -out {params.outname}"

rule blastn:
    input:
        query= "resource/{type}/query/{query}.fasta",
        db= "output/{type}/db/{db}.ndb"
    output:
        "output/{type}/{db}/{query}.blastn"
    params:
        perc_identity=95,
        outfmt=6,
        num_threads=2,
        max_target_seqs=2,
        max_hsps=1,
        db_prefix="output/{type}/db/{db}"
    conda:
        "envs/environment.yml"
    script:
        "scripts/blastn.py"
