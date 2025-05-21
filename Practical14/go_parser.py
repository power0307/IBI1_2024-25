import xml.dom.minidom  # Import the DOM parser
import time  # For measuring execution time

start_time = time.time()  # Start timing

# Load and parse the XML file
DOMTree = xml.dom.minidom.parse(r"C:\Users\F\Desktop\IBI1\IBI1_2024-25\Practical14\go_obo.xml")
collection = DOMTree.documentElement  # Get the root element
terms = collection.getElementsByTagName('term')  # Get all <term> elements

# Create a dictionary to store terms by namespace
term_data = {"biological_process": [], "molecular_function": [], "cellular_component": []}

# Loop through all terms
for term in terms:
    # Get the namespace value
    ns = term.getElementsByTagName('namespace')[0].firstChild.nodeValue
    # Get the GO term ID
    term_id = term.getElementsByTagName('id')[0].firstChild.nodeValue
    # Count the number of <is_a> elements
    is_a_count = len(term.getElementsByTagName('is_a'))

    # Append the (id, is_a count) to the appropriate namespace list
    if ns in term_data:
        term_data[ns].append((term_id, is_a_count))

# Print the GO term with the most <is_a> for each namespace
for ns, entries in term_data.items():
    if entries:
        # Find the term with the maximum number of <is_a>
        max_entry = max(entries, key=lambda x: x[1])
        print(f"[DOM] {ns}: GO term with most <is_a> is {max_entry[0]}, count = {max_entry[1]}")
    else:
        print(f"[DOM] {ns}: No GO terms found.")

# Calculate and print the time used
dom_time = time.time() - start_time
print(f"[DOM] Parsing time: {dom_time:.4f} seconds")

import xml.sax  # Import the SAX parser
import time  # For measuring execution time

start_time = time.time()  # Start timing

# Define a content handler for parsing GO terms
class TermHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""  # Current tag name
        self.current_term = {"id": "", "namespace": "", "is_a": []}  # Temporary term info
        self.terms = []  # List of all parsed terms

    def startElement(self, name, attrs):
        self.current_data = name  # Update the current tag
        if name == "term":
            # Reset current term when a new <term> starts
            self.current_term = {"id": "", "namespace": "", "is_a": []}

    def endElement(self, name):
        if name == "term":
            # When </term> ends, add the term to the list
            self.terms.append(self.current_term.copy())
        self.current_data = ""  # Reset current tag

    def characters(self, content):
        content = content.strip()
        if not content:
            return
        # Collect content based on current tag
        if self.current_data == "namespace":
            self.current_term["namespace"] += content
        elif self.current_data == "id":
            self.current_term["id"] += content
        elif self.current_data == "is_a":
            self.current_term["is_a"].append(content)

# Function to parse XML using SAX
def parse_go_xml(file_path):
    parser = xml.sax.make_parser()  # Create a SAX parser
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)  # Disable namespaces
    handler = TermHandler()  # Create handler instance
    parser.setContentHandler(handler)  # Set handler
    parser.parse(file_path)  # Start parsing
    return handler.terms  # Return list of terms

# Function to analyze and print results
def analyze_terms(terms):
    # Dictionary to store terms by namespace
    namespace_stats = {"biological_process": [], "molecular_function": [], "cellular_component": []}
    for term in terms:
        ns = term["namespace"]
        is_a_count = len(term["is_a"])
        if ns in namespace_stats:
            namespace_stats[ns].append((term["id"], is_a_count))

    # Find and print the term with the most <is_a> per namespace
    for ns, entries in namespace_stats.items():
        if entries:
            max_entry = max(entries, key=lambda x: x[1])
            print(f"[SAX] {ns}: GO term with most <is_a> is {max_entry[0]}, count = {max_entry[1]}")
        else:
            print(f"[SAX] {ns}: No GO terms found.")

if __name__ == "__main__":
    file_path = r"C:\Users\F\Desktop\IBI1\IBI1_2024-25\Practical14\go_obo.xml"  # File path
    terms = parse_go_xml(file_path)  # Parse the file
    analyze_terms(terms)  # Analyze and print results

    sax_time = time.time() - start_time  # Measure time
    print(f"[SAX] Parsing time: {sax_time:.4f} seconds")

    # Replace this with the actual DOM time after running the DOM script
    
if  sax_time < dom_time:
    faster = "SAX" 
else :
    faster ="DOM"
print(f"# {faster} was the quickest method.")  # Output the faster method as a comment