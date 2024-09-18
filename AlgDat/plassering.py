    """
    plan - lag en dict frå plass til elever som vil ha plassen
    eliminer alle som sitter på sin fav plass allerede (evt gjere dette seinare i koden)
    når man har dictet, kan gå gjennom alle keys  og se på verdiene til desse keys, og så behandle de som keys og se om man finner fram til sin plass
    cycle detection? dir graf? bfs?
    sjekke om cycle på en annen måte?
    returner ett set 
    
    """



def max_permutations(M):
    favplass = {}

    for i in range(len(M)):
        if M[i] not in favplass:
            favplass[M[i]] = []
        favplass[M[i]].append(i)
    res = set()
    for key in favplass:
        vis = set()
        cur = key
        while cur not in vis:
            vis.add(cur)
            cur = M[cur]
        if cur == key:
            for student in vis:
                if M[student] != student:
                    res.add(student)

    return res

# M = [2, 0, 1, 1, 5, 4, 6]
# print(max_permutations(M))


