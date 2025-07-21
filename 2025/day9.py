ram_child1 = 'sam'
ram_child2 = 'sita'

sam_child1 = 'navin'
def child(*child,**prarent): #args parameter,keyword parameter
    print(*child)
    print(prarent)
child(ram_child1, ram_child2, prarent='ram')
child(sam_child1, prarent='sam')

#Reture keyword
a=23
b=40

def add():
    return a+b
    print('hello')

    c = add()
    print(c)
