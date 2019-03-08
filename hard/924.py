class Solution(object):
    def minMalwareSpread(self, network, initial_machines):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
        initial_machines = set(initial_machines)
        searched = set()
        connected = {}
        malwares = {}
        def dfs(parent, node):
            if node in searched:
                return
            else:
                searched.add(node)
                connected[parent] += [node]
                malwares[parent] += 1 if node in initial_machines else 0
                for i in range(len(network)):
                    if network[node][i]:
                        dfs(parent, i)
        for machine in range(len(network)):
            if not machine in searched and machine in initial_machines:
                searched.add(machine)
                connected[machine] = [machine]
                malwares[machine] = 1 if machine in initial_machines else 0
                for i in range(len(network)):
                    if network[machine][i]:
                        dfs(machine, i)
        ans = [min(network), 0]
        for candidate, number in malwares.items():
            if number == 1:
                if len(connected[candidate]) > ans[1]:
                    ans = [candidate, len(connected[candidate])]
                    continue
                if len(connected[candidate]) == ans[1]:
                    ans = [min(candidate, ans[0]), ans[1]]
        return ans[0]

if __name__ == '__main__':
    sol = Solution()
    graph = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    initial = [0, 1]
    print(sol.minMalwareSpread(graph, initial))
