def canFinish(numCourses, prerequisites):
    dic={i:[] for i in range(numCourses)}
    for crs,pre in prerequisites:
        dic[crs].append(pre)
    visit=set()
    def dfs(crs):
        if crs in visit:
            return False
        if dic[crs]==[]:
            return True
        visit.add(crs)
        for pre in dic[crs]:
            if not dfs(pre):
                return False
        visit.remove(crs)
        dic[crs]=[]
        return True
    for crs in range(numCourses):
        if not dfs(crs):return False
    return True
