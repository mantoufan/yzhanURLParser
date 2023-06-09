# yzhanURLParser
![PyPI](https://img.shields.io/pypi/v/yzhanurlparser)
![PyPI - Format](https://img.shields.io/pypi/format/yzhanurlparser)
![PyPI - Downloads](https://img.shields.io/pypi/dm/yzhanurlparser)
![GitHub](https://img.shields.io/github/license/mantoufan/yzhanURLParser)  
A python library which could parse URL to ip and country.
## Usage
### Install
```shell
pip install yzhanurlparser
```

### API
#### Is IP
```python
from yzhanurlparser import is_ip
is_ip('123') # False
is_ip('8.8.8.8') # True
```

#### Get Info By IP
```python
from yzhanurlparser import get_info_by_ip
get_info_by_ip('8.8.8.8')
# {'ip': '8.8.8.8', 'country_short': 'US', 'country_long': 'United States of America'}
```

#### Get Country By IP
```python 
from yzhanurlparser import get_country_by_ip
get_country_by_ip('8.8.8.8') # US
get_country_by_ip('114.114.114.114') # CN
```

#### Get Info By URL
```python
from yzhanurlparser import get_info_by_url
get_info_by_url('https://www.163.com')
# {'ip': '183.3.203.247', 'country_short': 'CN', 'country_long': 'China'}
```

#### Get Country By URL
```python 
from yzhanurlparser import get_country_by_url
get_country_by_url('https://www.163.com') # CN
```

## Development
### Install
```shell
pip install -r requirements.txt
```

### Unit Test
```shell
cd yzhanurlparser
python -m unittest discover -s test -p '*_test.py'
```

### Build
```shell
pip install --user --upgrade setuptools wheel twine # First Run
python setup.py sdist bdist_wheel
```

## Thanks
[ip2location](https://lite.ip2location.com)