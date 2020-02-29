# protocol_buffers

Google Protobuf with examples and exercises

## Project layout

The `basics` folder is an introduction to protobuf: 
- 1 Defining scalar types
- 2 Creating multiple messages for one file
- 3 Making use of imports and nested messages
- 4 Making use of imports & packages

The `various-implementation-methods` folder shows the 4 different implementation designs to solve the same problem:
- 1 Same file
- 2 Nested messages
- 3 Making use of imports
- 4 Making use of imports & packages

The `coding` folder shows how to run the Protoc Compiler (see Setup Protoc Compiler)

The `protobuf-python` folder contains Python packages for implementing protobuf

## Getting started

Feel free to make use of VScode and setup a Python VM. This examples covers MacOSX and Linux.

- Clone repository
- Setup Protoc Compiler 
- Install [VSCode extensions](https://code.visualstudio.com/docs/editor/extension-gallery#_browse-and-install-extensions) `vscode-proto3`  & `Clang-Format`  (if you want to format your files automatically)
- Install [Python](https://www.python.org/)
- Install Python virtualenv
- Alternatively, you can use [Python IDE PyCharm](https://www.jetbrains.com/pycharm/download/)

### Setup Protoc Compiler

Generate code automatically from a protocol buffer file into any language. 

#### MacOSX
In order to perform code generation, you will need to install `protoc`  on your computer.
It is actually very easy, open a command line interface and type `brew install protobuf` 

#### Ubuntu (Linux) 
Find the correct protocol buffers version based on your [Linux Distro](https://github.com/google/protobuf/releases)


### Install Python virtualenv

These steps should be familiar if you're familiar with python; if you're not, here's a brief guide to installing:

- Create a virtualenv to hold the project (`python3 -m venv ~/.virtualenvs/protobuf`)
- List virtual environments to verify all OK (`lsvirtualenv`)
- Activate using `workon protobuf`
- Install the project into that virtualenv in development mode: `pip3 install -e .`
- Use `deactivate` to leave the virtual environment.

### Running code

Generate a single protocol buffer file using Python:
- cd `coding`
- Type `protoc` to get a list of supported coding languages
- Running for Python:
```protoc -I=<PATH_OF_SOURCE_PROTO_FILES> --python_out=<OUT_DIR> <FOLDER>/<FILE>.proto```
Example: ```protoc -I=proto --python_out=python proto/example.proto```

Generate multiple protocol buffer files using Python:
- cd `protobuf-python`
- Install dependencies to virtualenv
`pip3 install requirements.txt`
- Generate code automatically from protocol buffer, use `command.sh` to genereate this
- Run the `simple_demo.py` file to explore how we (write / read) serialize & de-serialize .proto files

## Source

- [source code](https://github.com/simplesteph/protobuf-example-python)
- [Google doc's for protocol buffers (Python)](https://developers.google.com/protocol-buffers/docs/pythontutorial)
- [Google doc's for types](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf)
- [Google doc's for style guide](https://developers.google.com/protocol-buffers/docs/style)
- [Uber style guidelines](https://github.com/uber/prototool/blob/dev/etc/style/uber1/uber1.proto)  to achieve consistency in how you write your .proto  
- [Protobufs made by Google](https://github.com/google/protobuf/tree/master/examples)
- [Google Apis types](https://github.com/googleapis/googleapis/tree/master/google/type)
- [Protocol Buffer itself](https://github.com/google/protobuf/tree/master/src/google/protobuf)  (may be very complex) 
