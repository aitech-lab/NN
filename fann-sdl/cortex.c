
#include <stdlib.h>
#include <stdio.h>

#include "cortex.h"

const unsigned int num_input  = 2;
const unsigned int num_layers = 3;
const unsigned int num_output = 1;
const unsigned int num_neurons_hidden = 9;

unsigned int num_train_data;

void
cortex_init(unsigned int train_data) {

    num_train_data = train_data;

    ann = fann_create_standard(
        num_layers,            
        num_input,          // 1 input
        num_neurons_hidden, // 2 hidden
        // num_neurons_hidden, // 2 hidden
        // num_neurons_hidden, // 2 hidden
        num_output);        // 5 output

    fann_set_activation_function_hidden(ann, FANN_SIGMOID_SYMMETRIC);
    fann_set_activation_function_output(ann, FANN_SIGMOID_SYMMETRIC);
    // fann_randomize_weights(ann, -100, 100);
    // fann_set_training_algorithm(ann, FANN_TRAIN_INCREMENTAL);
    // fann_set_learning_rate(ann, 0.001);

    // status
    fann_print_connections(ann);
    // fann_print_parameters(ann);

    unsigned int i;
    data = fann_create_train(num_train_data, num_input, num_output);
    for(i=0; i<num_train_data; i++) {
        fann_type x = (fann_type) rand()/RAND_MAX*2.0-1.0;
        fann_type y = (fann_type) rand()/RAND_MAX*2.0-1.0;
        data->input[i][0] = x;
        data->input[i][1] = y;
        // data->input[i][2] = x*x;
        // data->input[i][3] = y*y;
        // data->input[i][4] = x*x*x;
        // data->input[i][5] = y*y*y;
        
        double sq = x*x+y*y;
        data->output[i][0] = (fann_type)( sq > 0.6 ? 1.0 :-1.0);
        // data->output[i][0]*= x*y > 0 ? 1.0: -1.0;
        
        // data->output[i][0] = (fann_type)( sq < 2000 && sq > 500? 1: -1);
        // data->output[i][0] = ((int)(abs(x*3))%2)^((int)(abs(y*3))%2) ? 1 : -1;
        // data->output[i][0] = (fann_type)( x+y > 0 ? 1 : -1);
    }
    // fann_scale_train_data(data,-1.0, 1.0);
}

void
cortex_train() {
    float mse = fann_get_MSE(ann);
    printf("%f\n", mse);
    // fann_print_connections(ann);
    fann_shuffle_train_data(data);
    fann_train_epoch(ann, data);
    // fann_cascadetrain_on_data(ann,data,100,1,0.001);
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
