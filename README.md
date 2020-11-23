 Example Package
 =====================================




* **Function Sphere**
    - $f(\textbf{x}) = f(x_1, x_2, ..., x_n) = {\sum_{i=1}^{n} x_i^{2}}.$
   
    - su minima global esta:$f(\textbf{x}^{\ast})=0$ donde $\textbf{x}^{\ast} = (0, …, 0)$
    
     ![avatar](http://benchmarkfcns.xyz/benchmarkfcns/plots/spherefcn.png)
     
    - bounds: $x_i \in [-5.12, 5.12]$ for $i = 1..n$
    
    - la solucion que tenemos :
    ```
    [-0.00818072  0.11111143  0.05332875 -0.0282895   0.01149842 -0.02333086
    -0.01925091 -0.00604656 -0.00959379  0.04176625] 
    fitness: -0.018977087586905483
    ```
   
 
 * **Function Ackley**
    - $f(\textbf{x}) = f(x_1, ..., x_n)= -a.exp(-b\sqrt{\frac{1}{n}\sum_{i=1}^{n}x_i^2})-exp(\frac{1}{n}\sum_{i=1}^{n}cos(cx_i))+ a + exp(1)$
    
    - su minima global esta: $f(\textbf{x}^{\ast})=0$ donde $\textbf{x}^{\ast} = (0, …, 0)$
    
     ![avatar](http://benchmarkfcns.xyz/benchmarkfcns/plots/ackleyfcn.png)
     
    - bounds: $x_i \in [-32, 32]$ for $i = 1..n$
    
    - la solucion que tenemos:
    ```
    [-0.01337104  0.00378951  0.00671465  0.00461864 -0.01431343  0.01159774
    -0.00041528  0.00478414  0.00542893  0.00308027] 
    fitness: -0.03603606025219763
    ```
 
* **Function Rosenbrock**
    - $f(x, y)=\sum_{i=1}^{n}[b (x_{i+1} - x_i^2)^ 2 + (a - x_i)^2]$
    
    - su minima global esta: $f(\textbf{x}^{\ast})=0$ donde $\textbf{x}^{\ast} = (1, …, 1)$
    
     ![avatar](http://benchmarkfcns.xyz/benchmarkfcns/plots/rosenbrockfcn.png)
    
    - bounds: $x_i \in [-5, 10]$ for $i = 1..n$
    
    - la solucion que tenemos:
    ```
    [-2.01295544e+00 -2.00318632e+00  1.44479825e-03 -2.02127134e+00
    -2.04204708e+00  8.07145638e-02  1.63757233e-01 -2.35384226e+00
    8.39914142e-01  2.38744252e+00] 
    fitness: -0.9649353905764941
  
  
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
   [-0.04560432  0.24343054 -0.33134579 -0.20688494  0.1855236  -0.24691806
    -0.30072995  0.0131173  -0.47835121  0.26264957] 
    fitness: -0.4783512141489581

   ```

 * **Function Schwefel 2.22**
    - $f(\mathbf{x})=f(x_1, ..., x_n)=\sum_{i=1}^{n}|x_i|+\prod_{i=1}^{n}|x_i|$
    
    - su minima global esta: $f(\textbf{x}^{\ast})=0$ donde $\textbf{x}^{\ast} = (0, 0)$
    
    ![avatar](http://benchmarkfcns.xyz/benchmarkfcns/plots/schwefel222fcn.png)
    
    - bounds: $ x_i \in [-100, 100]$ for $i = 1..n$
    
    - la solucion que tenemos:
    
   ```
   [ 0.5630586  -0.8778864  -2.36791013 -1.91646273  4.32366397  1.243555
    -0.13521534  0.73974573 -0.36022494 -0.28107385] 
    fitness: -1.007845579473045

   ```
   
   
 * **Function Schwefel 1.2**
    - $f(\textbf{x}) = f(x_1, x_2, ..., x_n) = 418.9829d -{\sum_{i=1}^{n} x_i sin(\sqrt{|x_i|})}.$
    
    - su minima global esta: $f(\textbf{x}^{\ast})=0$ donde $\textbf{x}^{\ast} = (420.9687, …, 420.9687)$
    
    ![avatar](http://benchmarkfcns.xyz/benchmarkfcns/plots/schwefelfcn.png)
    
    - bounds: $ x_i \in [-500, 500]$ for $i = 1..n$
    
    - la solucion que tenemos:
    
   ```
   [ 0.62319837 -0.73560384  0.28831212 -0.41259132 -0.00641023  0.70275989
    -0.75575393  0.3279226  -0.19957433  0.198604  ] 
    fitness: -0.8761325390587813

   ```
   
  
 * **Function Extended_f_10**
   
   
 * **Function bohachevsky 1.2**
    - $f(x, y) = x^2 + 2y^2 -0.3cos(3\pi x)-0.4cos(4\pi y)+0.7$
    
    - su minima global esta: $f(\textbf{x}^{\ast})=0$ donde $\textbf{x}^{\ast} = (0, 0)$
    
    ![avatar](http://benchmarkfcns.xyz/benchmarkfcns/plots/bohachevskyn1fcn.png)
    
    - bounds: $ x_i \in [-100, 100]$ for $i = 1, 2$
    
    - la solucion que tenemos:
    
   ```
    [-0.02571173 -0.00842974 -0.01202293  0.02523098  0.04017672 -0.06709364
    0.00889741 -0.02672166 -0.08121992 -0.03592722] 
    fitness: -0.70623177179338

   ```
* **Function Schaffer**
    - $f(x, y)=0.5 + \frac{sin^2(x^2+y^2)^2-0.5}{(1+0.001(x^2+y^2))^2}$
    
    - su minima global esta: $f(\textbf{x}^{\ast})=0$ donde $\textbf{x}^{\ast} = (0, 0)$
    
    ![avatar](http://benchmarkfcns.xyz/benchmarkfcns/plots/schaffern1fcn.png)
    
    - bounds: $ x_i \in [-100, 100]$ for $i=1, 2$
    
    - la solucion que tenemos:
    
   ```
    [-0.00071607 -0.00710123 -0.00116371 -0.01384613 -0.00973399  0.01484788
    0.00604145 -0.00321972  0.00067127 -0.00734846] 
    fitness: -0.9990715308450793

   ```

