s = 'TTCCCAACAATCCCATTACAGCTCACACCGCACTAAGGTGTGCGGAAATCGCGCGCTCAAGCCATGGTATCGACAAACGCCTCCCGGATTGTCAATCGCCGTAATCCTTATTTATCCGATGTGACTACCGATGGATCCACCTCAGTGGTTGACAATAACTTCCTATGCGTGCCTATCCCCCCGAGCACACGATGACACCATCAGTATGACTAGCTAGAATAACACCTTTGGGCTCGTACGCCTGCGCCCAGGCAGCGTTTCTATTACAGAGGTAGCTATGACCTACTCACACATTGTAAGTGGTCTTCCCCAGTATTGTATAGTCTGACAGTTTCGTGGATGGGTATGTGAGCGACTGCGAGATGGCCCGAAATTTCGGGACTGAGCATTATGCGTCCTCAGCTTAATGGTCAATAATCTAATCGGATCGGCTATCGTACGCTACCACTGCGATTTTTAAATAGTCACTGAGTCGGTTACTTCTGCTCCCGTATGTTGGGACTGTGCCCTAACCTTTACCTCGTGCGTAATTTATTAACAGTGCCCCGTCAGTTTGGAACAGCCAAATTCACGAACGACGCTCTCGATCGTTGAATCTTGCGTATGAGGTTTCCGTGCGTTCTGACCGGTTCTTGACCGCCCCGGATGTACCGACGAGGGTCAGCCGTATCGAATTAATCGATTAGTCGATCCCATGGCGGTTGGAATGTCCCTTCGGGTGTCGGCACATGGGCTCGAGTTCTTAGGGCAGTATACGCCTTGCCCGTATTCAGTATTCTGTGGTCGAGATAAGACTAGTGAGTTCTGTCATCTTCTACAGGTGCGCGCGCACAGCTCTCGTCTAGAGAGCAGCACGGCTGACGCGGCAATTGTTTCCTGGATTAGCCTATGACTAAACTGAACACCAAGATATTCGATACACAGCATTGCGCGTGGGAAATCGGCGAGGATCTTTTA'

'''
Author : Sujit Mandal
Github: https://github.com/sujitmandal
Package   : https://pypi.org/project/images-into-array/
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
Facebook : https://www.facebook.com/sujit.mandal.33671748
Twitter : https://twitter.com/mandalsujit37
'''

def DNA(dna):
    def string(temp):
        temp_str = ''

        for j in temp:
            temp_str += j
        return(temp_str)

    a = []
    c = []
    g = []
    t = []

    for i in dna:
        if i == 'A':
            a.append(i)
        elif i == 'C':
            c.append(i)
        elif i == 'G':
            g.append(i)
        elif i == 'T':
            t.append(i)


    A = string(a)
    C = string(c)
    G = string(g)
    T = string(t)

    length_a = len(A)
    length_c = len(C)
    length_g = len(G)
    length_t = len(T)

    print(length_a, length_c, length_g,length_t)
    
if __name__ == "__main__":
    DNA(s)

