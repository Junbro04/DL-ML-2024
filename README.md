# DL-ML-2024

## We study to ML(Machine Learning) and DL(Deep Learning)
- [동빈나](https://www.youtube.com/@dongbinna)
- [코드없는프로그래밍](https://www.youtube.com/@user-pw9fm4gc7e)
- [혁펜하임](https://www.youtube.com/@hyukppen)
- [메타코드](https://www.youtube.com/@mcodeM)

# 1 주차
## 목표: MNIST data set을 사용해서 손글씨 인식 프로그램을 만들기
- ![image](https://github.com/user-attachments/assets/69a40a16-cf26-4cef-a516-01cc45c41f70)

- 논문:
  - https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
  - https://arxiv.org/pdf/1511.08458  
- 블로그: https://eumgill98.tistory.com/12
- 유튜브:
  - [AI기초수학](https://www.youtube.com/watch?v=Pm3BBaVRcJA)
  - [Pytorch](https://www.youtube.com/watch?v=_3JAG9vORfo)
  - [딥러닝](https://www.youtube.com/watch?v=WKnUYTxaPn4&list=PLDV-cCQnUlIZnEHuRFc1OZfcYjbgi4QnD)
  - [컴퓨터비전](https://www.youtube.com/watch?v=6MWlrSNXYi8&list=PLDV-cCQnUlIaIFHQwuXRRSL833cRAS76M)
  - [MNIST](https://www.youtube.com/watch?v=RjpkS-5rW4s&t=565s)

- [휴리스틱](https://en.wikipedia.org/wiki/Heuristic_(computer_science))에 대해서
- [그래프](https://en.wikipedia.org/wiki/Graph_theory) 에 대해서
- [ANN](https://en.wikipedia.org/wiki/Neural_network_(machine_learning))에 대해서([DNN](https://en.wikipedia.org/wiki/Deep_learning#Deep_neural_networks))
- loss funtion 그리고 local minimum 문제와 해결
- overfitting(과적합) 문제 그리고 해결(Drop out)

## 휴리스틱 알고리즘이란?

$3x = 9$ 라는 수식을 보면 우리는 $x$에 $3$이 들어가면 정확하다는 것을 알 수 있습니다. 
근데 우리가 살고 있는 이 세상은 정확한 알고리즘으로 돌아가지 않습니다. 정확하게 맞는 수식(알고리즘)을 찾는 것도 힘들 뿐더러 아예 **"정확한 해"** 가 존재하지 않을 수 있습니다. 따라서 **휴리스틱 알고리즘**은 정확하지는 않지만 거의 정답에 가까운 해를 찾는 알고리즘입니다. 저 수식에서 우리가 만약 $x=3$이라는 것을 모른다거나, 시간이 오래 걸린다면, 어떠한 휴리스틱 알고리즘이 (빠르게)$x=2.9888$ 이런식으로 근사시키는 것입니다. 실제로 $3*(2.9888) = 8.9664$로 오차가 $-0.0336$정도 나오고 이러한 오차를 줄일 수 있다면 좋은 알고리즘이라는 거죠

## 그래프(Graph Theory)
ANN을 알아보기 전에 간략히 그래프에 대해서 알아봅시다.
![image](https://github.com/user-attachments/assets/9bf05bc6-c3ac-4dbd-a63f-854a77feac68)

그래프는 원형 점으로  생긴 **노드(Node)** 와 선으로 이루어진 **엣지(Edge)로** 이루어 져 있습니다.

