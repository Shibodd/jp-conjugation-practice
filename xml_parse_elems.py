import xml.sax.handler
import xml.sax

def __get_handler(elementName, elementCallback, stripValues = True):
  """
  Returns an instance of xml.sax.handler.ContentHandler which builds a dictionary for each element with name elementName.
  When each element tagged elementName ends, it calls elementCallback, passing the dictionary as parameter.

  If there are nested elements with tag elementName, an exception is raised.

  If an element contains both text content and nested elements at the same time, an exception is raised.
  """

  class DictBuilderHandler(xml.sax.handler.ContentHandler):    
    @classmethod
    def startDocument(self):
      # Maintain a stack of the levels of the nested dictionaries
      self.stack = []
      self.content = ""

    @classmethod
    def startElement(self, name, attrs):
      if name == elementName:
        if len(self.stack) > 0:
          # The stack is cleared every time an element tagged elementName ends
          # and is filled only when an element tagged elementName begins.
          # Therefore, if the stack is not empty and an element tagged elementName begins,
          # then the two elementName tagged elements are nested, which is not supported.
          raise Exception("Nested element found.")
        self.stack.append({})
      
      elif len(self.stack) > 0:
        # Append the element to the stack.
        self.stack.append({})

    @classmethod
    def endElement(self, name):
      if len(self.stack) <= 0:
        return
      
      el = self.stack.pop()

      if len(self.content) > 0 and len(el) > 0:
        raise Exception("An element contains both text content and inner elements.")
      
      if len(el) == 0:
        el = self.content if len(self.content) > 0 else None

      self.content = ""

      if len(self.stack) <= 0:
        # The top of the stack was the elementName tagged element itself, so if the stack is empty that element should be ending
        if name != elementName:
          raise Exception("Some XML tag has not been closed.")
        
        # The elementName tagged element ended, so we successfully parsed it.
        elementCallback(el)
        self.stack.clear()
        return

      # An inner element is ending. Store it in the parent dictionary.

      parent = self.stack[-1]
      if name not in parent:
        # Try to avoid creating unnecessary lists. Assume we will find this name-tagged inner element only once.
        parent[name] = el
      
      else:
        # We were wrong, so put keep the elements in a list instead
        if isinstance(parent[name], list):
          parent[name].append(el)
        else:
          parent[name] = [ parent[name], el ]

    @classmethod
    def characters(self, chars):
      if len(self.stack) <= 0:
        return

      val = chars.strip() if stripValues else chars
      if len(val) > 0:
        # We found text, so add it to the current element's content.
        self.content += val

  return DictBuilderHandler()

def parse_xml(source, elementName, elementCallback, stripValues = True):
  """
  Parses an xml document, and calls elementCallback for each element
  with tag elementName with a dictionary representing the element as parameter.

  The elements tagged elementName must not be nested.

  Elements can either have nested elements OR textual content, not both at the same time.
  """
  xml.sax.parse(source, __get_handler(elementName, elementCallback, stripValues))