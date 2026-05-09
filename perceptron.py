class Perceptron:
    entries = []
    weights = []

    def __init__(self, entries):
        self.entries = entries
    
    def classify(self, entry):
        result = 0

        for entry, weight in self.entries[:-1], self.weights[:-1]:
            result += entry*weight
        
        if result > 0: 
            return 1

        return 0

    def adjust_w(self):
        # for each instance we have a list of attributes

        #              x0 + x1 ... xn
        attributes = 1 + self.attributes

        # and also a list of weights that is the same for them all

        # w0 ... wn
        self.weights = [1 for _ in range(len(attributes))]

        failed = False

        for entry in self.entries:
            if entry[-1] != self.classify(entry):

                failed = True

        
        if failed: self.adjust_w()


    def show_weights(self):
        print(self.weights)
    

novo = Perceptron([10,20,30,40])

novo.show_weights()