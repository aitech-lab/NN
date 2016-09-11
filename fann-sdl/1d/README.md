FANN + SDL binding
==================

Solution field visualisation for an simple NN model

![](./screenshoot.png)
![](./convergence.gif)

The functions are described with functions where

* x is the input to the activation function,
* y is the output,
* s is the steepness and
* d is the derivation.

FANN_LINEAR Linear activation function.

* span: -inf < y < inf
* y = x*s, d = 1*s
* Can NOT be used in fixed point.

FANN_THRESHOLD  Threshold activation function.

* x < 0 -> y = 0, x >= 0 -> y = 1
* Can NOT be used during training.

FANN_THRESHOLD_SYMMETRIC    Threshold activation function.

* x < 0 -> y = 0, x >= 0 -> y = 1
* Can NOT be used during training.

FANN_SIGMOID    Sigmoid activation function.

* One of the most used activation functions.
* span: 0 < y < 1
* y = 1/(1 + exp(-2*s*x))
* d = 2*s*y*(1 - y)

FANN_SIGMOID_STEPWISE   Stepwise linear approximation to sigmoid.

* Faster than sigmoid but a bit less precise.

FANN_SIGMOID_SYMMETRIC  Symmetric sigmoid activation function, aka. tanh.

* One of the most used activation functions.
* span: -1 < y < 1
* y = tanh(s*x) = 2/(1 + exp(-2*s*x)) - 1
* d = s*(1-(y*y))

FANN_SIGMOID_SYMMETRIC_STEPWISE Stepwise linear approximation to symmetric sigmoid.

* Faster than symmetric sigmoid but a bit less precise.

FANN_GAUSSIAN   Gaussian activation function.

* 0 when x = -inf, 1 when x = 0 and 0 when x = inf
* span: 0 < y < 1
* y = exp(-x*s*x*s)
* d = -2*x*s*y*s

FANN_GAUSSIAN_SYMMETRIC Symmetric gaussian activation function.

* -1 when x = -inf, 1 when x = 0 and 0 when x = inf
* span: -1 < y < 1
* y = exp(-x*s*x*s)*2-1
* d = -2*x*s*(y+1)*s

FANN_ELLIOT Fast (sigmoid like) activation function defined by David Elliott

* span: 0 < y < 1
* y = ((x*s) / 2) / (1 + |x*s|) + 0.5
* d = s*1/(2*(1+|x*s|)*(1+|x*s|))

FANN_ELLIOT_SYMMETRIC   Fast (symmetric sigmoid like) activation function defined by David Elliott

* span: -1 < y < 1
* y = (x*s) / (1 + |x*s|)
* d = s*1/((1+|x*s|)*(1+|x*s|))

FANN_LINEAR_PIECE   Bounded linear activation function.

* span: 0 <= y <= 1
* y = x*s, d = 1*s

FANN_LINEAR_PIECE_SYMMETRIC Bounded linear activation function.

* span: -1 <= y <= 1
* y = x*s, d = 1*s

FANN_SIN_SYMMETRIC  Periodical sinus activation function.

* span: -1 <= y <= 1
* y = sin(x*s)
* d = s*cos(x*s)

FANN_COS_SYMMETRIC  Periodical cosinus activation function.

* span: -1 <= y <= 1
* y = cos(x*s)
* d = s*-sin(x*s)

FANN_SIN    Periodical sinus activation function.

* span: 0 <= y <= 1
* y = sin(x*s)/2+0.5
* d = s*cos(x*s)/2

FANN_COS    Periodical cosinus activation function.

* span: 0 <= y <= 1
* y = cos(x*s)/2+0.5
* d = s*-sin(x*s)/2
