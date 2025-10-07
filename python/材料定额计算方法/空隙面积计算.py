import numpy as np


"两大一小空隙面积计算"
#大圆直径
print("请输入大圆直径：")
D=float(input())/2
#小圆直径
print("请输入小圆直径：")
d=float(input())/2
#成缆半径
print("请输入成缆直径：")
R=float(input())/2

def two_large_one_small_void_ratio_calc(D,d,R):
#三角形的边
    a=D+d
    b=D+d
    c=2*D
#三角形的各个角
    A=np.acos((np.power(a,2)+np.power(b,2)-np.power(c,2))/(2*a*b))
    B=np.acos((np.power(a,2)+np.power(c,2)-np.power(b,2))/(2*a*c))
    C=np.acos((np.power(b,2)+np.power(c,2)-np.power(a,2))/(2*b*c))
    theta = np.asin(D/(R-D))
#空隙面积计算
    if 2/3*D<d:
    #三个圆相切的最内的空隙面积
        S_0=D*np.sqrt((2*D+d)*d)-B*(np.power(D,2))-C*(np.power(d,2))/2
        print("三个圆相切的最内的空隙面积S_0：",S_0)
    #最大的那个空隙面积
        S_1=theta*(np.power(R,2)-np.power(D,2))-D*np.sqrt(np.power(R,2)-D*2*R)-np.pi*np.power(D,2)/2
        print("最大的那个空隙面积S_1：",S_1)
    #较小的那个空隙面积
        S_2=((np.pi*(np.power(R,2)-2*np.power(D,2)-np.power(d,2)))-S_1-S_0)/2
        print("较小的那个空隙面积S_2：",S_2)  
    else:
        S_0=D*np.sqrt((2*D+d)*d)-B*(np.power(D,2))-C*(np.power(d,2))/2
        print("三个圆相切的最内的空隙面积S_0：",S_0)
        S_1=np.pi*np.power(R,2)/4
        print("最大的那个空隙面积S_1：",S_1)
        S_2=((np.pi*(np.power(R,2)-2*np.power(D,2)-np.power(d,2)))-S_1-S_0)/2
        print("较小的那个空隙面积S_2)：",S_2)
    return S_0,S_1,S_2

# 使用样例
if __name__ == "__main__":
    print("===== 两大一小空隙面积计算样例 =====")
    # 设置样例参数
    D_example = 9  # 大圆直径
    d_example = 6   # 小圆直径
    R_example = 18  # 成缆直径
    
    print(f"样例参数：大圆直径={D_example}, 小圆直径={d_example}, 成缆直径={R_example}")
    
    # 计算空隙面积
    S = two_large_one_small_void_ratio_calc(D_example, d_example, R_example)
    print(f"计算结果：空隙面积={S}")



