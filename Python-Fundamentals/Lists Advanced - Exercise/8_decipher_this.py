message = input().split()

words = []
numbers = []
num = ""
let = ""
for word in message:

    for symbol in word:
        if symbol.isdigit():
            num += symbol
        else:
            let += symbol

    numbers.append(int(num))
    if len(let) != 1:
        let = let[-1] + let[1:-1] + let[0]
    words.append(let)
    num = ""
    let = ""

for n, w in zip(numbers, words):
    print(f"{chr(n)}{w}", end=" ")
