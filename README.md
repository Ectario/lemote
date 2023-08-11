# lemote
Create the dockerfile and the docker compose file automatically to simulate a remote challenge but in local

## Example

If we want params.py and local.py to be used, and the local.py is the main file to execute :

lemote -f ./local.py,./params.py -m ./local.py -p .
