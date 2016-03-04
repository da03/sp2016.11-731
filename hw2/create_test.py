import sys
import string
import codecs
import nltk
from nltk.util import ngrams

def main(f_file_path, out_file_path):
    with open(f_file_path, 'r') as f:
        with open(out_file_path, 'w') as fout:
            for line in f:
                fout.write('0 '+line)

if __name__ == '__main__':
    if len(sys.argv) <> 3:
        print 'Usage: python %s <features-file> <output-file>' %sys.argv[0]
        sys.exit(1)
    f_file_path = sys.argv[1]
    out_file_path = sys.argv[2]
    main(f_file_path, out_file_path)
