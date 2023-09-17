# Practice Set 04: Avert Dessert Disaster

from typing import Dict, List


def load_content_section(file_name: str) -> List[List[str]]:
    result = []
    
    try:
        with open(file_name, 'r') as file:
            current_section = []
            for line in file:
                line = line.strip()
                if not line:
                    if current_section:
                        result.append(current_section)
                    current_section = []
                else:
                    current_section.extend(line.split())
            
            if current_section:
                result.append(current_section)
    
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    
    return result

# Test the function
file_name = "data/four_words/four_words.content-cmdt"
content = load_content_section(file_name)
print(content)


def load_data_section(file_name: str) -> Dict[str, str]:
    pass


def load_cmdt(path_name: str) -> tuple[List[List[str]], Dict[str, str]]:
    pass


def cmdt_to_plaintext(
    content_section: List[List[str]], data_section: Dict[str, str]
) -> str:
    pass


def build_list_of_recipes(plaintext: str) -> List[str]:
    pass


# if __name__ == "__main__":
#     # Reconstruct the plaintext
#     content, data = load_cmdt("data/desserts/desserts")
#     plaintext = cmdt_to_plaintext(content, data)

#     # Show the plaintext and the list of recipes
#     print(plaintext)
#     print(build_list_of_recipes(plaintext))
