# lemote
Create the dockerfile and the docker compose file automatically to simulate a remote challenge but in local

## Example

If we want params.py and local.py to be used, and the local.py is the main file to execute (the -p . means we want the dockerfile and docker-compose being in the current folder):

lemote -f ./local.py,./params.py -m ./local.py -p .
