class language:
    def __init__(self):
        self.language = "PYTHON"
        self.lg = self.specification()
    
    def show(self):
        print("Language:", self.language)

    class specification:
        def __init__(self) -> None:
            self.type = "High-Level"
            self.founded = "2000"
        
        def display(self):
            print("Type:", self.type)
            print("Founded:", self.founded)

out = language()
out.show()

out_spec = out.lg
