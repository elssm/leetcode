class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        #解答1
        dict = {}
        res = []
        num = []
        result = []
        for i in range(len(arr)):
            s = str(bin(arr[i])) #将每个十进制数转为二进制字符串
            dict[i] = s.count('1') #字典中存索引对应的1的个数，不能存值，因为值会重复
        # print(dict)
        l = sorted(dict.items(),key=lambda dict:dict[1]) #按照字典的值排序，得到列表中的元祖
        l = [list(i) for i in l] #将列表中的元祖转为列表
        for i in range(len(l)):
            l[i][0] = arr[l[i][0]] #将每一个第一个索引转换为对应的值
        # print(l)
        count = list(set(sorted(dict.values()))) #计算这组数中1的不同个数
        # print(count)
        for i in count:
            for k in range(len(l)):
                if i == l[k][1]:
                    num.append(l[k][0])
            res.append(num) #将相同1的个数的值放在一个列表中
            num=[] #得到最终的列表
        # print(res)
        for i in range(len(res)): #对每一个列表中的值进行排序
            res[i]=sorted(res[i])
            for j in range(len(res[i])):
                result.append(res[i][j])
        return result

        #参考答案
        # return sorted(arr,key=lambda x:(bin(x).count('1'),x))