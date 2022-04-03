# A* algorithm
 
---
**What is A star search algoritm?**
A* is a graph traversal and path search algorithm. It is popular for finding a path on a grid. Many games and web-bases maps use this algorithm to find the shortest path very efficiently.

**Example**
![A star Map](static\image.png)

**About this implementation**

In this implementation core functionality has a Field class. Each field on a grid is a Field class object. Those object are binded in a array of object that visualization is showed in the picture above.   


--- 
### Core Technologies
- Python
- numpy
- matplotlib
- fastAPI
- pydatnic 
---
### The APP is hosted [here](https://fastapi-a-star.herokuapp.com/). 

---
The **documentation** of the api can be found in [here](https://fastapi-a-star.herokuapp.com/docs)

---
### Setup

- clone repository\
`git clone https://github.com/KostkaMateusz/Astar.git`

- create virtual environment\
`python -m venv venv`

- install packages from requirements.txt\
`pip install -r requirements.txt`

- Start fastAPI server\
`uvicorn app.main:app --reload` 

