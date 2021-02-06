# 复习

26

88

3

滑动窗口

https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/solution/wan-mei-xiang-xiang-xin-yuan-gong-ru-zhi-lao-yuan-/

https://leetcode-cn.com/problems/minimum-window-substring/solution/tong-su-qie-xiang-xi-de-miao-shu-hua-dong-chuang-k/

## 1.25 进度

445

## 1.26 进度

25 
25 147 148

## 1.28 进度

https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/

150 71

### 346-会员题目

## 1.29 进度
127 126 286

286-会员题目

### 回溯必读必做

https://leetcode-cn.com/problems/permutations/comments/

https://leetcode-cn.com/problems/combination-sum/comments/

类似题目还有:

[39.组合总和](https://leetcode-cn.com/problems/combination-sum/)

[40. 组合总和 II](https://leetcode-cn.com/problems/combination-sum-ii/)

[46. 全排列](https://leetcode-cn.com/problems/permutations/)

[47. 全排列 II](https://leetcode-cn.com/problems/permutations-ii/)

[78. 子集](https://leetcode-cn.com/problems/subsets/)

[90. 子集 II](https://leetcode-cn.com/problems/subsets-ii/)

这类题目都是同一类型的,用回溯算法!

其实回溯算法关键在于:不合适就退回上一步

然后通过约束条件, 减少时间复杂度.

大家可以从下面的解法找出一点感觉!

[78. 子集](https://leetcode-cn.com/problems/subsets/)

### 回朔法的思想： 回朔法的重要思想在于： 通过枚举法，对所有可能性进行遍历。 但是枚举的顺序是 一条路走到黑，发现黑之后，退一步，再向前尝试没走过的路。直到所有路都试过。因此回朔法可以简单的理解为： 走不通就退一步的方枚举法就叫回朔法。而这里回退点也叫做回朔点。

### 回朔关键点 通过分析发现，回朔法实现的三大技术关键点分别是：

一条路走到黑
回退一步
另寻他路
### 关键点的实现 那么如何才能用代码实现上述三个关键点呢？

for 循环
递归
#### 解释如下

for循环的作用在于另寻他路： 你可以用for循环可以实现一个路径选择器的功能，该路径选择器可以逐个选择当前节点下的所有可能往下走下去的分支路径。 例如： 现在你走到了节点a，a就像个十字路口，你从上面来到达了a，可以继续向下走。若此时向下走的路有i条，那么你肯定要逐个的把这i条都试一遍才行。而for的作用就是可以让你逐个把所有向下的i个路径既不重复，也不缺失的都试一遍

递归可以实现一条路走到黑和回退一步： 一条路走到黑： 递归意味着继续向着for给出的路径向下走一步。 如果我们把递归放在for循环内部，那么for每一次的循环，都在给出一个路径之后，进入递归，也就继续向下走了。直到递归出口（走无可走）为止。 那么这就是一条路走到黑的实现方法。 递归从递归出口出来之后，就会实现回退一步。

因此for循环和递归配合可以实现回朔： 当递归从递归出口出来之后。上一层的for循环就会继续执行了。而for循环的继续执行就会给出当前节点下的下一条可行路径。而后递归调用，就顺着这条从未走过的路径又向下走一步。这就是回朔

说了这么多，回朔法的通常模板是什么呢？ 递归和for又是如何配合的呢？

#### 回朔代码模板

```python
def backward():
    
    if (回朔点）：# 这条路走到底的条件。也是递归出口
        保存该结果
        return   
    
    else:
        for route in all_route_set :  逐步选择当前节点下的所有可能route
            
            if 剪枝条件：
                剪枝前的操作
                return   #不继续往下走了，退回上层，换个路再走
            
            else：#当前路径可能是条可行路径
            
                保存当前数据  #向下走之前要记住已经走过这个节点了。例如push当前节点
        
                self.backward() #递归发生，继续向下走一步了。
                
                回朔清理     # 该节点下的所有路径都走完了，清理堆栈，准备下一个递归。例如弹出当前节点

```

这里剪枝操作指的是： 对于有些问题，你走着走着，若某种情况发生了，你就已经直到不能继续往下走了，再走也没有用了。而这个情况就被称之为剪枝条件。

而DFS就是一个最典型的回朔法的应用。

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        candidates.sort()
        path = []
        res = []
        '''
        ！！！重点！！！
        在python中，如果传参是mutable var, 那么传参相当于引用，因此调用后，如果调用函数的内部对该传入变量进行修改，就会导致直接改变原始对象。这就是典型的privacy leak！！发生了。
        例如在这个，list就是该mutable var，而如果以path或res 为传参，放在__DFS 中， 那么就相当于在__DFS内部，实际上用的都是一个物理地址下的res和path，类似于全局变量。
        因此combinationSum下的局部变量path和res也在——DFS运行的过程中发生了改变。
        
        利用这个性质，我们可以把mutable var当成传入参数，从而实现全局变量的效果。
        '''
        self.__DFS(candidates, target, 0, path, res)
        return res
    '''
        DFS的实现
    '''
    def __DFS(self, candidates, target, begin, path, res):
        path = path.copy()
        # 递归出口 就是余数为0
        if target == 0:
            res.append(path)   #记录该符合条件的结果
            return
        
        #若当前路径有可能可行。
        for i in range(begin, len(candidates)):  # 我们现在到begin的节点上了
            if target - candidates[i] < 0:  # 剪枝条件
                return                      # 如果当前节点就不行了，就不用继续了,这里到不用继续了即包括该depth不用继续了，也包括该节点更大到child也不用继续了，该节点pop出来
            
            path.append(candidates[i])  #记录当前为止
            self.__DFS(candidates, target - candidates[i], i, path, res)# 向下继续走，记住递归不是return，递归到实现是调用！一旦return发生，递归停止。
            path.pop()  # 回朔清理。当前节点下的所有情况都进行完了，该节点也不应该在path里面了。

```

爬楼梯动态规划

# https://leetcode-cn.com/problems/climbing-stairs/solution/70zhong-quan-chu-ji-python3hui-ji-liao-ti-jie-qu-w/

## 动态规划三种解法+多图 三角形最小路径

https://leetcode-cn.com/problems/triangle/solution/san-chong-jie-fa-duo-tu-xiang-jie-120-san-jiao-xin/

## 剩余题目

## 动态规划 LeetCode 股票相关题目

https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/zui-jia-mai-mai-gu-piao-shi-ji-han-leng-dong-qi-4/

## 背包九讲

https://github.com/tianyicui/pack

## labuladong 的算法笔记

https://labuladong.gitee.io/algo/

## 最优子结构

要符合「最优子结构」，子问题间必须互相独立。

凑零钱问题 amount = 11 时的最少硬币数（原问题），如果你知道凑出 amount = 10 的最少硬币数（子问题），你只需要把子问题的答案加一（再选一枚面值为 1 的硬币）就是原问题的答案。因为硬币的数量是没有限制的，所以子问题之间没有相互制，是互相独立的。


1、确定 base case，这个很简单，显然目标金额 amount 为 0 时算法返回 0，因为不需要任何硬币就已经凑出目标金额了。

2、确定「状态」，也就是原问题和子问题中会变化的变量。由于硬币数量无限，硬币的面额也是题目给定的，只有目标金额会不断地向 base case 靠近，所以唯一的「状态」就是目标金额 amount。

3、确定「选择」，也就是导致「状态」产生变化的行为。目标金额为什么变化呢，因为你在选择硬币，你每选择一枚硬币，就相当于减少了目标金额。所以说所有硬币的面值，就是你的「选择」。

4、明确 dp 函数/数组的定义。我们这里讲的是自顶向下的解法，所以会有一个递归的 dp 函数，一般来说函数的参数就是状态转移中会变化的量，也就是上面说到的「状态」；函数的返回值就是题目要求我们计算的量。就本题来说，状态只有一个，即「目标金额」，题目要求我们计算凑出目标金额所需的最少硬币数量。所以我们可以这样定义 dp 函数：

dp(n) 的定义：输入一个目标金额 n，返回凑出目标金额 n 的最少硬币数量。

## 回溯法

解决一个回溯问题，实际上就是一个决策树的遍历过程。你只需要思考 3 个问题：

1、路径：也就是已经做出的选择。

2、选择列表：也就是你当前可以做的选择。

3、结束条件：也就是到达决策树底层，无法再做选择的条件。


```python
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
```

其核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」

只要从根遍历这棵树，记录路径上的数字，其实就是所有的全排列。我们不妨把这棵树称为回溯算法的「决策树」

```python
for 选择 in 选择列表:
    # 做选择
    将该选择从选择列表移除
    路径.add(选择)
    backtrack(路径, 选择列表)
    # 撤销选择
    路径.remove(选择)
    将该选择再加入选择列表
```

我们只要在递归之前做出选择，在递归之后撤销刚才的选择，就能正确得到每个节点的选择列表和路径。

### BFS 模板

```
// 计算从起点 start 到终点 target 的最近距离
int BFS(Node start, Node target) {
    Queue<Node> q; // 核心数据结构
    Set<Node> visited; // 避免走回头路

    q.offer(start); // 将起点加入队列
    visited.add(start);
    int step = 0; // 记录扩散的步数

    while (q not empty) {
        int sz = q.size();
        /* 将当前队列中的所有节点向四周扩散 */
        for (int i = 0; i < sz; i++) {
            Node cur = q.poll();
            /* 划重点：这里判断是否到达终点 */
            if (cur is target)
                return step;
            /* 将 cur 的相邻节点加入队列 */
            for (Node x : cur.adj())
                if (x not in visited) {
                    q.offer(x);
                    visited.add(x);
                }
        }
        /* 划重点：更新步数在这里 */
        step++;
    }
}
```

## TODO 学习

n数之和

###

105. 从前序与中序遍历序列构造二叉树

### 

416. 分割等和子集

### 0-1 bag问题

当前背包容量装不下，只能选择不装入背包


装入或者不装入背包，择优

