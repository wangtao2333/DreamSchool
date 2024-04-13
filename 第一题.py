import bisect
def solution(source, target):
    count = 0
    length1 = len(source)
    source_map = {}
    for i in range(length1):
        if source[i] in source_map:
            source_map[source[i]].append(i)
        else:
            source_map[source[i]] = [i]
    current_location = 0
    used_map = {}
    for c in target:
        if c not in source_map:
            return -1
        if c in used_map and used_map[c] == source_map[c][-1]:
            count += 1
            used_map.clear()
            used_map[c] = source_map[c][0]
            current_location = used_map[c]
            continue
        if c not in used_map:
            if current_location > source_map[c][0]:
                count += 1
                used_map.clear()
            used_map[c] = source_map[c][0]
            current_location = used_map[c]
        else:
            location  = used_map[c]
            if current_location > location:
                location = current_location
            temp = bisect.bisect_right(source_map[c], location)
            used_map[c] = source_map[c][temp]
            if used_map[c] <= current_location:
                count += 1
                used_map.clear()
                used_map[c] = source_map[c][0]
            current_location = used_map[c]
    if used_map:
        count += 1
    return count

if __name__ == "__main__":
    print(solution("abc", "abcab"))
    print(solution("abc", "acdab"))
    print(solution("xyz", "xzyxz"))

