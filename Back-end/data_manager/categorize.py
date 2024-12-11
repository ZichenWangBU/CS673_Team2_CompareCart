import json

def parse_taxonomy(file_path, output_path):
    root = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            path = line.strip()
            if not path:
                continue

            nodes = path.split(' > ')

            current_level = root
            for node in nodes:
                if node not in current_level:
                    current_level[node] = {}
                current_level = current_level[node]

    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(root, json_file, indent=4, ensure_ascii=False)
    print(f"JSON saved to {output_path}")

def count_leaf_nodes(node):
    if not isinstance(node, dict) or not node:  
        return 1
    return sum(count_leaf_nodes(child) for child in node.values())

def get_num_ends(json_file):
    return count_leaf_nodes(data)


def get_leaf_nodes(node):
    if not isinstance(node, dict) or not node: 
        return [node] if node else []
    leaf_nodes = []
    for key, child in node.items():

        leaf_nodes.extend(get_leaf_nodes(child))
    return leaf_nodes


file_path = "taxonomy.en-US" 
output_path = "taxonomy.json" 


if __name__== "__main__":
    #parse_taxonomy(file_path, output_path)
    #keys=get_first_level_keys("taxonomy.json")
    with open(output_path,'r', encoding='utf-8') as file:
        data = json.load(file)
    for key in list(data.keys()):
        print(key+":",count_leaf_nodes(data[key]))
    for key in list(data["Office Supplies"].keys()):
        print(key+":",get_leaf_nodes(data["Office Supplies"][key]))
