# Task 2: Shopping List Manager
# Step 1- Create an empty list.
# Step 2 - Ask the user to enter 3 shopping items (one by one).
# Step 3 - Add them to the list.
# # Step 4 - Display the list as a single string, separated by commas.

# Using complete control flow
shopping_list = []

for i in range(3):
    try:
        item = input(f"Enter shopping item {i + 1}: ")
        if not item.strip():  # if the input is empty
            raise ValueError("Item cannot be empty!")
        shopping_list.append(item)
    except ValueError as e:
        print(f"Error: {e}. Please try again.")
        # retry the same index
        item = input(f"Re-enter shopping item {i + 1}: ")
        shopping_list.append(item)
    finally:
        print(f"Step {i + 1} completed.\n")

print("Shopping List: " + ", ".join(shopping_list))