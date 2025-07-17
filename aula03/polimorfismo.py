# Trabalhando com orientação a objetos e polimorfismo

class Animal():
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return 'Au Au'


class Gato(Animal):
    def fazer_som(self):
        return 'Miau'


# usando o polimorfismo
def fazer_animal_falar(animal: Animal):
    print(animal.fazer_som())

# criando os objetos
cachorro = Cachorro()
gato = Gato()

# chamando o metodo de cada animal de forma polimorfica
fazer_animal_falar(cachorro)
fazer_animal_falar(gato)