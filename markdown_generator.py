import ast


def generate_documentation(source, module_name="module"):
    tree = ast.parse(source)

    lines = [f"# {module_name}", ""]

    module_doc = ast.get_docstring(tree)
    if module_doc:
        lines.extend([module_doc, ""])

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            doc = ast.get_docstring(node) or "No documentation available."
            lines.extend([
                f"## Function: {node.name}",
                "",
                doc,
                ""
            ])

        elif isinstance(node, ast.ClassDef):
            doc = ast.get_docstring(node) or "No documentation available."
            lines.extend([
                f"## Class: {node.name}",
                "",
                doc,
                ""
            ])

    return "\n".join(lines).rstrip() + "\n"
