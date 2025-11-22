import datetime


class Enos:
    def __doc__(self):
        return f"This is a class that holds personal information about Enos - a software engineer"
    def __init__(self, jina, miaka, jinsia):
        self.name = jina
        self.age = miaka
        self.gender = jinsia

    def skills(self):
        return  f'{self.name}["Python", "JavaScript", "C++"]'         
    def place (self, year):
        year=int(year)
        year_var = datetime.datetime.now().year
        if year > year_var:
            return f'{self.name} location will be unknown in the future, likely USA still'
        elif year > 2019:
            return f"{self.name} was in  USA"
        elif year == 2018:
            return f"{self.name} was in  Germany"
        else:
            return f"{self.name} was in Kenya"
    def interests(self, choice):
        if choice == "outdoors":
            return f'{self.name} likes ["soccer". "dancing", "art"]'
        else: 
            return f'{self.name} likes. ["writing", "film", "drawing"]'
