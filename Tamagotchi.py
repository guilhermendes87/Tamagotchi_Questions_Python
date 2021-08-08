#Tamagotchi
#Guilherme Mendes


from random import randrange

class Pet(object):
    """Tamagotchi"""
    excitement_reduce = 3
    excitement_max = 10
    excitement_warning = 3
    food_reduce = 2
    food_max = 10
    food_warning = 3
    vocab = ['"Grrr..."','"Oi"']

    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.food = randrange(self.food_max)
        self.excitement = randrange(self.excitement_max)
        self.vocab = self.vocab[:]

    def __clock__tick(self):
        self.excitement -= 1
        self.food -= 1

    def mood(self):
        if self.food > self.food_warning and self.excitement > self.excitement_warning:
            return "Feliz!"
        elif self.food < self.food_warning:
            return "Com fome!"
        else:
            return "Chateado"

    def __str__(self):
        return "\n Eu sou "+ self.name +"." + "\nEu estou" + self.mood() +"."

    def teach(self, word):
        self.vocab.append(word)
        self.__clock__tick()

    def talk(self):
        print("Eu sou um(a)", self.animal_type, "e me chamo", self.name, ".", "E estou", self.mood(), "agora.\n")

        print(self.vocab[randrange(len(self.vocab))])

        self.__clock__tick()

    def feed(self):
        print("***nhac nhac nhac*** \nHummm. Obrigado")
        meal = randrange(0, self.food_max)
        self.food += meal

        if self.food < 0:
            self.food = 0
            print("Eu continuo faminto!")
        elif self.food >= self.food_max:
            self.food = self.food_max
            print("Estou satisfeito!")
        self.__clock__tick()

    def play(self):
        print("Uhuuul!")
        fun = randrange(0, self.excitement_max)
        self.excitement += fun
        if self.excitement < 0:
            self.excitement = 0
            print("Estou chateado!")
        elif self.excitement > self.excitement_max:
            self.excitement_max = self.excitement_max
            print("Estou muito feliz! ^^")
        self.__clock__tick()

def main():
    pet_name = input("Qual o nome você deseja colocar no seu bichinho?")
    pet_type = input("Qual é o tipo de bichinho que você deseja? (cachorro, gato, coelho, e etc...)")

    #Criando um novo bichinho
    my_pet = Pet(pet_name, pet_type)

    input("Olá! Meu nome é " + my_pet.name + " e sou novo por aqui!" + "\nPressione enter para continuar.")

    choice = None

    while choice != 0:
      print("""
      *** INTERAJA COM SEU BICHINHO ***

      1 - ALIMENTAR SEU BICHINHO
      2 - CONVERSAR COM SEU BICHINHO
      3 - ENSINAR AO SEU BICHINHO UMA NOVA PALAVRA
      4 - BRINCAR COM O SEU BICHINHO
      0 - QUIT
      
      """)

      choice = input("Qual opção deseja escolher? ")

      if choice == "0":
          print("Tchau... Até a próxima!")
      elif choice == "1":
          my_pet.feed()
      elif choice == "2":
          my_pet.talk()
      elif choice == "3":
          new_word = input("Qual é a nova palavra que você deseja ensinar para o seu bichinho?")
          my_pet.teach(new_word)
      elif choice == "4":
          my_pet.play()
      else:
          print("Desculpe, esta não é uma opção válida.")
      break

main()