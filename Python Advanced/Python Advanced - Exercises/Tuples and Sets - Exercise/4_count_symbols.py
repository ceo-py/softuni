main_string = input()

result_ = {}
for symbol in main_string:
    result_[symbol] = f": {main_string.count(symbol)} time/s"

for sym, rep in sorted(result_.items()):
    print(f"{sym}{rep}")