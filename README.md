# trustar-coding-challenge
TruSTAR Software Engineering Questionnaire

# Description
The `extractors` package contains the functionality to extract the data from a json.

As example of what the package does, here some code to ilustrate the output.

INPUT:
```python
> from extractors.dot_notation import get_data
> a= '{
        "guid": "1234",
        "content": {
            "type": "text/html",
            "title": "Challenge 1",
            "entities": [ "1.2.3.4", "wannacry", "malware.com"]
        },
        "score": 74,
        "time": 1574879179
}'

> b = ["guid", "content.entities[0]", "score", "score.sign"]
```
OUTPUT:
```python
> get_data(a,b)
{ "guid": "1234", "content.entities[0]": "1.2.3.4", "score": 74 }
```

The package also support arrayed nested properties like `content.entities[0]`.

The `app.py` file is a Flask sample application to demonstrate the use of the package.

# Running the tests
```
python -m unittest discover
```

# Running the app locally
Some prerequisites before start:
- Clone this repo.
- Create a virtual environment for the app.

If you have a [github access token](https://github.com/settings/apps) (not required) export the `GITHUB_ACCESS_TOKEN` environment variable

```
export GITHUB_ACCESS_TOKEN=<your-access-token>
```

Install the dependencies:

```
pip install -r requirements.txt
```

Run the sample app.

```
python app.py
```

Visit `http://localhost:8000/` to see the results.

# If you prefer run this on docker, here the steps

### Build the image
```
docker image build --build-arg GITHUB_ACCESS_TOKEN=<your-access-token> -t itrustar .
```

> If you don't have a Github Token, It doesn't matter, the app also works without it. Just remove the `--build-arg GITHUB_ACCESS_TOKEN=<your-access-token>` param from the command above.

### Run the container
```
docker container run -p 8000:8000 --name ctrustar itrustar
```

Visit `http://localhost:8000/` to see the results.


# Important
The application will take its time to present the final results, it all depends on how many files are in the repo.