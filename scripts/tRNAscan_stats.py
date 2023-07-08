from snakemake.shell import shell

genome = snakemake.input.genome
tRNA = snakemake.output.tRNA
stats = snakemake.output.stats

shell(f"""tRNAscan-SE {genome} -o {tRNA} -m {stats}""")


#yüklem ypaparken snakefile dosyasını çalıştırmak için
# snakemake --jobs 1 -c1 --use-conda --printshellcmds -n komutu ile snakefile in çalışıp çalışmadığını komntorl ettim
# snakemake --jobs 1 -c1 --use-conda --printshellcmds  komutu ile dosyayı çalıştırdım ve hata aldım
# outpıt a tRNA_scan_result.txt dosyası ekledim ve IncompleteFilesException:
# The files below seem to be incomplete. If you are sure that certain files are not incomplete, mark them as complete with
#
#     snakemake --cleanup-metadata <filenames>
#
# To re-generate the files rerun your command with the --rerun-incomplete flag.
# Incomplete files:
# output/tRNA_scan_result.txt ne hatası aldım
# hatayı çözmek için önerdiği gibi snakemake --rerun-incomplete işlemin yapınca outputları aldım

