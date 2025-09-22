def merge(a:list[int], b:list[int])->None:
    i = 0
    j = 0
    n  = len(a)
    m = len(b)
    out=[]

    while i<n and j<m:
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j+=1

    while i<n:
        out.append(a[i])
        i+=1

    while j<m:
        out.append(b[j])
        j+=1

    print(out)


a = [10, 30, 50 ,70]
b = [20, 40, 60, 80, 90, 100]
merge(a,b)