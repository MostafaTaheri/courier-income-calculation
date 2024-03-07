# courier-income-calculation
Various factors affect the income of couriers. In this task, we want to identify and implement the relevant models and then calculate the salaries of couriers in 2 time scales.

## Installation

You need to install some packages.

To install using ```pip```:

```bash
pip install -r requirements/requirements.txt
```

## Run Test
```bash
python manage.py test income_calculation.tests.daily
```

## Calculating the daily salary of couriers
We want to add a new table to the system entities that shows the salary of a courier on a certain date. The rows of this table are actually the aggregated information of the previous tables for each driver on each day. The rows of this table must be referable at any time. That is, with the first activity of each courier every day, the corresponding row should be created and the value of this row should be updated as soon as each of the items mentioned above is created.

#### API endpoint:
* ``POST api/v1/earning/income-item/``

#### Body example:
``` python
{
    "courier": 1,
    "amount": 500
}
```

#### Response:
``` python
{
    "courier": {
        "id": 1,
        "user": {
            "id": 1,
            "email": "mm@gmail.com"
        }
    },
    "amount": 500,
    "date": "2024-03-06T00:00:00"
}
```

## Calculation of couriers' weekly salary
The main users of the previous table are couriers. For the operation team that makes weekly payments, it is necessary to have a table in which the Saturday date of each week and the total daily earnings of each courier in that week are known. This model is actually an aggregate of the daily salary model.
For this model, a view needs to be added to display the list of records in this table. For this view, consider the query parameters from_date, to_date. The final result of this view is an array of all the rows of this table whose date (Saturday date) is placed in the [from_date, to_date] range.

#### API endpoint:
* ``GET api/v1/earning/weekly/?from_date={date}&to_date={date}``

#### Response:
``` python
[
    {
        "courier": {
            "id": 1,
            "user": {
                "id": 1,
                "email": "mm@gmail.com"
            }
        },
        "amount": 8000.0,
        "start_date": "2022-03-26T00:00:00"
    },
    {
        "courier": {
            "id": 1,
            "user": {
                "id": 1,
                "email": "mm@gmail.com"
            }
        },
        "amount": -500.0,
        "start_date": "2022-04-02T00:00:00"
    }
]
```