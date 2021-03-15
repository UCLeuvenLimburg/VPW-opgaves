def solve(signal, codes):
    result = ''
    while signal:
        match = [ (letter, code) for letter, code in codes if signal.startswith(code) ]
        if not match:
            return 'ONMOGELIJK'
        else:
            letter, code = match[0]
            result += letter
            signal = signal[len(code):]
    return result


ncases = int(input())
for index in range(1, 1+ncases):
    signal = input().strip()
    ncodes = int(input())
    codes = []
    for _ in range(ncodes):
        letter = input().strip()
        code = input().strip()
        codes.append((letter, code))
    codes.sort(key=lambda pair: len(pair[1]), reverse=True)
    solution = solve(signal, codes)
    print(f"{index} {solution}")