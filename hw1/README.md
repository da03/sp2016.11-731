There are three Python programs here (`-h` for usage):

 - `./align` aligns words using Dice's coefficient.
 - `./check` checks for out-of-bounds alignment points.
 - `./grade` computes alignment error rate.

The commands are designed to work in a pipeline. For instance, this is a valid invocation:

    ./align -t 0.9 -n 1000 | ./check | ./grade -n 5


The `data/` directory contains a fragment of the German/English Europarl corpus.

 - `data/dev-test-train.de-en` is the German/English parallel data to be aligned. The first 150 sentences are for development; the next 150 is a blind set you will be evaluated on; and the remainder of the file is unannotated parallel data.

 - `data/dev.align` contains 150 manual alignments corresponding to the first 150 sentences of the parallel corpus. When you run `./check` these are used to compute the alignment error rate. You may use these in any way you choose. The notation `i-j` means the word at position *i* (0-indexed) in the German sentence is aligned to the word at position *j* in the English sentence; the notation `i?j` means they are "probably" aligned.

# Model:

I used IBM 2 as the basic model and trained it by EM algorithm. IBM 1 is used to initialize the parameters in IBM 1. In order to improve the results, I ran the model twice: first on english to german and then on german to english. Then the intersection of the two alignments are cacluated and I added them towards the union set until each word in each language has an alignment. A heuristic is used: the alignments closer to diagnal are considered to be added first.

# Usage:

```
python generate_t.py data/dev-test-train.de-en t-full
```

This will run the EM algorithm to learn IBM 1 and output the learned parameters to t-full.

```
python generate_t_p2.py t-full data/dev-test-train.de-en t2-full q2-full
```

This will run the EM algorithm to learn IBM 2 (the parameters are initialized by the IBM 1) and output the learned parameters to t2-full and q2-full.

```
python classify_p2.py t2-full q2-full data/dev-test-train.de-en output.txt.eg
```

The above command will do the inference and output the alignment results to `output.txt.eg`.

Then I run

```
python swap.py data/dev-test-train.de-en dev-test-train.en-de
```

to swap German and English. Then I ran the same steps as above to get alignments in another direction:

```
python generate_t.py dev-test-train.en-de t-full-swap && python generate_t_p2.py t-full-swap dev-test-train.en-de t2-full-swap q2-full-swap && python classify_p2.py t2-full-swap q2-full-swap dev-test-train.en-de output.txt.swap
```

Finally, I combined the two alignments together:

```
python improve.py data/dev-test-train.de-en output.txt.eg output.txt.swap output.txt
```
