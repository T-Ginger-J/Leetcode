// LeetCode 289: Game of Life
// Explanation:
// 1. In-place state encoding to avoid extra memory.
// 2. 2 represents live->dead, 3 represents dead->live.
// 3. Time: O(m*n), Space: O(1)

#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> gameOfLife(vector<vector<int>>& board) {
        int m = board.size(), n = board[0].size();
        vector<pair<int,int>> dirs{{0,1},{0,-1},{1,0},{-1,0},{1,1},{1,-1},{-1,1},{-1,-1}};
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                int live=0;
                for(auto d: dirs){
                    int x=i+d.first, y=j+d.second;
                    if(x>=0 && x<m && y>=0 && y<n && (board[x][y]==1 || board[x][y]==2)) live++;
                }
                if(board[i][j]==1 && (live<2 || live>3)) board[i][j]=2;
                if(board[i][j]==0 && live==3) board[i][j]=3;
            }
        }
        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++)
                if(board[i][j]==2) board[i][j]=0;
                else if(board[i][j]==3) board[i][j]=1;
        return board;
    }
};

#include <iostream>
int main() {
    Solution s;
    vector<vector<int>> board1{{0,1,0},{0,0,1},{1,1,1},{0,0,0}};
    auto res1 = s.gameOfLife(board1);
    for(auto row: res1){ for(int x: row) cout<<x<<" "; cout<<endl; }

    vector<vector<int>> board2{{1,1},{1,0}};
    auto res2 = s.gameOfLife(board2);
    for(auto row: res2){ for(int x: row) cout<<x<<" "; cout<<endl; }
}
