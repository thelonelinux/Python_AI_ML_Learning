"""Classes: define reusable blueprints for objects, support inheritance, encapsulation, and behavior."""

class Person:
    """A simple class to represent a person."""

    species = "Homo sapiens"  # class attribute shared by all Person objects

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        """Instance method: uses object state to return a greeting."""
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    @classmethod
    def species_info(cls) -> str:
        """Class method: acts on the class rather than a specific instance."""
        return f"All {cls.__name__} instances are {cls.species}."

    @staticmethod
    def is_adult(age: int) -> bool:
        """Static method: utility that does not access class or instance state."""
        return age >= 18

    @property
    def is_minor(self) -> bool:
        """Property: computed value accessed like an attribute."""
        return self.age < 18


class Student(Person):
    """Inheritance: Student extends Person with additional behavior."""

    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self) -> str:
        """Override the parent greet method with student-specific info."""
        base_greeting = super().greet()
        return f"{base_greeting} My student ID is {self.student_id}."


if __name__ == "__main__":
    alice = Person("Alice", 30)
    print(alice.greet())
    print(Person.species_info())
    print("Is Alice adult?", Person.is_adult(alice.age))
    print("Is Alice minor?", alice.is_minor)

    bob = Student("Bob", 17, "S12345")
    print(bob.greet())
    print("Is Bob adult?", Student.is_adult(bob.age))
    print("Is Bob minor?", bob.is_minor)
