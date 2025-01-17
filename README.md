# IMP-IPFE-FullySecure

## Scheme

The following project implements the fully secure Inner Product Functional Encryption Scheme under the DDH assumption as described on p.9/10 of the following paper

* [Fully Secure Functional Encryption for Inner Products, from Standard Assumptions](https://eprint.iacr.org/2015/608.pdf)

## Structure

* [ipfefullysec.py](./ipfefullysec.py) contains the implementation of the scheme
* [ipfehelpers.py](./ipfehelpers.py) helper functions used by the scheme
* [benchmark.py](./benchmark.py) calls the scheme in different ways and provides benchmarks

## Prerequisites

* Docker or Podman (if using podman replace the "docker" with "podman" in the instructions below)

## Usage

Clone the repository

```shell
git clone https://github.com/karimib/imp-ipfe-fullysecure-demo-charm.git
cd imp-ipfe-fullysecure-demo-charm
```

Build the image (assuming your in the root directory)

```shell
docker build -t ipfefsdemo:v1 .
```

Create a container from the image

```shell
docker run ipfefsdemo:v1 
```

Mount a volume to save benchmark csv (if)

````shell
docker run -v "${PWD}/results:/data" ipfefsdemo:v1 
````

## Benchmarking

The [benchmark.py](./benchmark.py) file contains two methods for benchmarking

| Method | Description |
| --- | --- |
| simulate_increasing_bits() | Compare the timings when increasing the security parameter (in bits) that instantiates the cyclic group G of prime order |
| simulate_increasing_length() | Compare the timings when increasing the length of the input vectors x and y|

to run them you have to uncomment line 161 and line 162 and build a new image as follows:

Build the image

```shell
docker build -t ipfefsdemo:v1 .
```

Then mount a volume to save the benchmark csv to your disk: 

````shell
docker run -v "${PWD}/results:/data" ipfefsdemo:v1 
````
