class People:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def change_age(self, new_age):
        if isinstance(new_age, int) and 1 <= new_age <= 100:
            self.age = new_age
        else:
            print("некорректное значение для возраста")

    def full_name(self):
        return f"{self.surname} {self.name}"

    def full_info(self):
        return f"Человек: {self.surname} {self.name} и ему {self.age} лет"


# Совет: не забывайте, вы можете добавлять в список и удалять из него любых людей, это просто пример!
peoples = [
    People("Иван", "Уткин", 27),
    People("Алена", "Перова", 32),
    People("Василий", "Быстров", 55),
    People("Ольга", "Подгорная", 32),
]

yangest = peoples[0]
for man in peoples:
    if man.age < yangest.age:
        yangest = man
print(f"Младший:\n{yangest.name} {yangest.surname}")

# TODO-2: найдите всех одногодок и выведите их Фамилии и Имена
#  Примечание: Если одногодок нет, выведите сообщение "одногодок нет"
eq_age_people = []
for man in peoples:
    eq_age_people = [m for m in peoples if m.age == man.age]
    if len(eq_age_people) == 1:
        eq_age_people.clear()

if len(eq_age_people) == 0:
    print("Одногодков нет")
else:
    print("\nОдногодки:")
    for man in eq_age_people:
        print(man.name, man.surname)
        
