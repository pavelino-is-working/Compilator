tabela_codificare = {
    "identificator": 0, "constanta": 1, "program": 2, "list": 3, "of": 4, "var": 5, "integer": 6, "real": 7,
    "boolean": 8, "char": 9, "string": 10, "input": 11, "output": 12, "for": 13," ": 14, "if": 16, "endif": 17,
    "else": 18, "and": 19, "or": 20, "not": 21, ":": 22, ";": 23, ",": 24, ".": 25, "+": 26, "*": 27, "(": 28, ")": 29,
    "[": 30, "]": 31, "-": 32, "<": 33, ">": 34, "=": 35, ":=": 36, "{": 37, "}": 38, "\n": 39, "while": 40,
    "endwhile": 41
}


def is_identificator_or_constant(string):
    """
    Verify if a string is a constant or an identifier.
    Returns: 1 or 0 if is a constant or an identifier, or -1 if is a lexical error
    """
    if string.isdecimal():
        return 1
    if string[0] == '\'' and string[-1] == '\'' and len(string) == 3:
        return 1
    if string[0] == '\"' and string[-1] == '\"':
        return 1
    if string[0] in "qwertyuiopasdfghjklzxcvbnm" and (string[-1] != '\'' and string[-1] != "\""):
        return 0
    return -1


def print_table_atomi(tabela_atomi):
    print('|' + '-' * 21 + '|' + '-' * 11 + '|'+ '-' * 21 + '|')
    print(f"| {'Atom':20}| {'Cod':10}| {'Pozitie in TS':20}|")
    print('|' + '-' * 21 + '|' + '-'*11 + '|'+ '-' * 21 + '|')
    for elem in tabela_atomi:
        key = elem[0]
        value = elem[1]
        positon = elem[2]
        print(f"| {key:20}| {value:10}| {positon:20}|")
        print('|' + '-' * 21 + '|' + '-' * 11 + '|' + '-' * 21 + '|')


def main():
    tabela_atomi = []
    tabel_simboluri_identificatori = {}
    tabel_simboluri_constanta = {}
    lines = ""
    file = ["my_code1.txt", "my_code2.txt", "posibile_erori.txt"]
    with open(file[1]) as f:
        lines = lines.join([i for i in f.readlines()])
    print(lines)
    atom = ""
    for char in lines:
        if char in " :;=,.{}[](\)<>-+*/ \n":
            # indetificatori, constante, cuvinte rezervate
            if atom:
                # verifica daca atom este cuvat rezervat. Cod cuv rezevat in fip este -2
                if atom.lower() in tabela_codificare:
                    tabela_atomi.append((atom, tabela_codificare[atom.lower()], ""))
                else:
                    # verifica daca este identificator sau constanta.
                    # aici verifica si erorile lexicale
                    cod = is_identificator_or_constant(atom)
                    if cod == -1:
                        raise Exception(f"Eroare lexicala pentru {atom}")
                    elif cod == 0 and atom not in tabel_simboluri_identificatori:
                        if len(atom) >= 250:
                            raise Exception(f"Atomul {atom} are prea multe litere")
                        tabel_simboluri_identificatori[atom] = len(tabel_simboluri_identificatori) + 1
                        tabela_atomi.append((atom, cod, tabel_simboluri_identificatori[atom]))

                    elif cod == 1 and atom not in tabel_simboluri_constanta:
                        tabel_simboluri_constanta[atom] = len(tabel_simboluri_constanta) + 1
                        tabela_atomi.append((atom, cod, tabel_simboluri_constanta[atom]))

                atom = ""
            # separatori. Cod separatori in fip este -1
            cod = tabela_codificare[char]
            if cod == tabela_codificare[' ']:
                char = "spatiu"
            elif cod == tabela_codificare['\n']:
                char = "line_breaker"
            tabela_atomi.append((char, cod, ""))

        else:
            atom = atom + char
    print_table_atomi(tabela_atomi)
    print(tabel_simboluri_identificatori)
    print(tabel_simboluri_constanta)



if __name__ == "__main__":
    main()

