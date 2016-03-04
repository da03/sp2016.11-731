import sys
import string
import codecs
import nltk
from nltk.util import ngrams

def main(f_file_path, l_file_path, out_file_path):
    with open(f_file_path, 'r') as f:
        with open(l_file_path, 'r') as fl:
            with open(out_file_path, 'w') as fout:
                for line in fl:
                    line2 = f.readline()
                    if line.strip() != '0':
                        fout.write(line.strip()+' '+line2)

if __name__ == '__main__':
    if len(sys.argv) <> 4:
        print 'Usage: python %s <features-file> <lable-file> <output-file>' %sys.argv[0]
        sys.exit(1)
    f_file_path = sys.argv[1]
    l_file_path = sys.argv[2]
    out_file_path = sys.argv[3]
    main(f_file_path, l_file_path, out_file_path)
