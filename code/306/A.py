def repeat_chars(S):
    return ''.join([c*2 for c in S])

N = int(input().strip())
S = input().strip()

print(repeat_chars(S))
