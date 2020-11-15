 Example Package
 =====================================




* **Function Sphere**
    - $f(\textbf{x}) = f(x_1, x_2, ..., x_n) = {\sum_{i=1}^{n} x_i^{2}}.$
   
    - su minima global es:
    $\textbf{x}^{\ast} = (0, …, 0)$
   
    - ![avatar](http://benchmarkfcns.xyz/benchmarkfcns/plots/spherefcn.png)
    
    - la solucion que tenemos 
    ```
    [-0.06889688 -0.01800394  0.12825548  0.16842909  0.03274765 -0.09587791
     -0.11922565  0.02011987 -0.01124445 -0.10457042] fitness: -0.0858347067339051
    ```
   
   -----------------------
 * **Function Ackley**
    - $f(\textbf{x}) = f(x_1, ..., x_n)= -a.exp(-b\sqrt{\frac{1}{n}\sum_{i=1}^{n}x_i^2})-exp(\frac{1}{n}\sum_{i=1}^{n}cos(cx_i))+ a + exp(1)$
    
    ```
   [-0.03493712  0.59355218 -0.07135287 -0.16715768  0.00476106 -0.11257682
    0.34237512  0.0728799   0.90491543 -0.08983283] 
    fitness: -2.431911011363344
    ```