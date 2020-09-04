def solution(N, stages):
    a = []
    for i in range(1, N+1):
        success, tries = 0, 0
        for stage in stages:
            if stage > i:
                success += 1
                tries += 1
            elif stage == i:
                tries += 1
        if tries:
            a.append((success/tries,i))
        else:
            a.append((1, i))
            
    return [i[1] for i in sorted(a)]