# finsee
help see your financial both income and outcome

project is still in progress nightly

# Install Requirements
Install python
```
pip install -r requirements.txt
```

# running the app
```
honcho start
```
# using Docker
running application using docker
```
make up
```
to see the app running as expected:
```
docker ps
```
Output Example:
```
CONTAINER ID        IMAGE                      COMMAND                  CREATED             STATUS              PORTS                    NAMES
970c68d00e6b        ahmadsyafrudin/finsee:v1   "/bin/sh -c 'uwsgi -…"   28 seconds ago      Up 5 seconds        0.0.0.0:8000->8000/tcp   finsee_finsee_1
```
