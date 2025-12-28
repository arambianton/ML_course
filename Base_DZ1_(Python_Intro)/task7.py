def find_modified_max_argmax(L,f):
    L=[*map(f,[*filter(lambda x:type(x)==int,L)])]
    return (m:=max(L),L.index(m)) if L else ()