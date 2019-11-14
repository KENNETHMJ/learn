#!/usr/bin/env python
# -*- coding:utf-8 -*-

#illumina
#fastq->QC->read alignment->sort->reduplication->GATK HaplotypeCaller

#step1: $ /path_to_fastqc/FASTQC/fastqc /path_to_fq/*.fq -o fastqc_out_dir/

#step2: $ bwa index hunman.fasta
#including file:ucsc.hg19.fasta ucsc.hg19.dict ucsc.hg19.fasta.amb ucsc.hg19.fasta.ann \
#ucsc.hg19.fasta.bwt ucsc.hg19.fasta.fai ucsc.hg19.fasta.fai.fai ucsc.hg19.fasta.pac ucsc.hg19.fasta.sa

#$ bwa mem -t 4 -R '@RG\tID:foo_lane\tPL:illumina\tLB:library\tSM:sample_name' \
# /path/to/human.fasta read_1.fq.gz read_2.fq.gz > sample_name.sam


#step3:$ samtools sort sample_name.bam sample_name.sorted

# #step4:
# $ java -jar path to/picard.jar MarkDuplicates \
#   I=sample_name.sorted.bam \
#   O=sample_name.sorted.markdup.bam \
#   M=sample_name.markdup_metrics.txt

# $ samtools index sample_name.sorted.markdup.bam

#step5:
#$ java -jar /path/to/GenomeAnalysisTK.jar \
#  -T HaplotypeCaller \
#  -R /path/to/human.fasta \
#  -I sample_name.sorted.markdup.bam \
#  -stand_call_conf 50 \
#  -o sample_name.HC.vcf
