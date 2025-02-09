import ast
import astor

class CodeModifier:
    def modify_code(self, command):
        try:
            # Example: "modify code to add a new feature"
            new_code = self._generate_code_from_command(command)
            with open("src/app/assistant.py", "r") as f:
                tree = ast.parse(f.read())
            
            # Add new code to the AST
            new_node = ast.parse(new_code)
            tree.body.extend(new_node.body)
            
            # Write modified code back
            with open("src/app/assistant.py", "w") as f:
                f.write(astor.to_source(tree))
            
            return "Code modified successfully!"
        except Exception as e:
            return f"Failed to modify code: {str(e)}"

    def _generate_code_from_command(self, command):
        # This is a placeholder for AI-generated code
        return """
def new_feature(self):
    return "This is a new feature!"
"""