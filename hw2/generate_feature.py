import sys
import string
import codecs
def main(s_file_path, out_file_path):
    with codecs.open(s_file_path, encoding='utf-8', mode='r') as f:
        for line in f:
            h1,h2,e = line.strip().split('|||')
            print h1
            break
if __name__ == '__main__':
    if len(sys.argv) <> 3:
        print 'Usage: python %s <sentence-file> <output-file>' %sys.argv[0]
        sys.exit(1)
    s_file_path = sys.argv[1]
    out_file_path = sys.argv[2]
    main(s_file_path, out_file_path)
