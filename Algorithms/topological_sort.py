
def topologicalSort(jobs, deps):
    # Write your code here.
    def dfs(node, dependency, jobs_state, job_order, cycleExists):
        if jobs_state[node] == 2:
            return
        if jobs_state[node] == 1:
            print('Cycle Exists.')
            cycleExists[0] = True
            return
        jobs_state[node] = 1
        for child in dependency[node]:
            dfs(child, dependency, jobs_state, job_order, cycleExists)
        jobs_state[node] = 2
        
        job_order.append(node)
        
    jobs_state = {value:0 for value in jobs} 
    dependency = {}
    cycleExists = [False]
    for pre, post in deps:
        if pre in dependency.keys():
            dependency[pre].append(post)
        else:
            dependency[pre] = [post]

    for job in jobs:
        if job not in dependency.keys():
            dependency[job] = []

    job_order = []
    for job in jobs:
        dfs(job, dependency, jobs_state, job_order, cycleExists)
    return job_order[::-1] if not cycleExists[0] else []

if __name__ == "__main__":
    jobs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    deps = [
                [1, 2],
                [1, 3],
                [1, 4],
                [1, 5],
                [1, 6],
                [1, 7],
                [2, 8],
                [3, 8],
                [4, 8],
                [5, 8],
                [6, 8],
                [7, 8],
                [2, 3],
                [2, 4],
                [5, 4],
                [7, 6],
                [6, 2],
                [6, 3],
                [6, 5],
                [5, 9],
                [9, 8],
                [8, 0],
                [4, 0],
                [5, 0],
                [9, 0],
                [2, 0],
                [3, 9],
                [3, 10],
                [10, 11],
                [11, 12],
                [12, 2]
            ]
    result = topologicalSort(jobs, deps)
    print('Job Order : {}'.format(result))