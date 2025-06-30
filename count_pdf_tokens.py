import fitz  # PyMuPDF
import tiktoken
import os
import sys
import glob
from datetime import datetime

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    try:
        doc = fitz.open(pdf_path)
        text = "\n".join(page.get_text() for page in doc)
        doc.close()
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

def count_tokens(text, model="gpt-4"):
    """Count tokens in text using tiktoken."""
    try:
        enc = tiktoken.encoding_for_model(model)
        return len(enc.encode(text))
    except Exception as e:
        print(f"Error counting tokens: {e}")
        return None

def save_to_file(content, filename):
    """Save content to a file in the sample_analysis folder."""
    # Create sample_analysis folder if it doesn't exist
    analysis_dir = "sample_analysis"
    if not os.path.exists(analysis_dir):
        os.makedirs(analysis_dir)
    
    filepath = os.path.join(analysis_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return filepath

def process_single_pdf(pdf_path):
    """Process a single PDF file and return its stats."""
    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)
    if text is None:
        return None
    
    # Count tokens
    num_tokens = count_tokens(text)
    if num_tokens is None:
        return None
    
    return {
        'path': pdf_path,
        'tokens': num_tokens,
        'characters': len(text)
    }

def process_folder(folder_path):
    """Process all PDF files in a folder."""
    # Find all PDF files in the folder
    pdf_pattern = os.path.join(folder_path, "*.pdf")
    pdf_files = glob.glob(pdf_pattern)
    
    if not pdf_files:
        print(f"No PDF files found in folder: {folder_path}")
        return
    
    # Capture output in a string
    output_lines = []
    
    output_lines.append(f"# PDF Token Analysis Report")
    output_lines.append(f"**Folder:** `{folder_path}`")
    output_lines.append(f"**Files Found:** {len(pdf_files)} PDF file(s)")
    output_lines.append("")
    
    total_tokens = 0
    total_characters = 0
    results = []
    
    for pdf_file in sorted(pdf_files):
        result = process_single_pdf(pdf_file)
        if result:
            results.append(result)
            total_tokens += result['tokens']
            total_characters += result['characters']
    
    # Create markdown table
    output_lines.append("## Individual File Analysis")
    output_lines.append("")
    output_lines.append("| File Name | Tokens | Characters |")
    output_lines.append("|-----------|--------|------------|")
    
    for result in results:
        filename = os.path.basename(result['path'])
        output_lines.append(f"| {filename} | {result['tokens']:,} | {result['characters']:,} |")
    
    output_lines.append("")
    output_lines.append("## Summary Statistics")
    output_lines.append("")
    output_lines.append("| Metric | Value |")
    output_lines.append("|--------|-------|")
    output_lines.append(f"| **Files Processed** | {len(pdf_files)} |")
    output_lines.append(f"| **Total Tokens** | {total_tokens:,} |")
    output_lines.append(f"| **Total Characters** | {total_characters:,} |")
    output_lines.append(f"| **Average Tokens per File** | {total_tokens // len(pdf_files):,} |")
    output_lines.append(f"| **Average Characters per File** | {total_characters // len(pdf_files):,} |")
    output_lines.append("")
    
    # Additional insights
    output_lines.append("## Additional Insights")
    output_lines.append("")
    if results:
        max_tokens = max(r['tokens'] for r in results)
        min_tokens = min(r['tokens'] for r in results)
        max_chars = max(r['characters'] for r in results)
        min_chars = min(r['characters'] for r in results)
        
        output_lines.append(f"- **Largest file by tokens:** {max_tokens:,} tokens")
        output_lines.append(f"- **Smallest file by tokens:** {min_tokens:,} tokens")
        output_lines.append(f"- **Largest file by characters:** {max_chars:,} characters")
        output_lines.append(f"- **Smallest file by characters:** {min_chars:,} characters")
        output_lines.append(f"- **Token range:** {max_tokens - min_tokens:,} tokens")
        output_lines.append(f"- **Character range:** {max_chars - min_chars:,} characters")
    
    # Join all lines and print to console
    output_content = "\n".join(output_lines)
    print(output_content)
    
    # Save to file
    folder_name = os.path.basename(folder_path.rstrip('\\/'))
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{folder_name}_analysis_{timestamp}.md"
    saved_path = save_to_file(output_content, filename)
    print(f"\n📄 **Report saved to:** `{saved_path}`")

def main():
    # Check if path is provided as command line argument
    if len(sys.argv) != 2:
        print("Usage: python count_pdf_tokens.py <path_to_pdf_or_folder>")
        print("Examples:")
        print("  python count_pdf_tokens.py sample_pdf\\sc4\\chapter_1.pdf")
        print("  python count_pdf_tokens.py sample_pdf\\sc4\\")
        return
    
    path = sys.argv[1]
    
    # Check if path exists
    if not os.path.exists(path):
        print(f"Error: Path '{path}' not found.")
        print("Please make sure the file or folder exists at the specified path.")
        return
    
    # Check if it's a file or folder
    if os.path.isfile(path):
        # Process single file
        if not path.lower().endswith('.pdf'):
            print(f"Error: '{path}' is not a PDF file.")
            return
        
        result = process_single_pdf(path)
        if result:
            # Capture output in a string
            output_lines = []
            
            output_lines.append(f"# Single PDF Analysis Report")
            output_lines.append(f"**File:** `{os.path.basename(path)}`")
            output_lines.append("")
            output_lines.append("## Statistics")
            output_lines.append("")
            output_lines.append("| Metric | Value |")
            output_lines.append("|--------|-------|")
            output_lines.append(f"| **Tokens** | {result['tokens']:,} |")
            output_lines.append(f"| **Characters** | {result['characters']:,} |")
            output_lines.append("")
            output_lines.append(f"**Estimated number of tokens:** {result['tokens']:,}")
            output_lines.append(f"**Text length:** {result['characters']:,} characters")
            
            # Join all lines and print to console
            output_content = "\n".join(output_lines)
            print(output_content)
            
            # Save to file
            file_name = os.path.splitext(os.path.basename(path))[0]
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{file_name}_analysis_{timestamp}.md"
            saved_path = save_to_file(output_content, filename)
            print(f"\n📄 **Report saved to:** `{saved_path}`")
    
    elif os.path.isdir(path):
        # Process folder
        process_folder(path)
    
    else:
        print(f"Error: '{path}' is neither a file nor a directory.")

if __name__ == "__main__":
    main() 