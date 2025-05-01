import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def make_request(status_code):
    url = f"https://httpstat.us/{status_code}"
    
    try:
        logger.info(f"Выполняется запрос к {url}")
        response = requests.get(url)
        
        received_status = response.status_code
        
        if 100 <= received_status < 400:
            logger.info(f"Status code: {received_status}")
            logger.info(f"Response body: {response.text}")
        elif 400 <= received_status < 600: 
            error_msg = f"Error! Status code: {received_status}"
            logger.error(error_msg)
            raise Exception(error_msg)
        else:
            logger.warning(f"Unexpected status code: {received_status}")
            
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        
def main():
    status_codes = [
        200,  # OK (2xx)
        301,  # Moved Permanently (3xx)
        404,  # Not Found (4xx)
        500,  # Internal Server Error (5xx)
        101   # Switching Protocols (1xx)
    ]
    
    for status_code in status_codes:
        make_request(status_code)
        print("-" * 50) 
        
if __name__ == "__main__":
    main()