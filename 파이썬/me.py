class Me:
    def __init__(self, name, age):
        self.name = "지선"
        self.age = 28

    def introduce(self):
        return f"안녕하세요, 저는 {self.name}이고, 나이는 {self.age}살입니다."


me = Me("지선", 29)


print(me.introduce())