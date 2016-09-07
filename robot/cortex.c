
#include <stdlib.h>
#include <stdio.h>

#include "cortex.h"

const unsigned int num_input  = 2;
const unsigned int num_layers = 3;
const unsigned int num_output = 1;
const unsigned int num_neurons_hidden = 5;
const unsigned int num_train_data     = 10;

void
cortex_init() {

    ann = fann_create_standard(
        num_layers, 
        num_input, 
        num_neurons_hidden,
        num_output);
    fann_set_activation_function_hidden(ann, FANN_SIGMOID);
    fann_set_activation_function_output(ann, FANN_SIGMOID);
    fann_set_learning_rate(ann, 0.1);

    unsigned int i;
    data = fann_create_train(num_train_data, num_input, num_output);
    for(i=0; i<num_train_data; i++) {
        fann_type x = (fann_type) rand()/RAND_MAX*100;
        fann_type y = (fann_type) rand()/RAND_MAX*100;
        data->input[i][0] = x;
        data->input[i][1] = y;
        data->output[i][0] = (fann_type)(x>50 ? 1 : -1);
    }
}

void
cortex_train() {
    fann_shuffle_train_data(data);
    fann_train_epoch(ann, data);
}

fann_type*
cortex_run(fann_type* data) {
    return fann_run(ann, data);
}

void
cortex_destroy() {
    fann_destroy(ann);
    fann_destroy_train(data);
}

/*
int main(int argc, char** argv) {
    cortex_init();
    cortex_destroy();
    return 0;
}
*/
