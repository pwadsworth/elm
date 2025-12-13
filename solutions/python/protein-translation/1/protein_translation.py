def proteins(strand:str, acc=[]) :
    first, rest = strand[:3], strand[3:]
    match first:
        case "AUG":	                        return proteins(rest, acc + ["Methionine"])
        case "UUU" | "UUC":	                return proteins(rest, acc + ["Phenylalanine"])
        case "UUA" | "UUG":	                return proteins(rest, acc + ["Leucine"])
        case "UCU" | "UCC" | "UCA" | "UCG": return proteins(rest, acc + ["Serine"])
        case "UAU" | "UAC":	                return proteins(rest, acc + ["Tyrosine"])
        case "UGU" | "UGC":	                return proteins(rest, acc + ["Cysteine"])
        case "UGG":                         return proteins(rest, acc + ["Tryptophan"])
        case _:	                            return acc
