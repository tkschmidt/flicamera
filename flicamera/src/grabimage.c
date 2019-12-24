/*
 * !/usr/bin/env python
 *  -*- coding: utf-8 -*-
 *
 *  @Author: José Sánchez-Gallego (gallegoj@uw.edu)
 *  @Date: 2019-12-23
 *  @Filename: libfli_wrapper.cpp
 *  @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)
 */

#include "libfli.h"


int grab_frame(flidev_t dev, unsigned short *img, size_t n_cols, size_t n_rows) {

    int out;

    // if((img = (unsigned short*)malloc(n_rows * n_cols * sizeof(unsigned short))) == 0)
    // {
    //     return -1;
    // }

    for(int row = 0; row < n_rows; row++)
    {
        out = FLIGrabRow(dev, &img[row * n_cols], n_cols);
        if (out){
            return out;
        }
    }

    return 0;

}
