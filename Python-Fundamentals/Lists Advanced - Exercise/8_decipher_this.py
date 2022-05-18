message = input().split()

words, numbers = [], []
for word in message:
    num, let = "", ""
    for symbol in word:
        if symbol.isdigit():
            num += symbol
        else:
            let += symbol
    numbers.append(int(num))
    if len(let) != 1:
        let = f"{let[-1]}{let[1:-1]}{let[0]}"
    words.append(let)

for n, w in zip(numbers, words):
    print(f"{chr(n)}{w}", end=" ")
