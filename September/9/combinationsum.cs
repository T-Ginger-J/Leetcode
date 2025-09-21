using System;
using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> CombinationSum(int[] candidates, int target) {
        var res = new List<IList<int>>();
        Backtrack(candidates, target, 0, new List<int>(), res);
        return res;
    }

    private void Backtrack(int[] candidates, int target, int start, List<int> path, IList<IList<int>> res) {
        if (target == 0) {
            res.Add(new List<int>(path));
            return;
        }

        for (int i = start; i < candidates.Length; i++) {
            if (candidates[i] <= target) {
                path.Add(candidates[i]);
                Backtrack(candidates, target - candidates[i], i, path, res); // can reuse same element
                path.RemoveAt(path.Count - 1);
            }
        }
    }
}

public class Program {
    public static void Main() {
        var sol = new Solution();
        int[] candidates = {2, 3, 6, 7};
        var res = sol.CombinationSum(candidates, 7);

        foreach (var combo in res) {
            Console.WriteLine(string.Join(",", combo));
        }
    }
}
