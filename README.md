# Evaluation-Query-refinement-type-aware-approach
# Overview 
This readme only includes altered or new folders and files in the ReQue. 
To run this method, clone the [ReQue](https://github.com/fani-lab/ReQue) and execute the ReQue based on its readme document. After installing ReQue follow these steps:

**Add following folders to the ReQue:**

*Source Folder:*

 [ds/trec2009/source](https://github.com/ZahraTaherikhonakdar/Eval-QR-type-aware-approach/tree/main/ds/trec2009mq/source): this folder Contains [TREC2009 Million Query](https://trec.nist.gov/data/million.query09.html) data set, the relevance judgment and query classes (query types).
 
 [ds/trec2009/lucene-index-trec2009mq](https://github.com/ZahraTaherikhonakdar/Eval-QR-type-aware-approach/tree/main/ds/trec2009mq/source): this folder includes clueweb indexes.
 
```
+---ds
|   +---trec2009mq
|   |   +---lucene-index-trec2009mq
|   |   +---source  
|   |   |   |   09.mq.topics.20001-60000 
|   |   |   |   prels.20001-60000
|   |   |   |   queryclasses 

```

*Codebase:*

Execute following files respectively:

 - preprocess_trec2009/preprocess_trec2009.py
 - qe/main.py 
 - stat/stat.py
 
[preprocess_trec2009/](https://github.com/ZahraTaherikhonakdar/Eval-QR-type-aware-approach/tree/main/preprocess_trec2009): Running [preprocess_trec2009.py](https://github.com/ZahraTaherikhonakdar/Eval-QR-type-aware-approach) would results in preprocessed input data set and relevance judgment. The out put would be placed in [ds/trec2009/output](https://github.com/ZahraTaherikhonakdar/Eval-QR-type-aware-approach/tree/main/ds/trec2009mq/output).

```
+---preprocess_trec2009
|   |   preprocess_trec2009.py
```
[qe/cmn/param.py](https://github.com/ZahraTaherikhonakdar/Eval-QR-type-aware-approach/blob/main/qe/cmn/param.py): to run the ReQue for the Trec2009mq, change the folder address for antique in param.py files to the following address:
```
'index': '../ds/trec2009mq/lucene-index-trec2009mq',
'topics': '../ds/trec2009mq/output/topics_trec',
'qrels':'../ds/trec2009mq/output/qrels_trec',

```

[stat/stat.py](https://github.com/ZahraTaherikhonakdar/Eval-QR-type-aware-approach/tree/main/stat): by running this files matrix consist of expanders and query type and also heat map of the matrix would be built.

```
+---stat
|   |   stat.py
```
**Target Folders:**
The target folders are the outputs for the preprocessed and stat and ReQue expanders.

[ds/trec2009/output](https://github.com/ZahraTaherikhonakdar/Eval-QR-type-aware-approach/tree/main/ds/trec2009mq/output): the results of preprocessing of input queries and the relevance judgment would be in this folder after running [preprocess_trec2009.py](https://github.com/ZahraTaherikhonakdar/Eval-QR-type-aware-approach/tree/main/preprocess_trec2009).

```
+---ds
|   +---trec2009mq
|   |   +---output 
|   |   |   |   topics_trec 
|   |   |   |   qrels_trec
```

[qe/output/trec2009mq](https://github.com/ZahraTaherikhonakdar/Eval-QR-type-aware-approach/tree/main/qe/output/trec2009mq): this folder includes ReQue results in txt files and also the [stat](https://github.com/ZahraTaherikhonakdar/Eval-QR-type-aware-approach/tree/main/qe/output/trec2009mq/stat) results in png format.

```
+---qe
|   +---output
|   |   +---trec2009mq
|   |   |   |   topics.antique.glove.topn3.bm25.txt
|   |   |   |   topics.antique.bm25.map.dataset.csv
|   |   |   |   .....
|   |   +---stat
|   |   |   |   heatmap.png
|   |   |   |   matrix_result.csv

```
