 i , j = 0 , 0
    m , n = len(a), len(b)
    out=[]

    while i<=n and j<=m:
        if a[i] <= b[j]:
            out.append(a[i])
            i+=1
        else:
            out.append(b[j])
            j+=1

    while i<=n:
        out.append(a[i])
        i+=1

    while j<=m:
        out.append(b[j])
        j+=1

    print(out)