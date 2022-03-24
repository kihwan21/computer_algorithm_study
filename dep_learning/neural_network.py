

import numpy as np

def sigmoid(x):     # 활성화 함수
    return 1 / (1 + np.exp(-x)) 

def identity_functions(x):  # 값을 출력하기 위한 함수(코드 흐름을 동일하게 하려고 있음) 설계는 미구현 선형 / 비선형
    return x

def init_network():
    network = {}
    network["W1"] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network["b1"] = np.array([0.1, 0.2, 0.3])
    
    network["W2"] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network["b2"] = np.array([0.1, 0.2])
    
    network["W3"] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network["b3"] = np.array([0.1, 0.2])
    
    return network

def forward(network, x):
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]
    
    a1 = np.dot(x, W1) + b1 # 1층
    z1 = sigmoid(a1)    # 활성화 함수
    
    a2 = np.dot(z1, W2) + b2    # 2층
    z2 = sigmoid(a2)    # 활성화 함수
    
    a3 = np.dot(z2, W3) + b3    # 출력 층
    y = identity_functions(a3)  # 출력 함수 코드 흐림 때문에 넣은 함수. 기능은 없음 출력층 설계는 미구현 선형 / 비선형
    
    return y

network = init_network()    # 객체 생성
x = np.array([1.0, 0.5])    # 입력 값
y = forward(network, x)     # 객체 생성
print(y)