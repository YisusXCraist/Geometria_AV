#  🧮 Analytic Vectorial Geometry  🚀

This is an open-source Python library for performing operations with vectors in 3-dimensional space. The library provides functions for defining vectors, performing arithmetic operations with vectors (addition, subtraction, scalar multiplication), and computing the dot product and cross product of two vectors.

## Installation 💻

To use this library, you can clone the repository from GitHub:

bash
git clone https://github.com/username/analytic-vectorial-geometry.git

## Usage 🧐

To use the library in your own Python code, you can import the Vector module:

```python
from Vector import Vector

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

```

## Add two vectors ➕
```python
v3 = v1 + v2

```
## Subtract two vectors ➖
```python
v4 = v1 - v2
```

## Multiply a vector by a scalar ✖️
```python
v5 = v1 * 2
```
## Compute the dot product of two vectors ⚫️
```python
dot_product = v1.dot(v2)
```

## Compute the cross product of two vectors ✖️➖✔️
```python
v6 = v1.cross(v2)
```

## Testing 🧪

This repository also includes a test suite for the Vector module. To run the tests, you can use the following command:

```python
Tests.py
```

The tests include checks for addition, subtraction, scalar multiplication, dot product, and cross product operations. The test suite also includes 3D plots of the vectors, which can be used to visually verify the results of the operations.

## Contributing 🤝

Contributions to this library are welcome. To contribute, please fork the repository and submit a pull request with your changes. Be sure to include tests for any new functionality you add.

## License 📝

This library is licensed under the MIT License. See the LICENSE file for details.