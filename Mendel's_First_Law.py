'''
Author : Sujit Mandal
Github: https://github.com/sujitmandal
Package   : https://pypi.org/project/images-into-array/
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
Facebook : https://www.facebook.com/sujit.mandal.33671748
Twitter : https://twitter.com/mandalsujit37
'''

def Mendelian_Inheritance(k,m,n):
    probability = (k * k + k * (2 * m + 2* n - 1) + m * (0.75 * m + n - 0.75)) / ((k + m + n - 1) * (k + m + n))

    roundup = round(probability, 5)
    print(roundup)


if __name__ =='__main__':
    Mendelian_Inheritance(15,18,20)