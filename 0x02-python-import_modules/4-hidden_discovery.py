#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    codes = dir(hidden_4)
    for code in codes:
        if code[:2] != "__":
            print(code)
