# https://leetcode-cn.com/problems/unique-binary-search-trees/
# 96. 不同的二叉搜索树


class Solution:
    """
        二叉搜索树个数
        很明显的动态规划,可以组成的二叉搜索树个数应该为
        以 1-n 为根组成的二叉搜索树个数之和

        麻了...想了半天,结果别人一个公式推出来了......
        设 n 个节点可以组成的搜索二叉树的个数为 G(n),
        以 i 为根节点可以组成的二叉搜索数个数为 f(i)
        G(n) = f(1) + f(2) + f(3) ... f(n)

        以 i 为根,重复上面的逻辑, i 左边的节点个数为 i-1,右边
        节点个数为 n-i

        f(i) = G(i-1) * G(n-i) (左子树个数*右子树个数)

        综合两个公式得到:
        G(n) = G(0)*G(n-1) + G(1)*G(n-2) + .... G(n-1)*G(0)
    """

    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[-1]
