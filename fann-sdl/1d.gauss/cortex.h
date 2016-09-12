#pragma once

#include "doublefann.h"

struct fann* ann;
struct fann_train_data* data;

void cortex_init();
void cortex_destroy();

unsigned int cortex_train_size();
void cortex_train();
fann_type* cortex_run(fann_type* data);
void cortex_randomize();