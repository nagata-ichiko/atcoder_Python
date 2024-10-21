def main():
    import sys
    import bisect

    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    A.sort()
    B.sort()

    def is_possible(x):
        # Combine existing boxes with the new box x
        combined = B + [x]
        combined.sort()
        # Try to assign smallest toy to smallest possible box
        for a, b in zip(A, combined[-N:]):
            if b < a:
                return False
        return True

    left = 1
    right = 10**10  # 上限を大きめに設定
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    # 最後に確認
    if answer != -1 and is_possible(answer):
        print(answer)
    else:
        print(-1)

if __name__ == "__main__":
    main()