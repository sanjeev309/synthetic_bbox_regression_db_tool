# Synthetic Bounding-Box Regression Database Tool

A Python tool to create synthetic bounding-box data for evaluation of continous regression techniques.

## Getting Started

- Clone the repo into your folder

    `git clone https://github.com/sanjeev309/synthetic_bbox_regression_db_tool.git`

- Open `main.py` and change values of TOTAL_IMAGES, IMAGE_DIMENSION and PADDING if required.
- Run the program using `python3 main.py`

- The Images and target co-ordinates are saved in numpy format in npy files `data.npy` and `target.npy` respectively.
- The images are stacked along the 0th axis in `data` whereas the corresponding index of `target` contains the 4 coordinates [x1, y1, x2, y2]

    - where x1,y1 are co-ordinates of top-left corner of rectange res.
    - where x2,y2 are co-ordinates of bottom-right corner of rectange res.


### Prerequisites

Python3 and OpenCV 3.2

### Data Structure

##### data.npy

![](https://imgur.com/Vix8EF9.jpg)

##### target.npy

![](https://imgur.com/lOG8cNQ.jpg)

### Sample Data

Data :

![](https://imgur.com/aY3zw9G.jpg)

Target :

`[0.37, 0.31, 0.91, 0.81]`

## Author

* **Sanjeev Tripathi** - [LinkedIn](https://www.linkedin.com/in/sanjeev309/)


## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/sanjeev309/synthetic_bbox_regression_db_tool.git/blob/master/LICENSE.md) file for details
