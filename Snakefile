rule all:
    input:"output/tRNA_scan_result.txt"
        "output/G_intestinalis.tRNA"

rule tRNAscan:
    input: "resource/G_intestinalis.fasta"
    output: "output/tRNA_scan_result.txt"
    shell: "bash tRNAscah.sh {input} {output}"

rule tRNAscan_stats:
    input:
        genome= "resource/G_intestinalis.fasta"
    output:
        tRNA = "output/G_intestinalis.tRNA"
        stats = "output/G_intestinalis.tRNA"
    params:
        threads = 2
    conda:
        "envs/environment.yml"
    script:
        "scripts/tRNAscan_stats.py"