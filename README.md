# SEEK Assessment AIPS
## Steps to run the program
### 1. Install docker (debian - apt install docker, fedora/centos/RHEL - yum install docker)
### 2. git clone this repository
### 3. cd into the downloaded repository
### 4. $ sudo docker build -t assessment . 
![image](https://user-images.githubusercontent.com/17043489/167782851-f0c33e85-049a-4f73-9c8e-db4bd1e36f37.png)

### 5. $ sudo docker run assessment
![image](https://user-images.githubusercontent.com/17043489/167782975-a49d2627-ad09-41cf-a02d-3b20ce1b9881.png)

## Input data assumptions.
#### Assuming that the input data is consistant as it is machine generated, We have assumed that the data provided in the sample can be assigned to 0 for the missing timestamp values.

## Output for sample data provided.

![image](https://user-images.githubusercontent.com/17043489/167780349-a46976b8-0b0f-4aea-847b-8edebc3e2f65.png)

## Tests
### Test are locally performed in the test/ directory. with the sample data in test/test_data/ directory.
### change the path for raw data manually in the test.py code 
#### for example : directory = '/home/vipuljad/assessment/test/test_data/'
#### test logs and outputs are saved in test/test_log.log file.
