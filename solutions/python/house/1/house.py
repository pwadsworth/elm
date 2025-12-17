def recite(start_verse: int, end_verse:int):
    result = []
    rhyme = ""
    verses_content = [ ("house", "Jack built."),("malt", "lay in"), ("rat", "ate"), ("cat", "killed") , ("dog", "worried") , ("cow with the crumpled horn", "tossed") , ("maiden all forlorn", "milked") , ("man all tattered and torn", "kissed") , ("priest all shaven and shorn", "married") , ("rooster that crowed in the morn", "woke") , ("farmer sowing his corn", "kept") , ("horse and the hound and the horn", "belonged to")]

    for content in verses_content: 
        match content:
            case ("house", _): 
                result.append(f"This is the {content[0]} that {content[1]}")
            case _:
                result.append(f"This is the {content[0]} that {content[1]} {result[-1][8:]}")
    return result[start_verse-1:end_verse]