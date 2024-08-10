# 1 주차 
## 목표: MNIST data set을 사용해서 손글씨 인식 프로그램을 만들기
- ![image](https://github.com/user-attachments/assets/b80a7f4c-fc16-4774-9381-60cfd2084216)

- 논문:
  - https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
  - https://arxiv.org/pdf/1511.08458 
- 참고한 링크:
  - https://eumgill98.tistory.com/12
  - 

### Prelearning before reading the paper
- About a [Heuristic Algorithm](https://en.wikipedia.org/wiki/Heuristic_(computer_science))
- What is [Graph](https://en.wikipedia.org/wiki/Graph_theory)?
- About a [ANN](https://en.wikipedia.org/wiki/Neural_network_(machine_learning)) and ([DNN](https://en.wikipedia.org/wiki/Deep_learning#Deep_neural_networks))
- Loss funtion 
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

## 휴리스틱 알고리즘이란?

$3x = 9$ 라는 수식을 보면 우리는 $x$에 $3$이 들어가면 정확하다는 것을 알 수 있습니다. 

근데 우리가 살고 있는 이 세상은 정확한 알고리즘으로 돌아가지 않습니다. 정확하게 맞는 수식(알고리즘)을 찾는 것도 힘들 뿐더러 아예 **"정확한 해"** 를 찾을 방법이 없을 수도  있습니다. 

따라서 **휴리스틱 알고리즘**은 정확하지는 않지만 거의 정답에 가까운 해를 찾는 알고리즘입니다. 

저 수식에서 우리가 만약 $x=3$이라는 것을 모른다거나, 해를 찾는 시간이 오래 걸린다면, 어떠한 휴리스틱 알고리즘이 (빠르게) $x=2.9888$ 이런식으로 근사시키는 것입니다. 

실제로 $3*(2.9888) = 8.9664$로 오차가 $-0.0336$정도 나오고 이러한 오차를 줄일 수 있다면 좋은 알고리즘이라는거죠

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


## Loss funtion과 Local Minimum



## Batch and Epoch


## Overfitting 문제와 해결

### Drop out

