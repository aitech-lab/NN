
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#include "cortex.h"

const unsigned int num_input  = 1;
const unsigned int num_layers = 3;
const unsigned int num_output = 1;
const unsigned int num_neurons_hidden = 20;
const unsigned int g_count = 10;

unsigned int num_train_data;

void generate_train_data();

double 
rnd(double s) {return (double)rand()/RAND_MAX*s;}


void
cortex_init(unsigned int size_of_train_data) {

    num_train_data = size_of_train_data;

    ann = fann_create_standard(
        num_layers,            
        num_input,          // 0 input
        // 1,                  // 1 hidden
        num_neurons_hidden, // 2 hidden
        // num_neurons_hidden, // 2 hidden
        num_output);        // 5 output
    
    // http://libfann.github.io/fann/docs/files/fann_data-h.html#fann_activationfunc_enum
    
    /*
        1) x 
        2) l1 = s*dot(x, L1)            
        4) l2 = exp(-dot(l1, L2)^2)
        5) y = sum(l2) 
    */
    // fann_set_activation_function_layer (ann, FANN_LINEAR  , 1); // hidden 1
    // fann_set_activation_steepness_layer(ann,      1e-6    , 1);
    fann_set_activation_function_layer (ann, FANN_GAUSSIAN, 1);   // hidden 2
    fann_set_activation_steepness_layer(ann,      1e-2    , 1);
    fann_set_activation_function_output(ann, FANN_LINEAR     );

    // fann_set_activation_function_hidden(ann, FANN_GAUSSIAN);
    // fann_set_learning_rate(ann, 0.00001);
    // fann_randomize_weights(ann, -100, 100);
    // fann_set_training_algorithm(ann, FANN_TRAIN_INCREMENTAL);

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
    data = fann_create_train(num_train_data, num_input, num_output);
    fann_type x, y;
    fann_type k[g_count][3];
    for(i=0; i<g_count; i++) {
        k[i][0] = rnd(1000.0)-500.0; // x offset
        k[i][1] = rnd(100.0)+20;    // width
        k[i][2] = rnd( 50.0)+50;    // height
    }
    
    for(i=0; i<num_train_data; i++) {
        x = (fann_type) i-num_train_data/2;
        y = 0;
        for(j=0; j<g_count; j++)
            y+=exp(-pow((x+k[j][0])/k[j][1], 2))*k[j][2];

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
