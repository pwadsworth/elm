def get_coordinate(record: tuple[str, str]) -> str:
    _, coord = record
    return coord

def convert_coordinate(coordinate: str) -> tuple[str, str]:
    return (coordinate[0], coordinate[1])

def compare_records(azara_record: tuple[str, str], rui_record: tuple[str, tuple[str, str], str]) -> bool:
    return azara_record[1] == (rui_record[1][0] + rui_record[1][1])

def create_record(azara_record: tuple[str, str], rui_record: tuple[str, tuple[str, str], str]) -> tuple[str, str, str, tuple[str, str], str] | str:
    return azara_record + rui_record if compare_records(azara_record, rui_record) else "not a match"

def clean_up(combined_record_group) -> str:
    result = ""
    for el in combined_record_group:
        result += f"('{el[0]}', '{el[2]}', {el[3]}, '{el[4]}')\n"
    return result