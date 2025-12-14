def response(input:str) -> str:
    if input.endswith("?") and input.isupper():
        return "Calm down, I know what I'm doing!"
    elif input.strip().endswith("?"):
        return "Sure."
    elif input.isupper():
        return "Whoa, chill out!"
    elif input.isspace() or input == "":
        return "Fine. Be that way!"
    else:
        return "Whatever."
