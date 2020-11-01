# trustar-coding-challenge
TruSTAR Software Engineering Questionnaire

The `poc_app.py` file is an sample application that uses the package (`extractors`).

The package has a function that receives a json-string and a list of properties, expressed in dot notation, to extract from the json-string.

## Running the app
Some prerequisites before start:
- You should have created a virtual environment for the app.
- You should have a [github access token](https://github.com/settings/apps) created for you.

Export the GITHUB_ACCESS_TOKEN environment variable

`export GITHUB_ACCESS_TOKEN=<your-access-token>`

Install the dependencies:

`pip install -r requirements.txt`

Run the sample app.

`python app.py`


## If you prefer run this on docker, here the steps

### build the image
`docker image build --build-arg GITHUB_ACCESS_TOKEN=<your-access-token> -t itrustar .`

> If you don't have a Github Token, It doesn't matter, the app also works without it. Just remove the `--build-arg GITHUB_ACCESS_TOKEN=<your-access-token>` param from the command above.

### Run the container
`docker container run -p 8000:8000 --name ctrustar itrustar`

Visit `http://localhost:8000/` to see the results.


# Important
The application will take its time to present the final results, it all depends on how many files are in the repo.