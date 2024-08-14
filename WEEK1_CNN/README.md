# 1 주차 
## 목표: MNIST data set을 사용해서 손글씨 인식 프로그램을 만들기
- ![image](https://github.com/user-attachments/assets/b80a7f4c-fc16-4774-9381-60cfd2084216)

- 논문:
  - https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
  - https://arxiv.org/pdf/1511.08458 
- 참고한 링크:
  - https://eumgill98.tistory.com/12
  - https://ratsgo.github.io/deep%20learning/2017/05/14/backprop/
  - https://ratsgo.github.io/deep%20learning/2017/04/05/CNNbackprop/
  - 

### Pre-study for the Paper
- About a [Heuristic Algorithm](https://en.wikipedia.org/wiki/Heuristic_(computer_science))
- What is [Graph](https://en.wikipedia.org/wiki/Graph_theory)?
- About a [ANN](https://en.wikipedia.org/wiki/Neural_network_(machine_learning)) and ([DNN](https://en.wikipedia.org/wiki/Deep_learning#Deep_neural_networks))
- Batch and Epoch
- Loss function 
  - [MSE](https://en.wikipedia.org/wiki/Mean_squared_error)
  - [cross entropy](https://en.wikipedia.org/wiki/Cross-entropy)
- Optimizer
  - [GD](https://en.wikipedia.org/wiki/Gradient_descent)
  - Local minima problem
  - [SGD](https://en.wikipedia.org/wiki/Stochastic_gradient_descent)
  - [Adam](https://arxiv.org/abs/1412.6980)
- Overfitting problem and Solving(Dropout)
  - Definition
  - Dropout
- [Convolution](https://en.wikipedia.org/wiki/Convolution)
  - Definition
  - Forward and Backward
### [Paper](https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf) review
1. Intrduction
2. Dataset
3. The Architecture
  - 1. Relu and tanh
  - 3. Local Response Normalization
  - 4. Overlapping Pooling
  - 5. Overall Architecture
4. Reducing Overfitting
  - 1. Data Argmentation
  - 2. Dropout
5. Details of learning
6. Results
  - 1. Qualitative Evaluations
7. Discussion
# Pre-study for the Pape
## 휴리스틱 알고리즘이란?

$3x = 9$ 라는 수식을 보면 우리는 $x$에 $3$이 들어가면 정확하다는 것을 알 수 있습니다. 

근데 우리가 살고 있는 이 세상은 정확한 알고리즘으로 돌아가지 않습니다. 정확하게 맞는 수식(알고리즘)을 찾는 것도 힘들 뿐더러 아예 **"정확한 해"** 를 찾을 방법이 없을 수도  있습니다. 

따라서 **휴리스틱 알고리즘**은 정확하지는 않지만 거의 정답에 가까운 해를 찾는 알고리즘입니다. 

## 그래프(Graph Theory)
ANN을 알아보기 전에 간략히 그래프에 대해서 알아봅시다.
<div style="text-align: center;">
  <img src="https://github.com/user-attachments/assets/9bf05bc6-c3ac-4dbd-a63f-854a77feac68" alt="Graph Theory">
</div>


그래프는 원형 점으로  생긴 **노드(Node)** 와 선으로 이루어진 **엣지(Edge)로** 이루어 져 있습니다.

그래프의 종류는 엣지가 양방향인지 단방향인지에 따라 "undirect graph"와 "direct graph"으로 나뉩니다. 현재 위에 그래프는 undirect grapth입니다.

## Artificial Neural Network 와 Deep Neural Network
<div style="text-align: center;">
  <img src="https://github.com/user-attachments/assets/67ff420b-db17-4b47-ae9f-ad7b2a1f8c39" alt="ANN">
</div>

ANN은 Input Layer에서 Output Layer로 진행되는 방식을 Forward pass라 합니다.

반대로 Output Layer에서 Input Layer로 손실함수를 통해 Optimize하는 것을 Backward pass라 합니다. 

Input Layer와 Output Layer 사이에 있는 Layer(층)을 Hidden Layer(은닉층)이라고 합니다.

이러한 Hidden Layer가 2개이상이라면 그런 ANN을 DNN이라고 부릅니다.

각 간선에는 Weight(가중치)가 존재하고 Forward로 넘어갈때 이전노드*가중치로 넘어갑니다. 그리고 은닉 층에는 기본적으로 bias(편향)이 있어서 +bias도 해줘야 합니다. 즉 다음 노드의 값 = (이전 노드) * (가중치) + 편향 입니다.

그런데 우리는 이러한 NN을 통해서 복잡한 함수를 모델링 할 수 없습니다.
[이미지]()
다음 사진을 보면 이러한 모델은 결국 Wx + b 꼴이기 때문에 곡선을 표현할 수 없습니다.
따라서 각 노드에 Activation function을 적용시켜 비선형성을 줍니다.
다음 [링크](텐서플로우.플레이그라운드)에 들어가보면 Activation function이 어떻게 비선형성을 주는지 시각화해서 볼 수 있습니다.
[이미지]()

## Batch and Epoch
- 배치(Batch) : 한번에 학습하는 데이터 단위, 1 iteration = 1batch
- 에폭(Epoch) : 전체 데이터셋을 학습 시키는 단위

## Loss function
- 모델이 예측한 값과 실제 값이 얼만큼 차이가 나는지 수치화시킨 함수

### MSE
$f(x) = \frac{1}{2}\displaystyle\sum^{n}_{1} (\hat y - y)^2$

### Cross entropy


## Backpropagation



## Optimizer
학습의 목적은 Loss function을 최소화 시키는 것. 따라서 Backpropagation을 할 때 최솟값으로 갱신 시켜주는 방법을 Optimizer라고 합니다.
### GD
### Local Minima problem
### SGD
### Adam


## Overfitting 문제와 해결
### Definition
### Dropout

## Convoltuion
### Defintion
### Forward pass
### Backward pass
# Paper Review

## Introduction
## Dataset
## The Architecture
### Relu and tanh
### Local Response Normalization
### Overlapping Pooling
### Overall Architecture
## Reducing Overfitting
### Data Argmentation
### Dropout
## Details of learning
## Results
### Qualitative Evaluations
## Discussion
