 Example Package
 =====================================




* **Function Sphere**
    - $f(\textbf{x}) = f(x_1, x_2, ..., x_n) = {\sum_{i=1}^{n} x_i^{2}}.$
   
    - bounds: $x_i \in [-5.12, 5.12]$ for $i = 1..n$
   
    - su minima global esta:
    $\textbf{x}^{\ast} = (0, …, 0)$
   
     ![avatar](http://benchmarkfcns.xyz/benchmarkfcns/plots/spherefcn.png)
    
    - la solucion que tenemos :
    ```
    [-0.41132545  0.46045217 -0.42690628  0.07419403 -0.21747127  0.10151513
    0.3634374  -0.18947059  0.39664933  0.05690414] 
    fitness: -0.9551122511475386
    ```
   
 
 * **Function Ackley**
    - $f(\textbf{x}) = f(x_1, ..., x_n)= -a.exp(-b\sqrt{\frac{1}{n}\sum_{i=1}^{n}x_i^2})-exp(\frac{1}{n}\sum_{i=1}^{n}cos(cx_i))+ a + exp(1)$
   
    - bounds: $x_i \in [-32, 32]$ for $i = 1..n$
    
    - su minima global esta: $f(\textbf{x}^{\ast})=0$ donde $\textbf{x}^{\ast} = (0, …, 0)$
    
     ![avatar](http://benchmarkfcns.xyz/benchmarkfcns/plots/ackleyfcn.png)
    
    - la solucion que tenemos:
    ```
   [-0.03493712  0.59355218 -0.07135287 -0.16715768  0.00476106 -0.11257682
    0.34237512  0.0728799   0.90491543 -0.08983283] 
    fitness: -2.431911011363344
    ```
 
* **Function Rosenbrock**
    - $f(x, y)=\sum_{i=1}^{n}[b (x_{i+1} - x_i^2)^ 2 + (a - x_i)^2]$
    
    - su minima global esta: $f(\textbf{x}^{\ast})=0$ donde $\textbf{x}^{\ast} = (1, …, 1)$
    
     ![avatar](http://benchmarkfcns.xyz/benchmarkfcns/plots/rosenbrockfcn.png)
    
    - bounds: $x_i \in [-5, 10]$ for $i = 1..n$
    
    - la solucion que tenemos:
    ```
  [-1.99958731 -2.00391387 -2.03307994  0.05224216  0.07695987  0.1016336
    -2.18536878  0.42312525 -2.98130505 -4.95726777] 
    fitness: -2.1213558789940317
  
  
   ```
  
  
 * **Function Rastrigin**
    - $f(x, y)=10n + \sum_{i=1}^{n}(x_i^2 - 10cos(2\pi x_i))$
    
    - su minima global esta: $f(\textbf{x}^{\ast})=0$ donde$ \textbf{x}^{\ast} = (0, 0)$
    
    ![avatar](http://benchmarkfcns.xyz/benchmarkfcns/plots/rastriginfcn.png)
    
    - bounds: $x_i \in [-5.12, 5.12]$ for $i = 1..n$
    
    - la solucion que tenemos:
    
   ```
    [ 0.01357292  0.00305028  0.00353871 -0.00032503 -0.00053246  0.00213341
    -0.00402281  0.00668157  0.0123271   0.00122662] 
    fitness: -0.0843335201155675

   ```
   
 * **Function Griewank**
    - $f(x, y)=10n + \sum_{i=1}^{n}(x_i^2 - 10cos(2\pi x_i))$
    
    - su minima global esta: $f(\textbf{x}^{\ast})=0$ donde $\textbf{x}^{\ast} = (0, 0)$
    
     ![avatar](http://benchmarkfcns.xyz/benchmarkfcns/plots/griewankfcn.png)
    
    - bounds: $ x_i \in [-600, 600]$ for $i = 1..n$
    
    - la solucion que tenemos:
    
   ```
   [-1.63665742 -0.63387212  1.06524781 -2.93834095 -0.81735668 -0.84701633
    -0.60488459 -3.34330734 -2.21048473  0.91448804] 
    fitness: -1.007875167722615

   ```
   
   
   
 * **Function Schwefel 2.21**
    - $f(\mathbf{x})=f(x_1, ..., x_n)=\max_{i=1,...,n}|x_i|$
    
    - su minima global esta: $f(\textbf{x}^{\ast})=0$ donde $\textbf{x}^{\ast} = (0, 0)$
    
    ![avatar](http://benchmarkfcns.xyz/benchmarkfcns/plots/schwefel221fcn.png)
    
    - bounds: $ x_i \in [-100, 100]$ for $i = 1..n$
    
    - la solucion que tenemos:
    
   ```
   asdasdasdasdasd

   ```

 * **Function Schwefel 2.22**
    - $f(\mathbf{x})=f(x_1, ..., x_n)=\sum_{i=1}^{n}|x_i|+\prod_{i=1}^{n}|x_i|$
    
    - su minima global esta: $f(\textbf{x}^{\ast})=0$ donde $\textbf{x}^{\ast} = (0, 0)$
    
    ![avatar](http://benchmarkfcns.xyz/benchmarkfcns/plots/schwefel222fcn.png)
    
    - bounds: $ x_i \in [-100, 100]$ for $i = 1..n$
    
    - la solucion que tenemos:
    
   ```
   asdasdasdasdasd

   ```
   
   
 * **Function Schwefel 1.2**
    - $f(\textbf{x}) = f(x_1, x_2, ..., x_n) = 418.9829d -{\sum_{i=1}^{n} x_i sin(\sqrt{|x_i|})}.$
    
    - su minima global esta: $f(\textbf{x}^{\ast})=0$ donde $\textbf{x}^{\ast} = (420.9687, …, 420.9687)$
    
    ![avatar](http://benchmarkfcns.xyz/benchmarkfcns/plots/schwefelfcn.png)
    
    - bounds: $ x_i \in [-500, 500]$ for $i = 1..n$
    
    - la solucion que tenemos:
    
   ```
   asdasdasdasdasd

   ```
   
  
 * **Function Extended_f_10**
   
   
 * **Function bohachevsky 1.2**
    - $f(x, y) = x^2 + 2y^2 -0.3cos(3\pi x)-0.4cos(4\pi y)+0.7$
    
    - su minima global esta: $f(\textbf{x}^{\ast})=0$ donde $\textbf{x}^{\ast} = (0, 0)$
    
    ![avatar](http://benchmarkfcns.xyz/benchmarkfcns/plots/bohachevskyn1fcn.png)
    
    - bounds: $ x_i \in [-100, 100]$ for $i = 1, 2$
    
    - la solucion que tenemos:
    
   ```
   asdasdasdasdasd

   ```
* **Function Schaffer**
    - $f(x, y)=0.5 + \frac{sin^2(x^2+y^2)^2-0.5}{(1+0.001(x^2+y^2))^2}$
    
    - su minima global esta: $f(\textbf{x}^{\ast})=0$ donde $\textbf{x}^{\ast} = (0, 0)$
    
    ![avatar](http://benchmarkfcns.xyz/benchmarkfcns/plots/schaffern1fcn.png)
    
    - bounds: $ x_i \in [-100, 100]$ for $i=1, 2$
    
    - la solucion que tenemos:
    
   ```
   asdasdasdasdasd

   ```

