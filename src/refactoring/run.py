from refactoring.statement import Statement
import json


def main():
    with open("data/invoices.json") as f:
        invoices = json.load(f)
    with open("data/plays.json") as f:
        plays = json.load(f)
    print(Statement().statement(invoices[0], plays))


if __name__ == "__main__":
    main()
