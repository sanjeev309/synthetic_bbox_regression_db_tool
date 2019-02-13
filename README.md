# Synthetic Bounding-Box Regression Database Tool

A Python tool to create synthetic bounding-box data for evaluation of continous regression techniques.

## Getting Started

- Clone the repo into your folder

    `git clone https://github.com/sanjeev309/synthetic_bbox_regression_db_tool.git`

- Open `main.py` and change values of TOTAL_IMAGES, IMAGE_DIMENSION and PADDING if required.
- Run the program using `python3 main.py`
- The Images and target co-ordinates are saved in numpy format in npy files `data.npy` and `target.npy` respectively.
- The images are stacked along the 0th axis in `data` whereas the corresponding index of `target` contains the 4 coordinates [x,y,w,h] 

    - where x,y are coodinates of top-left corner of rectange resp. 
    - where w,h are width and height of the rectangle resp.


### Prerequisites

Python3 and OpenCV 3.2


## Authors

* **Sanjeev Tripathi** - [LinkedIn](https://www.linkedin.com/in/sanjeev309/)


## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/sanjeev309/synthetic_bbox_regression_db_tool.git/blob/master/LICENSE.md) file for details