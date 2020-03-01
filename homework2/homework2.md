# Homework2

### P8
a.3M/150K = 20 So it can support 20 users.


b.p = 0.1


c. 
<a href="https://www.codecogs.com/eqnedit.php?latex=\binom{n}{120}*&space;0.1^{n}&space;*&space;0.9^{120-n}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\binom{n}{120}*&space;0.1^{n}&space;*&space;0.9^{120-n}" title="\binom{n}{120}* 0.1^{n} * 0.9^{120-n}" /></a>


d.<a href="https://www.codecogs.com/eqnedit.php?latex=P&space;=&space;1-\sum_{n=1}^{20}\binom{n}{120}0.1^{n}*0.9^{120-n}=0.0079" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P&space;=&space;1-\sum_{n=1}^{20}\binom{n}{120}0.1^{n}*0.9^{120-n}=0.0079" title="P = 1-\sum_{n=1}^{20}\binom{n}{120}0.1^{n}*0.9^{120-n}=0.0079" /></a>

### P21
a.if use one path, the max throughput is <a href="https://www.codecogs.com/eqnedit.php?latex=max\{&space;min\{R_{1}^{1},R_{2}^{1},...,R_{N}^{1}\},min\{R_{1}^{2},R_{2}^{2},...,R_{N}^{2}&space;\}.....min\{&space;R_{1}^{M},R_{2}^{M},...,R_{N}^{M}\}&space;\}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?max\{&space;min\{R_{1}^{1},R_{2}^{1},...,R_{N}^{1}\},min\{R_{1}^{2},R_{2}^{2},...,R_{N}^{2}&space;\}.....min\{&space;R_{1}^{M},R_{2}^{M},...,R_{N}^{M}\}&space;\}" title="max\{ min\{R_{1}^{1},R_{2}^{1},...,R_{N}^{1}\},min\{R_{1}^{2},R_{2}^{2},...,R_{N}^{2} \}.....min\{ R_{1}^{M},R_{2}^{M},...,R_{N}^{M}\} \}" /></a> 


b.if use all the paths, the max throughput is <a href="https://www.codecogs.com/eqnedit.php?latex=\sum_{k=1}^{M}&space;min\{R_{1}^{k},R_{2}^{k},...,R_{N}^{k}\}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sum_{k=1}^{M}&space;min\{R_{1}^{k},R_{2}^{k},...,R_{N}^{k}\}" title="\sum_{k=1}^{M} min\{R_{1}^{k},R_{2}^{k},...,R_{N}^{k}\}" /></a>

### P23
a.Because the speed of the bottleneck link is R pbs, and the first link is the bottleneck link, the time is<a href="https://www.codecogs.com/eqnedit.php?latex=L/R_{s}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?L/R_{s}" title="L/R_{s}" /></a>


b.
if Rc = 0 , the second pack will surely line up before the second link. T = L/Rc-L/Rs.
