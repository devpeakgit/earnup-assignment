![Logo](https://earnup.com/wp-content/uploads/2023/07/EarnUp-logo.png)
Hi Earnup Engineering 👋,

I hope this reaches you well and you can get this running ok. I'd do more but the time limit is coming close.
I've already some thoughts of how this an be improved. Any questions or issues please reach out.

All the best,
Will


# To run api server
Within a new virtual env do a pip install
>pip install -r requirements.txt

Then to run the api server
>uvicorn main:app --host 0.0.0.0 --port 8000

# To make a request using curl 
> curl --location 'localhost:8000/generate_sets' --header 'Content-Type: application/json' --data '[
    {
        "id": 1,
        "shape": 1,
        "color": 1,
        "shade": 1,
        "number": 1
    },
    {
        "id": 2,
        "shape": 2,
        "color": 2,
        "shade": 2,
        "number": 2
    },
    {
        "id": 3,
        "shape": 3,
        "color": 3,
        "shade": 3,
        "number": 3
    },
    {
        "id": 4,
        "shape": 1,
        "color": 1,
        "shade": 1,
        "number": 2
    },
    {
        "id": 5,
        "shape": 1,
        "color": 1,
        "shade": 1,
        "number": 3
    }
]'
