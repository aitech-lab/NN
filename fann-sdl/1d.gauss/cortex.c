
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#include "cortex.h"

const unsigned int num_input  = 1;
const unsigned int num_layers = 3;
const unsigned int num_output = 1;
const unsigned int num_neurons_hidden = 20;
const unsigned int g_count = 10;

unsigned int train_size = 200;

void generate_train_data();

double 
rnd(double s) {
    return (double)rand()/RAND_MAX*s;
}

unsigned int
cortex_train_size(){
    return train_size;
}

void
cortex_init() {

    ann = fann_create_standard(
        num_layers,            
        num_input,          // 0 input
        // 1,                  // 1 hidden
        num_neurons_hidden, // 2 hidden
        // num_neurons_hidden, // 2 hidden
        num_output);        // 5 output
    
    // http://libfann.github.io/fann/docs/files/fann_data-h.html#fann_activationfunc_enum

    fann_set_activation_function_layer (ann, FANN_GAUSSIAN, 1);   // hidden 2
    fann_set_activation_function_output(ann, FANN_LINEAR     );

    // status
    fann_print_connections(ann);
    // fann_print_parameters(ann);
    data = NULL;
    generate_train_data();
}

void
generate_train_data(){
    
    if(data) fann_destroy_train(data);

    unsigned int i,j;
    data = fann_create_train(train_size, num_input, num_output);
    fann_type x, y;
    fann_type k[g_count][3];
    for(i=0; i<g_count; i++) {
        k[i][0] = rnd(1.00)-0.50; // x offset
        k[i][1] = rnd(0.20)+0.10; // width
        k[i][2] = rnd(1.00)-0.50; // height
    }
    
    for(i=0; i<train_size; i++) {
        x = (fann_type) rnd(2.0)-1.0;
        y = 0.0;
        for(j=0; j<g_count; j++)
            y+= k[j][2] * exp(-pow((x+k[j][0])/k[j][1], 2)) + rnd(0.02);

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
    generate_train_data();
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
