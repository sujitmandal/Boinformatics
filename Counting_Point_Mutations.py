s = 'AGTCACGTGCATTACGGATGGCAGACCCATCTGCAGAAATGTATTCTTTGTTAGGCTGTGACAGAGTAGTCTGCCTACTCTAATACTCTTTCCTCCAAGCCTTGGGGACCCTGGAGAGTCAGTATTCTTAATTGAGTGACGGTTAGTCTTTAACCAGTCTTGTGACAGTCACCCCGTCTGATGGCAATCGGGTTCTAACAAATGGAGATCACTCTCAACGCCTTCTGGTCAGTCTGATTTCGAGCAGGCAGCGATAAATCGGCGGTAGGCATTTACAGAGAAGGTTAGGCGAACTCACGTGGATCATGGTGCCCGCCACTAGTACACGCCTGAAGATTTTGCGTTAATTAGACAGCAACCTACTGATGGAATCTGGTCAGTGAACTAGAGTGGGCCGTCAGTTGAAAAGCCATAGGCGACGCCGCTCCAGCTCGAAGCTAGCTCCGGGCTATGTAACCAAATAGCATGTAAAATCAAGTTGATCGGAACGCTCCATGCATACTCTCATCTGCCAATATCAGGCCACTTAACAATCGACGTATACAAGACAGCCTTGACTTTTGAAGCACGAATCTGCCCTACAACAGGTCGTATATAAGAAGCGCACGCGATTTTGTTTATTGGGTCATCCTGCGTCCTGGCGAGCCGAGTTTGATATGTTCGGTTGGATGAAGGTTGCTCCGGCGTATTTAGAGTCGTAGCTCCGTTCGTATCTGTCTCTGCCAGTAGTTGCGATACAATTGACACTTTGGTATAGCCACCTGGGTTTGATGCGAGGTAACGCTTCGCTTTCTGTAATCCCACTATGGGTCCTTGACATGACGTGCACATCAATTCTCCGTTACCCAGATTCACCAGGCGCGCGCAATTGGGCATCCTTCGGCCTGGTGCGGTAGGCACGTCTGACGGGCGGAGTTTCCGCTAGTGTCACGGACTGATTATGTGGGCGTAAGCATCCGGC'
t = 'AGCGGCGTGTCAGATGTAAGCCACACCCTCAAGCTCGCAGCGATTTTTGGGTAACCCTGCCTATACTCATCCTCCAAGATACCTCTTGGTGACTCAAACCTTTGAGCATGGTGGACAGGCCACCTTTTTATTTAAGCAATGTATTGCCTACAACCTCACATTTGGAGGCAATGTCGTATGATGGCACTCGTCTTAGAAATGCGGGAGCGCAAGCTCAGCACCGTCTGGTCTTCCCTATATTCAGCAGTTGGTAAGAGGTCGTGTCTCTGCATAAAAAAACCAGGATCCTGCCAATCTCGTCGCCGCCGACTCAGGCTCCCGGCGACCGCCGGGACCTTTTATGCTAGTCCGATGGTTACTTGCTTAGTCAACCTTGGTACGTTACTTGTGTTGGTCCTTACACTTAAACGGGTAGGTGACCGGTGTGGTGGTCGAAGTAGTTGCCGGGATCGGTACTACTCTCGAGCTTACTCGCAAGTTAATCGGGACGCTCCGTAGTTGGCCTGTTCGGCCACCTGCACGAAACCTTCCTATCAGGTGGTAGAACACAGCCACGGATCTTTGCGCGCGTATCAGCGCTGCGAGGGTGCCCGACTAACTCAGACACACTATGTAGACAGATAGTATGAGATCCGAGTTGCCGTTGAGCCTAGGCGTAGCATCTCACGGTCAACATTGTTCCGCCTTATTTACAAGCCCGTCCCAGTTTCCCTCTAGCTGCTACAGAGCGGGTGGCGCATTTGATACCTAGGTGTGGACCCCTGCCTAAGTTACGAGCTATCTCTCCGCTTAATGGAGACCTAATATGTATCCTAGGTTGGACGCGGAAATCAATTCGCCAGTAAACACGATGACTAGGCGCCCTCAACTGACCGTACTAGGGCAGTGAGAGGTAATCATTGAGGGAGTCCTTAGATTATGCTATTCGGATGCGTTTTGCGTATTTTTATGGGGATCCGGT'

'''
Author : Sujit Mandal
Github: https://github.com/sujitmandal
Package   : https://pypi.org/project/images-into-array/
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
Facebook : https://www.facebook.com/sujit.mandal.33671748
Twitter : https://twitter.com/mandalsujit37
'''

def Hamming_distance(x, y):
    n = len(x)
    temp = []
    for i in range(n):
        if x[i] != y[i]:
            temp.append(x[i])

    print(temp)
    print(len(temp))

def Not_Hamming_distance(x, y):
    n = len(x)
    temp = []
    for i in range(n):
        if x[i] == y[i]:
            temp.append(x[i])

    print(temp)
    print(len(temp))

if __name__ == "__main__":
    Hamming_distance(s, t)
    Not_Hamming_distance(s,t)
