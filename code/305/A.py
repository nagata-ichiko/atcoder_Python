def nearest_water_station(N):
    if N % 5 == 0: # 高橋くんの位置が5の倍数である場合、その地点に給水所がある
        return N
    else:
        remainder = N % 5
        if remainder <= 2: # 高橋くんの位置が5の倍数から2以下離れている場合、下の5の倍数に給水所がある
            return N - remainder
        else: # 高橋くんの位置が5の倍数から3以上離れている場合、上の5の倍数に給水所がある
            return N + (5 - remainder)

N = int(input())
print(nearest_water_station(N))