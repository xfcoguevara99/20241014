#coding:utf-8
def scrip0():
    vA = [] # Vetor vazio e de tamanho 0
    vB = [ None ] * 5 # Vetor vazio de tamanho 5
    vC = [1 , 3.4 , "A" , " IFSC ",3.4 ] #vetor de
        # tamanho 5 e com tipos diferentes
    print ( vA ) # Imprime o vetor vA
    print ( vB ) # Imprime o vetor vB
    print ( vC ) # Imprime o vetor vC
    print("Numero de vezes que aparece 3.4: ", vC.count(3.4))
    print("Posição do valor 3.4: ", vC.index(3.4))



def scrip1(): #tuplas
    lista1 = ["rampa","descida",11.34]
    tupla1 = (1,1.34,"A","IFSC") 
    print(lista1)
    lista1[1] = "subida"
    print("Lista modificada : ",end = " ")
    print(lista1)

def scrip2():
    vC = [1,3.4,"A","IFSC"]
    for i in vC:
        print(type(i))


if __name__ == "__main__":
    #scrip0()
    #scrip1()
    scrip2()


