# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root.handler = root_handler
        return

    def insert(self, domain_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for domain in domain_list:
            if domain not in current_node.children:
                current_node.insert(domain)
            current_node = current_node.children[domain]
        current_node.handler = handler
        return

    def find(self, domain_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for domain in domain_list:
            if domain not in current_node.children:
                return None
            current_node = current_node.children[domain]
        return current_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None
        return

    def insert(self, domain):
        # Insert the node as before
        self.children[domain] = RouteTrieNode()
        return


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routeTrie = RouteTrie(root_handler)
        return

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if path == "":
            path = "/"
        domain_list = self.split_path(path)
        self.routeTrie.insert(domain_list, handler)
        print(f"Successfully add a handler \'{handler}\' to \'{path}\'")
        return

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        domain_list = self.split_path(path)
        return self.routeTrie.find(domain_list)


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return [domain for domain in path.split("/") if domain]

# Here are some test cases and expected outputs you can use to test your implementation

# Case 1
print("Test Case 1:")
# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one


# Case 1
print("Test Case 2:")
# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/", "new root handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # new root handler
print(router.lookup("/home")) # None
print(router.lookup("/home/about")) # None



# Case 1
print("Test Case 3:")
# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/my-blog/photos", "photos handler")  # add a route
router.add_handler("/home/my-blog", "blog handler")  # add a route
router.add_handler("/home", "home handler")  # add a route
router.add_handler("", "new root handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # new root handler
print(router.lookup("")) # new root handler
print(router.lookup("/home")) # home handler
print(router.lookup("/home/my-blog/photos/")) # photos handler