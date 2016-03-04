import sys
import string
import codecs
import nltk
from nltk.util import ngrams

def main(s_file_path, out_file_path):
    with codecs.open(s_file_path, encoding='utf-8', mode='r') as f:
        with open(out_file_path, 'w') as fout:
            #idx=0
            for line in f:
                #print idx
                #idx = idx+1
                h1,h2,e = line.strip().split('|||')
                features = calc_features(h1,e)+calc_features(h2,e)
                #print features
                #print len(features)
                fout.write(' '.join(['%d:%f'%(i+1,features[i]) for i in range(len(features))])+'\n')

def calc_features(h,e):
    htokens = nltk.word_tokenize(h)
    etokens = nltk.word_tokenize(e)
    htagged = nltk.pos_tag(htokens)
    etagged = nltk.pos_tag(etokens)
    features = calc_ngram(htokens,etokens)
    features = features+calc_ngram_pos(htagged,etagged)
    return features

def calc_ngram(htokens,etokens):
    features = []
    for n in range(1,5):
        hgrams = nltk.FreqDist(ngrams(htokens,n))
        egrams = nltk.FreqDist(ngrams(etokens,n))
        prec = 0
        num = 0
        for k in hgrams:
            if k in egrams:
                prec = prec + hgrams[k]
            num = num + hgrams[k]
        if num > 0:
            prec = float(prec) / num
        features.append(prec)
        recall = 0
        num = 0
        for k in egrams:
            if k in hgrams:
                recall = recall + egrams[k]
            num = num + egrams[k]
        if num > 0:
            recall = float(recall) / num
        features.append(recall)
        features.append(calc_f1(prec,recall))
    return features

def calc_f1(prec,recall):
    if prec > 0 and recall > 0:
        return 2.0/(1.0/prec+1.0/recall)
    else:
        return 0.0

def calc_ngram_pos(hpos,epos):
    htokens = [item[1] for item in hpos]
    etokens = [item[1] for item in epos]
    return calc_ngram(htokens,etokens)

if __name__ == '__main__':
    if len(sys.argv) <> 3:
        print 'Usage: python %s <sentence-file> <output-file>' %sys.argv[0]
        sys.exit(1)
    s_file_path = sys.argv[1]
    out_file_path = sys.argv[2]
    main(s_file_path, out_file_path)
