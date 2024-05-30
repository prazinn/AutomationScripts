import json


def get_connection_count(HealthCheckQCP):
    try:
        with open('HealthCheckQCP.txt', 'r') as file:
            # Read the contents of the file
            content = file.read()
            print("File Content:")
            print(content)

            # Parse the JSON response
            data = json.loads(content)

            print("Parsed JSON:")
            print(data)

            # Extract the connection_count value
            for item in data['data']:
                if item['name'] == 'DatabaseConnectionCount':
                    connection_count_str = item['shortSummary']
                    print("Connection Count String:")
                    print(connection_count_str)
                    # Extract the integer part of the string
                    connection_count = int(connection_count_str.split()[0])
                    return connection_count

            print("DatabaseConnectionCount not found in the response.")
            return None
    except FileNotFoundError:
        print(f"File not found at path: {HealthCheckQCP}")
        return None

# Example usage:
file_path = 'api_response.txt'  # Replace with your file path
connection_count = get_connection_count(file_path)
if connection_count is not None:
    print(f"Connection count: {connection_count}")