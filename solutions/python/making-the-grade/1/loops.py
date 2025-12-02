#Because_declarative
def round_scores(student_scores: list[float]) -> list[int]:
    return [round(x) for x in student_scores]

def count_failed_students(student_scores:list[int]) -> int:
    return len([x for x in student_scores if x <= 40])


def above_threshold(student_scores: list[int], threshold: int) -> list[int]:
    return [x for x in student_scores if x >= threshold]


def letter_grades(highest: int) -> list[int]:
    return list(range(41, highest, round((highest-40)/4)))


def student_ranking(student_scores: list[int], student_names: list[str]) -> list[str]:
    rankings = list(zip(range(1,len(student_names) + 1), student_names, student_scores))
    return list(map(lambda r: f"{r[0]}. {r[1]}: {r[2]}", rankings))


def perfect_score(student_info: list[list[str | int]]) -> list[str | int]:
    result = [x for x in student_info if x[1] == 100]
    return result[0]  if result else []