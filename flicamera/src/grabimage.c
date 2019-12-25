/*
 * !/usr/bin/env python
 *  -*- coding: utf-8 -*-
 *
 *  @Author: José Sánchez-Gallego (gallegoj@uw.edu)
 *  @Date: 2019-12-23
 *  @Filename: libfli_wrapper.cpp
 *  @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)
 */

#include <stdio.h>
#include "libfli.h"


int grab_frame(flidev_t dev, size_t n_cols, size_t n_rows) {

    int out;

    unsigned short *img2;
    // unsigned short img2[(size_t)(n_cols * n_rows)];
    if((img2 = (unsigned short*)malloc(n_rows * n_cols * sizeof(unsigned short))) == 0)
    {
        free(img2);
        return -1;
    }

    // for(int row = 0; row < n_rows; row++)
    // {
    //     out = FLIGrabRow(dev, &img2[row * n_cols], n_cols);
    //     if (out) {
    //         return out;
    //     }
    // }

    return 0;

}
