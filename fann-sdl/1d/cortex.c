
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#include "cortex.h"

const unsigned int num_input  = 1;
const unsigned int num_layers = 3;
const unsigned int num_output = 1;
const unsigned int num_neurons_hidden = 9;

unsigned int num_train_data;

void
cortex_init(unsigned int train_data) {

    num_train_data = train_data;

    ann = fann_create_standard(
        num_layers,            
        num_input,          // 0 input
        num_neurons_hidden, // 1 hidden
        // num_neurons_hidden, // 2 hidden
        // num_neurons_hidden, // 2 hidden
        num_output);        // 5 output

    // FANN_SIGMOID_SYMMETRIC
    fann_set_activation_function_hidden(ann, FANN_GAUSSIAN);
    // fann_set_activation_function_layer(ann, FANN_SIGMOID, 0);
    // fann_set_activation_function_layer(ann, FANN_GAUSSIAN,1);
    fann_set_activation_function_output(ann, FANN_LINEAR);

    // fann_set_learning_rate(ann, 0.00001);
    // fann_randomize_weights(ann, -100, 100);
    // fann_set_training_algorithm(ann, FANN_TRAIN_INCREMENTAL);

    // status
    fann_print_connections(ann);
    // fann_print_parameters(ann);

    unsigned int i;
    data = fann_create_train(num_train_data, num_input, num_output);
    fann_type x, y;
    for(i=0; i<num_train_data; i++) {
        x = (fann_type) i-num_train_data/2;
        y = exp(-pow((x+200.0)/ 50, 2))*150 + 
            exp(-pow((x+100.0)/100, 2))*100 +
            exp(-pow((x+350.0)/100, 2))* 50 +
            exp(-pow((x-100.0)/250, 2))*200;
        data->input[i][0]  = x;
        data->output[i][0] = y;
    }
}

void
cortex_train() {
    // float mse = fann_get_MSE(ann);
    // printf("%f\n", mse);
    // fann_print_connections(ann);
    fann_shuffle_train_data(data);
    fann_train_epoch(ann, data);
    // fann_cascadetrain_on_data(ann,data,100,1,0.001);
}

void
cortex_randomize() {
    fann_randomize_weights(ann, -1.0, 1.0);
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
