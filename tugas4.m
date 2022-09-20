s = tf('s')
T = 1;

num = 1;
den = [T T/16 1];

Kp = 1;
Td = 3;
Kd = Kp*Ti;

sys = tf(num, den);
sys_c = tf([Kp, Kd], [1, 0]);
function = feedback(sys*sys_c, 1);

figure
subplot(311), step(function*s);   
stepinfo(function*s)
subplot(312), step(function);      
stepinfo(function)
subplot(313), step(function / s); 
stepinfo(function/s)