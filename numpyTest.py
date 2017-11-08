#encoding=utf-8
import  numpy as np
from numpy.linalg import *


def mian():
    lst  = [[1,3,5],[2,4,6]]
    print(type(lst))
    '''<class 'list'>'''
    np_lst = np.array(lst)
    print(type(np_lst))
    '''<class 'numpy.ndarray'>'''
    '''
        np.arrary(lst,dype=**)
        定义数据结构类型
    '''
    print(np_lst.shape)             # 形状
    print(np_lst.ndim)              # 维数
    print(np_lst.dtype)             # 类型
    print(np_lst.itemsize)          # 每个元素的大小
    print(np_lst.size)              # 大小

    #2 Some Arrarys
    print(np.zeros([2,4]))
    print(np.ones([3,5]))
    print("Rand")
    print(np.random.rand(2,4))
    print(np.random.rand())
    print("RandInt")
    print(np.random.randint(1,10,3))
    print("RandN")
    print(np.random.randn(2,4))
    print("Choice")
    print(np.random.choice([10,100,200]))
    print("Distribute")
    print(np.random.beta(1,10,100))

    # 3 arrary opes
    lst = np.arange(1,11).reshape([2,5])
    print(np.exp(lst))
    print(np.exp2(lst))
    print(np.sqrt(lst))
    print(np.sin(lst))
    print(np.log(lst))
    print(lst.sum(axis = 0))

    #4 liner algebra
    print(np.eye(3))
    lst = np.array([[1,2],[3,4]])
    print('Inv:')       # 逆
    print(inv(lst))
    print('T:')
    print(lst.transpose())  #转换
    print('Det:')
    print(det(lst))         #行列式
    print(eig(lst))         #特征值和特征向量
    y = np.array([[5],[7]])
    print('Solve')
    print(solve(lst,y))

if __name__ == '__main__':
    mian()