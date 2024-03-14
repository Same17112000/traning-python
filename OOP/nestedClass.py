class specification:
    def __init__(self):
        self.type = "High-Level"
        self.founded = "2000"
        
    def display(self):
            print("Type:", self.type)
            print("Founded:", self.founded)

class language:
    def __init__(self, spec):
        self.language = "PYTHON"
        self.lg = spec
    
    def show(self):
        print("Language:", self.language)


spec = specification()
out = language(spec)

lg = out.lg
lg.display()
