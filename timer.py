class Timer:
    def __init__(self):
        self.second = 0
        self.running = False

    def reset(self):
        self.second = 0
        self.running = False

    def tic(self):
        if not self.running:
            return
        self.second += 1

    def time(self):
        return self.second

    def start(self):
        self.running = True

    def stop(self):
        self.running = False
