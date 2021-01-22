import numpy as np
import dionysus as d
from itertools import chain
from itertools import combinations

def powerset(iterable, cutoff):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(cutoff+1))

def read_complex(face_list, order):
    h=d.Filtration()
    cutoff=order+2
    for face in face_list:
        temp=set(np.unique(face))
        for j in powerset(temp, cutoff):
            if set(j)==set():
                continue
            h.append(d.Simplex(j, 1))
    h.sort()
    
    return h

class Homology:
    h=d.Filtration()
    order=0

    def init(self, face_list, order):
        self.h=read_complex(face_list, order)
        self.order=order

    def bettis(self):
        m=d.homology_persistence(self.h)
        dgms=d.init_diagrams(m, self.h)
        betti=list(len(dgms[i]) for i in range(len(dgms)))
        betti_len=len(betti)
        if(betti_len<self.order+2):
            for _ in range(self.order+2-betti_len):
                betti.append(0)
        return np.array(betti)[:self.order+1]