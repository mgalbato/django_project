# Weather Powered Email Project

## Steps to Run:
1. Set up a Python3.7 environment with numpy, pandas, requests, and django installed. You can see the exact versions below.
2. You can access the main signup page at localhost:8000/, and sign up whatever emails you want.
3. You can access the admin page at localhost:8000/admin using the username: mgalbato and password: testpassword
4. You can run the management command by navigating to the django_project directory and running ```python python manage.py email_command ```.

## Citations:
I used [this source](https://simplemaps.com/data/us-zips) for the population data and used [this tool](https://arendjr.github.io/selectivity/) for the dropdown selector functionality.

## Notes:
My data source didn't include Anchorage nor Boston in the list of 100 most populous cities. So instead, I assigned weatherapp+anc@klaviyo.com to Albuquerque and weatherapp+bos@klaviyo.com to New York. Obviously, I am not using Albuquerque as a proxy for Anchorage weather, but I just needed to select some city for demonstration purposes.

## Packages in Environment:
|     Name      |    Version    |
| ------------- | ------------- | 
|asn1crypto            |    0.24.0       |  
|blas                   |   1.0          |              
|ca-certificates        |  2019.5.15     |                
|certifi                |   2019.6.16    |          
|cffi                   |   1.12.3       |    
|chardet                |   3.0.4        |         
|cryptography           |   2.7          |    
|django                 |   2.2.4        |      
|django-static-jquery   |   2.1.4        |   
|idna                   |   2.8          |   
|intel-openmp           |   2019.4       |   
|libcxx                 |   4.0.1        |     
|libcxxabi              |   4.0.1        |     
|libedit                |   3.1.20181209 |     
|libffi                 |   3.2.1        |    
|libgfortran            |   3.0.1        |    
|mkl                    |   2019.4       |      
|mkl_fft                |   1.0.12       |   
|mkl_random             |   1.0.2        |   
|ncurses                |   6.1          |   
|numpy                  |   1.16.4       |  
|numpy-base             |   1.16.4       |    
|openssl                |   1.1.1        |    
|pandas                 |   0.25.0       |   
|pip                    |   19.1.1       |        
|pycparser              |   2.19         |     
|pyopenssl              |   19.0.0       |       
|pysocks                |   1.7.0        |       
|python                 |   3.7.3        |    
|python-dateutil        |   2.8.0        |       
|pytz                   |   2019.2       |          
|readline               |   7.0          |     
|requests               |   2.22.0       |          
|setuptools             |   41.0.1       |         
|six                    |   1.12.0       |           
|sqlite                 |   3.29.0       |     
|sqlparse               |   0.3.0        |         
|tk                     |   8.6.8        |      
|urllib3                |   1.24.2       |      
|wheel                  |   0.33.4       |         
|xz                     |   5.2.4        |      
|zlib                   |   1.2.11       | 

