# Reference sequence variants (stable meaning)

* Full: primary assembly plus alt, decoy, and HLA contigs; needs alt-aware handling.
* Analysis set: alt contigs for alt-aware mapping, decoys included.
* No-alt: simplest for tools that do not handle alts.
* Masked: hard-masked regions; fewer artifacts, lost sequence. Record whether the Y PAR is masked.
* A RefSeq-named FASTA (NC_ accessions) needs renaming before mixing with UCSC-style files.
* Record the patch level with the build.
* Pangenome references: coordinates need a linear path; report on a linear reference.

Check the FASTA `.fai` to see which variant a file is. Use the reference directory in CLAUDE.md; list it before downloading, and note the FASTA name, index files, annotation, and chain files.
