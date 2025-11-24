class Solution:
    def addOperators(self, num: str, target: int):
        res = []

        def dfs(index, path, value, prev):
            if index == len(num):
                if value == target:
                    res.append(path)
                return
            for i in range(index+1, len(num)+1):
                tmp = num[index:i]
                if len(tmp) > 1 and tmp[0] == '0':
                    break
                n = int(tmp)
                if index == 0:
                    dfs(i, tmp, n, n)
                else:
                    dfs(i, path+'+'+tmp, value+n, n)
                    dfs(i, path+'-'+tmp, value-n, -n)
                    dfs(i, path+'*'+tmp, value-prev+prev*n, prev*n)

        dfs(0, '', 0, 0)
        return res
