# Mac-Address-Vendor-Validator
This script helps to get the vendor's data of a mac address, data is being consumed via API from Mac Address io

### How to get my own API KEY?
You can register to get your own api key by visiting https://macaddress.io, once done, do not forget to place it into the code line 7

### How to build the docker container ?
To build the docker container run:
```bash
docker build -t mac_address_vendor .
``` 

### How to run the docker container ?
To execute the docker container run:
```bash
docker run mac_address_vendor "arguments"
``` 
### Arguments
There  are two command lines you can use:
* Use -h or --help to get more info on how to use the project
* Use -a or --address to specify the mac address we want to get data for
