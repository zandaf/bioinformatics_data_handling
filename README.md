# RNA-seq Data Engineering Pipeline: VCaP Cancer Dataset

## Project Overview

This project explores the processing and quality control of real RNA-seq sequencing data using a public dataset from NCBI GEO/SRA.

The objective is to build a reproducible bioinformatics workflow, starting from raw sequencing data acquisition and progressing towards downstream transcriptomic analysis.

## Dataset

- **Dataset:** GSE256370
- **Organism:** Homo sapiens
- **Research context:** VCaP cancer cell model
- **Data type:** RNA sequencing (RNA-seq)
- **Source:** NCBI GEO / SRA
- **Sequencing:** Paired-end reads
- **Planned samples:** 12 sequencing runs

## Technologies

- Galaxy Europe
- NCBI GEO / SRA
- SRA Toolkit (`fasterq-dump`)
- FastQC
- Python
- Pandas

## Workflow

1. Dataset identification and biological metadata investigation.
2. Experimental group and sample metadata inspection.
3. Raw sequencing data retrieval from SRA.
4. FASTQ extraction using `fasterq-dump`.
5. Paired-end read organization.
6. Sequencing quality assessment using FastQC.

## Current Progress

- Dataset selected and investigated.
- First sequencing sample downloaded and extracted.
- FastQC quality-control jobs submitted for forward and reverse reads.

## Future Work

- Complete quality control for all 12 samples.
- Adapter and low-quality read trimming if necessary.
- Alignment or pseudo-alignment.
- Gene-level quantification.
- Differential gene expression analysis.
- Downstream statistical analysis and visualization.

## Reproducibility

Raw sequencing files are not stored in this repository because of their large size. Dataset accession numbers and processing documentation will be provided to allow retrieval and reproduction of the workflow.

**Project status:** In progress — initial data acquisition and quality control.