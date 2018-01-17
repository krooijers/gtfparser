# GTFParser

Does what is says on the tin... it parses GTF (GFFv2) files...

Tries to do it fast as well...


## Caution

> You probably don't want to use this!
> Instead, you're probably better off with HTSeq's GTF Parser, or BioPython, or
> in fact anything more tested...!

[HTSeq](https://htseq.readthedocs.io/)  
[BioPython](http://biopython.org/wiki/GFF_Parsing)  


## Installation

```bash
pip install git+https://github.com/krooijers/gtfparser
```


## Use

```python
>>> from gtfparser import GTFParser

>>> fn = "gencode.v26lift37.basic.annotation.gtf"
>>> fn = "/data/zfs/references/human/hg19/transcriptome/gencode_v26/gencode.v26lift37.basic.annotation.gtf"

>>> gtf = GTFParser(fn)

>>> gtfiter = iter(gtf)
>>> gf = next(gtfiter)

>>> gf.iv
GenomicInterval(chrom='chr1', start=11868, end=14409, strand='+')
>>> gf.iv.end > gf.iv.start
True
>>> gf.feature
'gene'
>>> gf.attr
{'gene_type': 'transcribed_unprocessed_pseudogene', 'gene_name': 'DDX11L1', 'havana_gene': 'OTTHUMG00000000961.2_2', 'level': '2', 'remap_status': 'full_contig', 'gene_id': 'ENSG00000223972.5_2', 'remap_target_status': 'overlap', 'remap_num_mappings': '1'}
>>> gf.source
'HAVANA'

>>> print(gf)
GenomicFeature(feature='transcript', source='HAVANA', iv=GenomicInterval(chrom='chr1', start=11868, end=14409, strand='+'), score='.', frame='.', attrstr='gene_id "ENSG00000223972.5_2"; transcript_id "ENST00000456328.2_1"; gene_type "transcribed_unprocessed_pseudogene"; gene_name "DDX11L1"; transcript_type "processed_transcript"; transcript_name "DDX11L1-002"; level 2; transcript_support_level 1; tag "basic"; havana_gene "OTTHUMG00000000961.2_2"; havana_transcript "OTTHUMT00000362751.1_1"; remap_num_mappings 1; remap_status "full_contig"; remap_target_status "overlap";\n')

# let's have some fun while we're at it:
>>> from collections import Counter

>>> exoncounter = Counter()

>>> for exon in filter(lambda gf: gf.feature == "exon", gtfiter):
...     assert exon.feature == "exon"
...     assert "transcript_id" in exon.attr
...     tid = exon.attr["transcript_id"]
...     exoncounter[tid] += 1

>>> print(exoncounter.most_common(15))
[('ENST00000589042.5_3', 363), ('ENST00000591111.5_3', 313), ('ENST00000342992.10_3', 312), ('ENST00000615779.5_1', 312), ('ENST00000342175.11_1', 191), ('ENST00000359218.10_1', 191), ('ENST00000460472.6_3', 191), ('ENST00000618972.4_2', 183), ('ENST00000397345.7_1', 182), ('ENST00000427231.6_1', 182), ('ENST00000603639.5_1', 180), ('ENST00000604864.5_1', 180), ('ENST00000454784.8_2', 172), ('ENST00000409198.5_2', 150), ('ENST00000172853.14_2', 149)]

```

No joke (it's TTN):
```bash
grep "ENST00000589042.5_3" gencode.v26lift37.basic.annotation.gtf | awk '$3 == "exon"' | wc -l
```
```text
363
```

## See also

[StepVector](https://github.com/krooijers/stepvector), a package to handle data
or features spanning (genomic) ranges efficiently.


## Feedback and Legal

No warranty whatsoever.

Feedback, bug reports and fixes (in the form of well-formatted pull requests)
are much appreciated.
