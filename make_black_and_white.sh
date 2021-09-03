#!/bin/bash

gs  -sOutputFile=black_and_white.pdf  -sDEVICE=pdfwrite  -sColorConversionStrategy=Gray  -dProcessColorModel=/DeviceGray  -dCompatibilityLevel=1.4  -dNOPAUSE  -dBATCH  $1

