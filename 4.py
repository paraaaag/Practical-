class TextEditor:
    def __init__(self):
       self.document = ""  
       self.undo_stack = []          
       self.redo_stack = []          
    def make_change(self, new_text): 
        self.undo_stack.append(self.document)
        self.redo_stack.clear()
        self.document = new_text
        print("Change made.")
        self.display_document()
    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.document)
            self.document = self.undo_stack.pop()
            print("Undo performed.")
        else:
            print("Nothing to undo.")
        self.display_document()
    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.document)
            self.document = self.redo_stack.pop()
            print("Redo performed.")
    else:
            print("Nothing to redo.")
        self.display_document()
    def display_document(self):
        print("Current Document State:")
        print(self.document)
        print("-" * 30) 
editor = TextEditor()
editor.make_change("Hello")
editor.make_change("Hello, nice to meet you! ")
editor.make_change("Hello, nice to meet you! are you busy tomorrow ?") 
editor.undo()
editor.undo()
editor.redo()
editor.make_change("New line added.") 
editor.undo()
