class Solution(object):
    def dfs(self,curr,adjList,visited,path_visited,stack):
        visited[curr]=True
        path_visited[curr]=True
        for neighbor in adjList[curr]:
            # 1. Cycle detection: If neighbor is in current path, TopSort is impossible
            if path_visited[neighbor]:
                return True#cycle exist
                
            if not visited[neighbor]:
                if self.dfs(neighbor, adjList, visited, path_visited, stack):
                    return True#eplore all neighbors

        path_visited[curr] = False  # Backtrack
        # 2. Topological Sort Addition:
        # Since 'curr' has finished exploring all its dependencies, 
        # it is safe to push it to our order stack.
        stack.append(curr) 
        return False

    def canFinish(self, numCourses, prerequisites):
        adjList=[]
        for i in range(numCourses):
            adjList.append([])
        for edge in prerequisites:
            x=edge[0]
            y=edge[1]
            adjList[x].append(y)#becouse this is a directed graph

        visited=[False]*numCourses
        path_visited=[False]*numCourses
        stack=[]

        for i in range(numCourses):
            if not visited[i]:
                # If a cycle is detected, topological sort is invalid
                if self.dfs(i, adjList, visited, path_visited, stack):
                    return False#if a cycle exist we cantnot completet ourse
                    
        # Reverse the stack to get the correct chronological ordering
        return True # if no cycle exists then we can finist the complete course return True

        