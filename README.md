# trustar-coding-challenge
TruSTAR Software Engineering Questionnaire

The `extractors` package contains the functionality to extract the data from a json.

The `app.py` file is a Flask sample application to demonstrate the use of the package.

# Running the app locally
Some prerequisites before start:
- Clone this repo.
- Create a virtual environment for the app.

If you have a [github access token](https://github.com/settings/apps) (not required) export the `GITHUB_ACCESS_TOKEN` environment variable

`export GITHUB_ACCESS_TOKEN=<your-access-token>`

Install the dependencies:

`pip install -r requirements.txt`

Run the sample app.

`python app.py`

Visit `http://localhost:8000/` to see the results.

# If you prefer run this on docker, here the steps

### Build the image
`docker image build --build-arg GITHUB_ACCESS_TOKEN=<your-access-token> -t itrustar .`

> If you don't have a Github Token, It doesn't matter, the app also works without it. Just remove the `--build-arg GITHUB_ACCESS_TOKEN=<your-access-token>` param from the command above.

### Run the container
`docker container run -p 8000:8000 --name ctrustar itrustar`

Visit `http://localhost:8000/` to see the results.


# Important
The application will take its time to present the final results, it all depends on how many files are in the repo.