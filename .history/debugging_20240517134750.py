from flask import Flask

app = Flask(__name__)

# Define a list of route paths
route_paths = ['/route1', '/route2', '/route3']

# Define a function to handle route
def route_handler(route):
    return f"This is {route}."

# Dynamically create routes using a for loop
for path in route_paths:
    # Use the path as the route decorator
    @app.route(path)
    def dynamic_route():
        # Call the route handler function with the current path
        return route_handler(path)

if __name__ == "__main__":
    app.run(debug=True)
