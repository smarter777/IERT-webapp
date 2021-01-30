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

