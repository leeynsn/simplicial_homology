from sys import path
path.insert(0, '../library/')
import homology

face_list=[[0, 1], [1, 2], [2, 0], [2, 3]] # vectices: <0>, <1>, <2>, <3>  &  edges: <0, 1>, <1, 2>, <2, 0>, <2, 3>
hom=homology.Homology()
hom.init(face_list, 1)
print(hom.bettis())