import sys

def split_token_pos(pos_tagged):
    tagged_list = pos_tagged.split('|')
    token = list()
    pos = list()
    for tagged in tagged_list:
        if '//' in tagged:     # //SP
            tok = '/'
            tag = tagged.split('/')[-1]
        else:
            tok, tag = tagged.split('/')
        token.append(tok)
        pos.append(tag)
    #token = '+'.join(token)
    token = ''.join(token)
    pos = '+'.join(pos)
    return token, pos

if __name__ == "__main__":
    in_file = sys.argv[1]
    out_file = sys.argv[2]

    print(("in_file: ", in_file))
    print(("out_file: ", out_file))

    with open(in_file, 'r') as in_f:
        with open(out_file, 'w') as out_f:
            for line in in_f:
                line = line.strip()
                if len(line) == 0:
                    out_f.write('\n')
                    continue
                if line.startswith(';'):
                    continue
                elements = line.split()
                try:
                    idx, head, deprel, _, pos_tagged = elements
                except:
                    # error in original file: hand annotated postag contains blank letter
                    idx, head, deprel, _, _, pos_tagged = elements
                #token, pos = split_token_pos(pos_tagged)
                #line = "{}\t{}\t_\t_\t{}\t_\t{}\t{}\t_\t_".format(idx, token, pos, head, deprel)
                _, pos = split_token_pos(pos_tagged)
                line = "{}\t{}\t_\t_\t{}\t_\t{}\t{}\t_\t_".format(idx, pos_tagged, pos, head, deprel)
                out_f.write(line+'\n')

    print("file processing finished")