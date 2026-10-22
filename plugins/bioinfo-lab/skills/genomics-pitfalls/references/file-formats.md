# Common file formats

| Format | Holds | Watch for |
|---|---|---|
| FASTA | Sequences | Contig names must match the annotation and variants |
| FASTQ | Reads with Phred quality scores, 4 lines per read | Paired files must stay in the same read order |
| SAM, BAM, CRAM | Alignments | CRAM needs the exact reference; check `@SQ` lines for the build |
| VCF, BCF | Variants, genotypes per sample | 1-based; REF/ALT must be normalized; multi-allelic sites; header lists contigs |
| gVCF | Variants plus reference blocks | Needed to merge cohorts correctly |
| BED | Intervals | 0-based, half-open; at least 3 columns |
| GFF3, GTF | Gene annotation | 1-based, closed; GTF and GFF3 attribute syntax differ |
| bgzip + tabix index | Compressed, indexed text | gzip is not bgzip; indexing needs bgzip and sorted input |
| PLINK `.bed/.bim/.fam` | Binary genotypes | The `.bed` here is not a BED interval file; allele order in `.bim` |
| PLINK 2 `.pgen/.pvar/.psam` | Genotypes, dosages | Different from PLINK 1 files |
| Numeric genotype matrix (0/1/2, HapMap) | Marker calls for plants and animals | State coded allele, missing code, and marker order |
| bedGraph, bigWig | Signal tracks | Build and coordinate base |
| BrAPI JSON, MIAPPE sheets | Breeding trial data and metadata | Keep IDs identical to the genotype files |
