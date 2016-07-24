

# Send Flask to AWS Lambda with Zappa

 ## Heλλo Worλd, the most basic template
 
  	Heλλo! This is a minimal Python [Flask](http://flask.pocoo.org/docs/0.11/tutorial/) app for getting started with [Amazon Lambda](https://aws.amazon.com/lambda/). All the Lambda magic is handled by [Zappa](https://zappa.gun.io/). 

# Why?

The goal of this exercise is to get a minimal working Flask app to use a jumping off point for future projects.


# Development

## Getting started, run locally

Environment setup

	virtualenv venv
	pip install Flask
 	pip install -r requirements.txt

Actually run the Flask app. 

 	FLASK_APP=flask-demo.py python -m flask run

## Now run in the cloud

Environment setup

Check out `zappa_settings.json.default`. At the very least, you'll need a region `"aws_region"`, an S3 bucket `"s3_bucket"` to push the zip of this project to, and a pointer to the entry point `app_function"`. If you want environment variables, you can put them in a file `"remote_env_file"`in a(nother) bucket `"remote_env_bucket"`.

Send to the cloud

1. First time, builds the routes which can take a while. This will give a link to the active Lambda app.

	zappa deploy dev 

2. Future iterations

	zappa update dev 
	
3. Cleanup when done

	zappa undeploy dev
