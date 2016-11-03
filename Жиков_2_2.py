import mmh3 as mur

def hash_trick(input_dict, bits):
    ret = {}
    for key in input_dict.keys():
        str = key + input_dict[key]
        hsh = mur.hash(str) % (2**bits)
        ret[key] = hsh
    return ret
        
print hash_trick({'a':'b', 'b':'d'}, 10)
