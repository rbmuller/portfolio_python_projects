#Algumas vezes quando lidamos com Herança, fica dificil fazer debugging. 
# Esta funcao ajuda a encontrar a qual Classe raiz o metodo esta associado  

def find_def_class(obj,meth_name):
    '''Parametros: Objeto, metodo
    retorna a Classe original do metodo'''
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty

