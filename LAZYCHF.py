class Lazy():
    def __init__(self, iteration):
        self.iteration = iteration
    def check_lazines(self):
        for i in range(self.iteration):
            m,x,d = map(int,input().split())
            time = m*x
            upper_bound = m+d
            print(time,upper_bound)
iteration = Lazy(iteration=3)
iteration.check_lazines()