from flask import Flask

app = Flask(__name__)

# Define a list of route paths
route_paths = ['/route1', '/route2', '/route3']

# Define a function to handle route
def route_handler(route):
    return f"This is {route}."

# Define the route handler function dynamically
    def route_handler_wrapper(route=path):
        return route_handler(route)
    
# Dynamically create routes using a for loop
for path in route_paths:
    
    
    # Use add_url_rule to add routes dynamically
    app.add_url_rule(path, f'route_{path}', route_handler_wrapper)

if __name__ == "__main__":
    app.run(debug=True)
