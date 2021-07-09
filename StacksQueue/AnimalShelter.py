from Queue import Queue, Node

class Animal:
    def __init__(self, type, number):

        if type != "cat" and type != "dog":
            raise TypeError

        self.type = type #"cat" or "dog"
        self.number = number
    
    def __str__(self):
        return self.type + str(self.number)

class AnimalShelter:
    def __init__(self):
        self.catQueue = Queue()
        self.dogQueue = Queue()
        self.anyQueue = Queue()

    def enqueue(self, animal):
        self.anyQueue.add(Node(animal))

        if animal.type == "cat":
            self.catQueue.add(Node(animal))
        else: #animal.type == "dog"
            self.dogQueue.add(Node(animal))

    def dequeueAny(self):
        animalAnyPeek = self.anyQueue.peek()
        self.anyQueue.remove()
        if animalAnyPeek.type == "cat":
            self.catQueue.remove()
        else: #animal.type == "dog"
            self.dogQueue.remove()
        
        return animalAnyPeek
    
    def dequeueDog(self):
        dogPeek = self.dogQueue.peek()
        self.dogQueue.remove()

        if self.anyQueue.peek().type == "dog":
            self.anyQueue.remove()
            return dogPeek
        
        #peek of anyQueue is not dog, we have to find the first dog of anyQueue and return it
        #since we can only use the interface of Queues, we need to use tmp queue adding every element from anyQueue but the first dog found
        tmpQueue = Queue()
        while not self.anyQueue.isEmpty():
            animalAnyPeek = self.anyQueue.peek()
            if animalAnyPeek.type == "dog" and animalAnyPeek.number == dogPeek.number:
                #we found the dog to remove from anyQueue, so we don't add it to temporal queue
                self.anyQueue.remove()
            else:
                #it's not the dog to remove, so we add to temporal queue
                tmpQueue.add(Node(Animal(animalAnyPeek.type, animalAnyPeek.number)))
                self.anyQueue.remove()
        
        #Now we have to put every element of tmpQueue to original anyQueue
        while not tmpQueue.isEmpty():
            animalTmpPeek = tmpQueue.peek()
            self.anyQueue.add(Node(Animal(animalTmpPeek.type, animalTmpPeek.number)))
            tmpQueue.remove()

    def dequeueCat(self):
        catPeek = self.catQueue.peek()
        self.catQueue.remove()

        if self.anyQueue.peek().type == "cat":
            self.anyQueue.remove()
            return catPeek
        
        #peek of anyQueue is not cat, we have to find the first cat of anyQueue and return it
        #since we can only use the interface of Queues, we need to use tmp queue adding every element from anyQueue but the first cat found
        tmpQueue = Queue()
        while not self.anyQueue.isEmpty():
            animalAnyPeek = self.anyQueue.peek()
            if animalAnyPeek.type == "cat" and animalAnyPeek.number == catPeek.number:
                #we found the cat to remove from anyQueue, so we don't add it to temporal queue
                self.anyQueue.remove()
            else:
                #it's not the cat to remove, so we add to temporal queue
                tmpQueue.add(Node(Animal(animalAnyPeek.type, animalAnyPeek.number)))
                self.anyQueue.remove()
        
        #Now we have to put every element of tmpQueue to original anyQueue
        while not tmpQueue.isEmpty():
            animalTmpPeek = tmpQueue.peek()
            self.anyQueue.add(Node(Animal(animalTmpPeek.type, animalTmpPeek.number)))
            tmpQueue.remove()
    
    def print(self):
        print("Cat Queue: ")
        self.catQueue.print()
        print("Dog Queue: ")
        self.dogQueue.print()
        print("Any Queue: ")
        self.anyQueue.print()

#tests
cat1 = Animal("cat", 1)
cat2 = Animal("cat", 2)
cat3 = Animal("cat", 3)

dog1 = Animal("dog", 1)
dog2 = Animal("dog", 2)

shelter = AnimalShelter()
shelter.enqueue(cat1)
shelter.enqueue(dog1)
shelter.enqueue(dog2)
shelter.enqueue(cat2)
shelter.enqueue(cat3)
shelter.print()

print("Dequeuing a Dog...")
shelter.dequeueDog() #We want to dequeue the first dog, which is the second element of anyQueue
shelter.print()

print("\nDequeuing Any...")
shelter.dequeueAny() #In this case we dequeue current first animal in anyQue which is cat1
shelter.print()

print("\nDequeuing Any...")
shelter.dequeueAny() #In this case we dequeue current first animal in anyQueue which is dog2
shelter.print()

print("\nDequeuing a Cat...")
shelter.dequeueCat() #Dequeue cat2 and we are left with just cat3
shelter.print()


