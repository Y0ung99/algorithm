def solution(s):
    minimum = 1001
    
    if len(s) == 1:
        return 1

    for i in range(1, len(s), 1):
        arr = []
        strs = ''
        for j in range(0, len(s), i):
            if j+i > len(s):
                tail = []
                for k in range(j, len(s)):
                    tail.append(s[k])
                arr.append(''.join(tail))
                break
            arr.append(s[j:j+i])
            
        pos = 0
        same = 1
        while pos < len(arr) - 1:
            if arr[pos] == arr[pos+1]:
                same += 1
            else:
                if same > 1:
                    strs += str(same) + arr[pos]
                else:
                    strs += arr[pos]
                same = 1
            pos += 1
            if pos == len(arr) - 1:
                if same > 1:
                    strs += str(same) + arr[pos]
                else:
                    strs += arr[pos]
                same = 1
        minimum = min(len(strs), minimum)
        
    return minimum