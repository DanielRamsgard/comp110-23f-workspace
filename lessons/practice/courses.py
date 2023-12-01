"""Pratice function writing for quiz 3."""


class Course:
    """Models the idea of a UNC course."""
    name: str
    level: int
    prerequisites: list[str]

    def is_valid_course(self, prereq: str) -> bool:
        """Checks some stuff word."""
        level_check: int = 400
        if self.level > 400 and prereq in self.prerequisites:
            return True
        
        return False


def find_courses(input_list: list[Course], prereq: str) -> list[str]:
    """Returns list of courses."""
    level_check: int = 400
    new_list: list[str] = list()

    for i in range(0, len(input_list), 1):
        if input_list[i].level > level_check and prereq in input_list[i].prerequisites:
            new_list.append(input_list[i].name)

    return new_list