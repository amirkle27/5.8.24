def perform_action (action):
    actions = {'add': 'Adding item','delete': 'Deleting item','update': 'Updating item','_': 'Unknown action'}
    return actions.get(action)
action = input("Which action? ['add','delete','update','_']")

output = perform_action(action)
print(output) # Output: Adding item

