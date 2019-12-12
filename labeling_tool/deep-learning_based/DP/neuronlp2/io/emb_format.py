# runs in python 2.7
# embedding file should be in utf-8 encoding
# outfile will be in euc-kr encoding for further use 

import sys
import os
import importlib
importlib.reload(sys)
sys.setdefaultencoding('euc-kr')

def get_emb_dict(filename):
    word_emb_dict = dict()
    embedding = list()
    word = 'error'
    for line in open(filename, 'r'):
        line = line.decode('utf-8').strip()
        if line.endswith('containing:'):
            word = line.split()[0]
        elif len(line.split()) == 1:
            embedding.append(line)
        elif line.endswith(']'):
            continue
        elif len(line.split()) == 0:
            word_emb_dict[word] = ' '.join(embedding)
            embedding = list()
    return word_emb_dict

def save_dict_to_file(word_emb_dict, outfile):
    with open(outfile, 'w') as f:
        for word, embedding in list(word_emb_dict.items()):
            f.write('{} {}\n'.format(word, embedding.encode('euc-kr')))
    print(("file saved at: {}".format(outfile)))

if __name__ == "__main__":
    filename = sys.argv[1]
    outfile = os.path.join(os.path.dirname(filename), 'embedding_formatted.txt')
    print(("embedding file to format: {}".format(filename)))

    word_emb_dict = get_emb_dict(filename)
    save_dict_to_file(word_emb_dict, outfile)
