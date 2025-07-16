class Solution:
    def simplifyPath(self, path: str) -> str:
        parts: list[str] = [part for part in path.split('/') if part]
    
        # Use a stack to build the canonical path
        stack: list[str] = []
        
        for part in parts:
            if part == '..':
                # Go to parent directory (pop from stack if not empty)
                if stack:
                    stack.pop()
            elif part != '.':
                # Add valid directory/file names to stack
                # Skip current directory markers ('.')
                stack.append(part)
            # Note: '.' is ignored (current directory)
        
            # Build the result path
        return '/' + '/'.join(stack)

        