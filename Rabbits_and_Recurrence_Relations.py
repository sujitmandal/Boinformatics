'''
Author : Sujit Mandal
Github: https://github.com/sujitmandal
Package   : https://pypi.org/project/images-into-array/
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
Facebook : https://www.facebook.com/sujit.mandal.33671748
Twitter : https://twitter.com/mandalsujit37
'''

def rabbit(n, k):
    if n == 1:
        return(1)
    elif n == 2:
        return(k)

    oneGen = rabbit((n - 1), k)
    twoGen = rabbit((n - 2), k)

    if n <= 4:
        add = (oneGen + twoGen)
        return(add)

    sequence = (oneGen + (twoGen * k))
    return(sequence)


if __name__ == "__main__":
    a = rabbit(33, 3)
    print(a) 
