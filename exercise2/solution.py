

def solution() -> None:
    sentence : str = input("Write a sentence to flip: ")
    print(reverseSentence(sentence))

def bonus(filepath: str) -> None:
    try:
        with open(filepath, "r") as fileobj:
            lines: list = fileobj.readlines()
            sentence: str = " ".join(lines)
    except Exception as e:
        print(e)
    else:
        print(reverseSentence(sentence))
    print(sentence)

def reverseSentence(sentence: str) -> str:
    if sentence is not None:
        return " ".join(sentence.split()[::-1])
        wordlist : list = sentence.split()
        wordlist = wordlist[::-1]
        return " ".join(wordlist)