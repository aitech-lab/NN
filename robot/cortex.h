#pragma once

#include "fann.h"

struct fann* ann;
struct fann_train_data* data;

void cortex_init();
void cortex_destroy();

void cortex_train();
fann_type* cortex_run(fann_type* data);