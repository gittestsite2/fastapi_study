# FastAPI Study
    # 일시 : 2022.06 ~

# Day1 
    > homework
      endpoint함수의 QueryParam을 가변으로 받는 기능 구현해오기

    > 문제
      인자값 q=a&q2=b&q3=c&q4=d&q5=f 5가지 값을 한번에 동적으로 보내는 방법
      인자값의 Parameter는 a,b,c등등 동적으로 변할수 있다.

    > 방안1
      key&value를 하나의 문자열로 인코딩해서 Request보내는 방법
      & 와 = 으로 분리하여서 Parsing처리함

    > 방안2
      방안 1에서 처럼 하나의 문자열을 인코딩해서 전송하지만, Dict형태로 구성해서 
      받는쪽에서 쉽게 구별해서 처리

    > 방안 3
      QueryParam방식은 아니지만, Request Body을 통해서 전송하는 방법

