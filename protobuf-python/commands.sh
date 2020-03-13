#!/bin/bash
SRC_DIR=proto
echo $SRC_DIR

protoc -I=$SRC_DIR --python_out=message/ $SRC_DIR/sample_message.proto
protoc -I=$SRC_DIR --python_out=enums/ $SRC_DIR/sample_enum.proto
protoc -I=$SRC_DIR --python_out=complex-message/ $SRC_DIR/sample_complex_message.proto
