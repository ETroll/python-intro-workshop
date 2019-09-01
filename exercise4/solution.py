import json


def solution(word: str) -> int:
    if(word and word is not None):
        uppercase: str = word.upper()
        sum: int = 0

        try:
            with open("exampledata/scrabbleletters.json") as fileobj:
                scoreDict: dict = json.load(fileobj)

                for letter in uppercase:
                    for wordvalue in scoreDict["values"]:
                        if letter in wordvalue["letters"]:
                            sum += wordvalue["value"]

        except Exception as e:
            print(e)
        else:
            return sum
    
    return 0