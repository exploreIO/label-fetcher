# Label Fetcher

This project is designed to fetch addresses from a website that were sold and transfer it into a Word Doc, therefore too label it.

### Prerequisits

- Python 3.10
- Virtual Env (Optional)

# Get Started

First, go to your project directory:

```
./label-fetcher
```

Make a Virtual Environment to keep dependencies within your project:

```
python -m virtualenv env
```

Now activate it:

```
./env/Scripts/activate.bat
``` 

or

```   
. env/Scripts/activate
```

Next, download the necessary dependencies to run this program:

```
pip install -r requirements.txt
```

To finally utilize this program, run:

```
python run.py
```

You will have the option to put a American zipcode you desire, as well as to pick how far you would like to go back to the addresses sold in the past.