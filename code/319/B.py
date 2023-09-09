def generate_string(N):
    # Nの約数を求める(1~9まで)
    divisors = [i for i in range(1, 10) if N % i == 0]
    
    result = []
    for i in range(N+1):
        valid_divisors = [d for d in divisors if i % (N // d) == 0]
        # そのようなjが見つかった場合、最小のものを選ぶ
        if valid_divisors:
            result.append(str(min(valid_divisors)))
        # そのようなjが見つからない場合、"-"を追加する
        else:
            result.append("-")
    return "".join(result)

# 標準入力からNを受け取る
N = int(input().strip())
print(generate_string(N))
