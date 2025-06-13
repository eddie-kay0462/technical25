def compare_versions(v1, v2):
    version1 = v1.split(".")
    version2 = v2.split(".")

    n = len(version1)
    m = len(version2)

    for i in range(min(n, m)):
        # get the ele at index and cast
        v1_int = int(version1[i])
        v2_int = int(version2[i])

        # compare and return
        if(v1_int < v2_int):
            return -1
        
        # compare and return 
        if(v1_int > v2_int):
            return 1
    
    # len v1 more than v2
    if n > m:
        for i in range(n,m):
            v1_int = int(version1[i])
            if v1_int > 0:
                return 1
                
            if v1_int < 0:
                  return -1
    
    # len v2 more than v1
    if m > n:
        for i in range(n,m):
            v2_int = int(version2[i])
            if v2_int > 0:
                return -1
                
            if v2_int < 0:
                  return 1

    # the version are equall
    return 0

res = compare_versions("1.0.1", "1")
print(res)