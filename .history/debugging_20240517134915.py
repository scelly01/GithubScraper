from flask import Flask

app = Flask(__name__)

# Define a list of route paths
route_paths = ['/route1', '/route2', '/route3']

# Define a function to handle route
def route_handler(route):
    return f"This is {route}."

# Dynamically create routes using a for loop
for path in route_paths:
    # Generate a unique function name based on the path
    function_name = path.replace('/', '').replace('-', '_') + '_route'
    
    # Define the route handler function dynamically
    globals()[function_name] = lambda route=path: route_handler(route)
    
    # Use the path as the route decorator
    app.route(path)(globals()[function_name])

if __name__ == "__main__":
    app.run(debug=True)
