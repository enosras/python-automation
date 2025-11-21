class Enos:
    def __init__(self, jina, miaka, jinsia):
        self.name = jina
        self.age = miaka
        self.gender = jinsia

    def skills(self):
        return  f'{self.name}["Python", "JavaScript", "C++"]'         
    def place (self, year):
        if year  > 2019:
            return "USA"
        elif year < 2018:
            return f"{self.name} was in  Germany"
        else:
            return f"{self.name} was in Kenya"
    def interests(self, choice):
        if choice == "outdoors":
            return f'{self.name} likes ["soccer". "dancing", "art"]'
        else: 
            return f'{self.name} likes. ["writing", "film", "drawing"]'
