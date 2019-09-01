import exercise1
import exercise2
import exercise3
import exercise4
# from exercise1 import solution as exercise1;

if __name__ == '__main__':
    for i in range(1,20):
        print(exercise1.fizzbuzz(i), end=" ")
    print("\n")

    exercise2.solution()
    exercise2.bonus("exampledata/sentence.txt")
    print("\n")

    exercise3.solution()

    print(f"Oxyphenbutazone has a score of {exercise4.solution('oxyphenbutazone')}")