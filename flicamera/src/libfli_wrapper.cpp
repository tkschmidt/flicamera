/*
 * !/usr/bin/env python
 *  -*- coding: utf-8 -*-
 *
 *  @Author: José Sánchez-Gallego (gallegoj@uw.edu)
 *  @Date: 2019-12-23
 *  @Filename: libfli_wrapper.cpp
 *  @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)
 */

#include <pybind11/pybind11.h>
#include "libfli.h"


namespace py = pybind11;


// int connect() {

//     int strSize = 1024;
//     char buff[strSize];
//     int out;

//     out = FLIGetLibVersion(buff, strSize);
//     if (out)
//     {
//         printf("Unable to retrieve library version!\n");
//         return out;
//     }
//     printf("Library version '%s'\n", buff);

// }


grab_frame(size_t n_cols, size_t n_rows){

    unsigned short out;
    unsigned short *img;

    if((img = (unsigned short*)malloc(n_rows * n_cols * sizeof(unsigned short))) == NULL)
    {
        return -1;
    }

    for(int row = 0; row < n_rows; row++)
    {
        out = FLIGrabRow(dev, &img[row * n_cols], n_cols);
        if (out){
            return out;
        }
    }

    return std::make_tuple(err, img);


PYBIND11_MODULE(fliwrapper, m) {
    m.def("grab_frame", &grab_frame);
}
